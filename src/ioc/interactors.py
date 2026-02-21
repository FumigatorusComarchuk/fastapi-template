from dishka import Provider, Scope, provide

from src.application.interactors import (
    GetDossierInteractor,
    NewDossierInteractor,
    GetDossierListInteractor,
)


class InteractorsProvider(Provider):
    get_dossier_list_interactor = provide(
        GetDossierListInteractor, scope=Scope.REQUEST)
    get_dossier_interactor = provide(GetDossierInteractor, scope=Scope.REQUEST)
    create_new_dossier_interactor = provide(
        NewDossierInteractor, scope=Scope.REQUEST)
