from dishka import Provider, Scope, provide

from src.application.interactors import GetDossierInteractor, NewDossierInteractor


class InteractorsProvider(Provider):
    get_dossier_interactor = provide(GetDossierInteractor, scope=Scope.REQUEST)
    create_new_dossier_interactor = provide(
        NewDossierInteractor, scope=Scope.REQUEST)
