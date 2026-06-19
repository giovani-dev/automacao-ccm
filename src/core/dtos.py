"""Data Transfer Objects (DTOs) para a automação de CCM."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class CompanyDTO:
    """Representa os dados de uma empresa extraídos da fonte de dados.

    Attributes:
        cnpj (str): O CNPJ da empresa (preferencialmente apenas números).
        municipio (str): O nome do município da empresa.
    """

    cnpj: str
    municipio: str


@dataclass
class ProcessingResultDTO:
    """Representa o resultado da automação para uma empresa específica.

    Attributes:
        success (bool): Indica se o processamento foi concluído com sucesso.
        ccm (Optional[str]): O número da Inscrição Municipal, caso encontrado.
        ccm_receipt_path (Optional[str]): Caminho local onde o comprovante foi salvo.
        invoice_path (Optional[str]): Caminho local onde a nota fiscal foi salva.
        error_message (Optional[str]): Detalhes do erro, em caso de falha.
    """

    success: bool
    ccm: Optional[str] = None
    ccm_receipt_path: Optional[str] = None
    invoice_path: Optional[str] = None
    error_message: Optional[str] = None
