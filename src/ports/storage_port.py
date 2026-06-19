"""Porta para armazenamento de arquivos físicos."""

from abc import ABC, abstractmethod


class StoragePort(ABC):
    # pylint: disable=too-few-public-methods
    """Interface abstrata para persistência de arquivos em disco ou cloud."""

    @abstractmethod
    def save_document(
        self, file_name: str, file_data: bytes, municipality: str, cnpj: str
    ) -> str:
        """Salva um documento e sua respectiva estrutura de pastas.

        O adaptador implementando este método deverá garantir a criação
        da estrutura do tipo `[municipality]/[cnpj]`.

        Args:
            file_name (str): Nome do arquivo com a extensão (ex: 'comprovante.pdf').
            file_data (bytes): O conteúdo binário do arquivo baixado.
            municipality (str): Nome do município para compor a pasta.
            cnpj (str): CNPJ da empresa para compor a pasta.

        Returns:
            str: O caminho (absoluto ou relativo) onde o arquivo foi efetivamente salvo.
        """
