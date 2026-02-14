from .database import DatabaseProvider
from .interactors import InteractorsProvider
from .uuid import UUIDProvider


class AppProvider(DatabaseProvider, UUIDProvider, InteractorsProvider):
    pass
