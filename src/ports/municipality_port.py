"""Porta para interação com os serviços e sites das prefeituras."""

from abc import ABC, abstractmethod
from typing import Optional


class MunicipalityPort(ABC):
    """Interface abstrata para os scrapers e APIs de cada município."""

    @abstractmethod
    def get_ccm(self, cnpj: str) -> Optional[str]:
        """Consulta o número de Inscrição Municipal (CCM) a partir do CNPJ.

        Args:
            cnpj (str): O CNPJ que será consultado.

        Returns:
            Optional[str]: O número do CCM da empresa, ou None se não encontrado.
        """

    @abstractmethod
    def download_ccm_receipt(self, cnpj: str, ccm: str) -> Optional[bytes]:
        """Baixa o comprovante de cadastro municipal da empresa.

        Args:
            cnpj (str): O CNPJ da empresa.
            ccm (str): O número da Inscrição Municipal.

        Returns:
            Optional[bytes]: Arquivo em bytes (PDF/Imagem), ou None caso ocorra erro ao baixar.
        """

    @abstractmethod
    def download_invoice(self, cnpj: str, ccm: str) -> Optional[bytes]:
        """Baixa o documento da Nota Fiscal mais recente vinculada à empresa.

        Args:
            cnpj (str): O CNPJ da empresa.
            ccm (str): O número da Inscrição Municipal.

        Returns:
            Optional[bytes]: Arquivo da NF em bytes, ou None caso não encontre ou ocorra erro.
        """
