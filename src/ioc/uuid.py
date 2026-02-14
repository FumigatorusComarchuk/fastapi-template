from uuid import uuid4

from dishka import Provider, Scope, provide

from src.application import interfaces


class UUIDProvider(Provider):
    @provide(scope=Scope.APP)
    def get_uuid_generator(self) -> interfaces.UUIDGenerator:
        return uuid4
