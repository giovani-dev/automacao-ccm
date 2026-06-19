"""Porta para interação com as fontes de dados (Planilhas, DBs, JSON, etc)."""

from abc import ABC, abstractmethod
from typing import Iterable
from core.dtos import CompanyDTO, ProcessingResultDTO


class DataSourcePort(ABC):
    """Interface abstrata para leitura e gravação dos dados do processo."""

    @abstractmethod
    def get_companies(self) -> Iterable[CompanyDTO]:
        """Recupera as empresas a serem processadas.

        A implementação deve suportar o retorno de um gerador (yield) para lidar
        com grandes volumes de dados sem sobrecarregar a memória.

        Returns:
            Iterable[CompanyDTO]: Iterável contendo as DTOs das empresas.
        """

    @abstractmethod
    def save_result(self, company: CompanyDTO, result: ProcessingResultDTO) -> None:
        """Salva o resultado do processamento de uma empresa.

        Args:
            company (CompanyDTO): Os dados da empresa cujos resultados serão gravados.
            result (ProcessingResultDTO): O resultado da execução da automação.
        """
