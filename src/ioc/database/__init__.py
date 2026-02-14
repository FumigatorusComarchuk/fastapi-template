from .session import DatabaseSessionProvider  # noqa: 401
from .gateways import DatabaseGatewaysProvider  # noqa: F401


class DatabaseProvider(DatabaseSessionProvider, DatabaseGatewaysProvider):
    pass
