"""Registry para gerenciamento e localização dinâmica de adaptadores de Municípios."""

from typing import Dict, Optional
from ports.municipality_port import MunicipalityPort


class MunicipalityRegistry:
    """Implementa o padrão Registry para mapeamento dinâmico de municípios aos seus adaptadores.

    Este padrão permite que o Orchestrator descubra o adaptador correto de município
    em tempo de execução, sem necessidade de acoplamento direto.
    """

    def __init__(self) -> None:
        """Inicializa o registro de municípios vazio."""
        self._municipalities: Dict[str, MunicipalityPort] = {}

    def register(self, municipality_name: str, adapter: MunicipalityPort) -> None:
        """Registra um adaptador de município no registry.

        Args:
            municipality_name (str): Nome único do município (ex: 'SÃO PAULO', 'RIO DE JANEIRO').
            adapter (MunicipalityPort): Instância do adaptador implementando MunicipalityPort.
        """
        self._municipalities[municipality_name.upper()] = adapter

    def get(self, municipality_name: str) -> Optional[MunicipalityPort]:
        """Recupera o adaptador associado a um município.

        Args:
            municipality_name (str): Nome do município a buscar.

        Returns:
            Optional[MunicipalityPort]: O adaptador relativo ao município,
                ou None se não registrado.
        """
        return self._municipalities.get(municipality_name.upper())

    def is_registered(self, municipality_name: str) -> bool:
        """Verifica se um município está registrado no registry.

        Args:
            municipality_name (str): Nome do município a verificar.

        Returns:
            bool: True se o município está registrado, False caso contrário.
        """
        return municipality_name.upper() in self._municipalities
