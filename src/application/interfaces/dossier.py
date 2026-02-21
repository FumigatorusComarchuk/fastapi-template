from abc import abstractmethod
from typing import List, Protocol

from src.domain.dossier import Dossier


class DossierSaver(Protocol):
    @abstractmethod
    async def save(self, dossier: Dossier) -> None: ...


class DossierReader(Protocol):
    @abstractmethod
    async def read_by_uuid(self, uuid: str) -> Dossier | None: ...

    @abstractmethod
    async def get_all(self) -> List[Dossier] | List: ...
