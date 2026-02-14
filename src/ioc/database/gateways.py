from dishka import Provider, Scope, provide, AnyOf

from src.application import interfaces
from src.infrastructure.database.gateways import DossierGateway


class DatabaseGatewaysProvider(Provider):
    dossier_gateway = provide(
        DossierGateway,
        scope=Scope.REQUEST,
        provides=AnyOf[interfaces.DossierReader, interfaces.DossierSaver],
    )
