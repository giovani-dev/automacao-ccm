"""Configuração centralizada para Circuit Breakers."""

from dataclasses import dataclass


@dataclass
class CircuitBreakerConfig:
    """Configuração global para todos os Circuit Breakers da aplicação.

    Attributes:
        fail_max (int): Número máximo de falhas antes de abrir o circuit.
        reset_timeout (int): Tempo em segundos para tentar resetar o circuit (half-open).
        name_prefix (str): Prefixo para nomes dos circuit breakers (facilita logging).
    """

    fail_max: int = 5
    reset_timeout: int = 60
    name_prefix: str = "ccm_scraper"
