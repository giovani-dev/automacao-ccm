"""Orquestrador central da automação de consulta e extração de documentos fiscais municipais."""

import logging
from ports.data_source_port import DataSourcePort
from ports.storage_port import StoragePort
from ports.municipality_port import MunicipalityPort
from core.registry import MunicipalityRegistry
from core.dtos import CompanyDTO, ProcessingResultDTO

logger = logging.getLogger(__name__)


class CCMOrchestrator:
    # pylint: disable=too-few-public-methods
    """Orquestrador responsável pela automação completa do fluxo de processamento.

    Coordena a leitura de dados, consulta de prefeituras, download de documentos,
    armazenamento em disco e atualização do registro de resultados.
    """

    def __init__(
        self,
        data_source: DataSourcePort,
        storage: StoragePort,
        municipality_registry: MunicipalityRegistry,
    ) -> None:
        """Inicializa o orquestrador com as dependências injetadas.

        Args:
            data_source (DataSourcePort): Implementação do adaptador de fonte de dados.
            storage (StoragePort): Implementação do adaptador de armazenamento.
            municipality_registry (MunicipalityRegistry): Registry com mapeamento de municípios.
        """
        self._data_source = data_source
        self._storage = storage
        self._municipality_registry = municipality_registry

    def process_all(self) -> None:
        """Executa o fluxo completo de processamento para todas as empresas.

        Itera sobre as empresas fornecidas pela fonte de dados, busca informações
        de cada prefeitura, baixa documentos e atualiza o registro de resultados.
        """
        for company in self._data_source.get_companies():
            logger.info(
                "Processando empresa CNPJ %s em %s", company.cnpj, company.municipio
            )

            # Obtém o adaptador do município
            municipality_adapter = self._municipality_registry.get(company.municipio)

            # Verifica se o município está registrado
            if municipality_adapter is None:
                result = ProcessingResultDTO(
                    success=False,
                    error_message=(
                        f"Município '{company.municipio}' "
                        "não possui adaptador registrado."
                    ),
                )
                logger.warning("Adaptador não encontrado para %s", company.municipio)
                self._data_source.save_result(company, result)
                continue

            result = self._process_company(company, municipality_adapter)

            # Persiste o resultado
            self._data_source.save_result(company, result)

    def _process_company(
        self, company: CompanyDTO, municipality_adapter: MunicipalityPort
    ) -> ProcessingResultDTO:
        """Processa uma empresa individual consultando seus dados municipais.

        Args:
            company: DTO da empresa com CNPJ e município.
            municipality_adapter: Adaptador concreto do município.

        Returns:
            ProcessingResultDTO: Resultado do processamento com status e caminhos dos arquivos.
        """
        try:
            # Passo 1: Consultar o CCM
            ccm = municipality_adapter.get_ccm(company.cnpj)
            if not ccm:
                return ProcessingResultDTO(
                    success=False,
                    error_message=f"CCM não encontrado para CNPJ {company.cnpj}",
                )

            # Passo 2: Baixar comprovante de cadastro
            ccm_receipt_data = municipality_adapter.download_ccm_receipt(
                company.cnpj, ccm
            )
            ccm_receipt_path = None
            if ccm_receipt_data:
                ccm_receipt_path = self._storage.save_document(
                    file_name="comprovante_ccm.pdf",
                    file_data=ccm_receipt_data,
                    municipality=company.municipio,
                    cnpj=company.cnpj,
                )
                logger.info("Comprovante CCM salvo em %s", ccm_receipt_path)

            # Passo 3: Baixar nota fiscal
            invoice_data = municipality_adapter.download_invoice(company.cnpj, ccm)
            invoice_path = None
            if invoice_data:
                invoice_path = self._storage.save_document(
                    file_name="nota_fiscal.pdf",
                    file_data=invoice_data,
                    municipality=company.municipio,
                    cnpj=company.cnpj,
                )
                logger.info("Nota fiscal salva em %s", invoice_path)

            # Passo 4: Retornar resultado de sucesso
            return ProcessingResultDTO(
                success=True,
                ccm=ccm,
                ccm_receipt_path=ccm_receipt_path,
                invoice_path=invoice_path,
            )

        except Exception as e:  # pylint: disable=broad-exception-caught
            logger.error("Erro ao processar empresa %s: %s", company.cnpj, str(e))
            return ProcessingResultDTO(
                success=False, error_message=f"Erro durante processamento: {str(e)}"
            )
