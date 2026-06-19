"""Utilitários para aplicação de Circuit Breaker nos adaptadores de Município."""

from functools import wraps
from typing import Callable, Any
from pybreaker import CircuitBreaker
from core.circuit_breaker_config import CircuitBreakerConfig


def with_circuit_breaker(
    method_name: str, config: CircuitBreakerConfig
) -> Callable[..., Any]:
    """Decorator que aplica Circuit Breaker a um método.

    Facilita a aplicação de proteção de falhas em métodos que fazem chamadas
    a serviços externos (APIs, Web Scraping, etc).

    Args:
        method_name (str): Nome descritivo do método (ex: 'get_ccm', 'download_invoice').
        config (CircuitBreakerConfig): Configuração global do circuit breaker.

    Returns:
        Callable: Decorator que envolve o método com proteção de circuit breaker.

    Example:
        >>> config = CircuitBreakerConfig(fail_max=5, reset_timeout=60)
        >>> @with_circuit_breaker('get_ccm', config)
        >>> def get_ccm(self, cnpj: str) -> Optional[str]:
        ...     return self._fetch_ccm(cnpj)
    """
    breaker = CircuitBreaker(
        fail_max=config.fail_max,
        reset_timeout=config.reset_timeout,
        name=f"{config.name_prefix}_{method_name}",
    )

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return breaker.call(func, *args, **kwargs)

        return wrapper

    return decorator
