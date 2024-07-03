import flet as ft

from database.DAO import DAO


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
    def fillDD(self):
        loc = DAO.getLoc()
        for l in loc:
            self._view.ddLocalizzazione.options.append(ft.dropdown.Option(l))
        self._model.creaGrafo(loc)
        self._view.txt_result.controls.append(ft.Text(self._model.stampa()))
        self._view.update_page()

    def handle_statistiche(self, e):
        n, lista = self._model.statistica(self._view.ddLocalizzazione.value)
        for l in lista:
            if l!=n:
                self._view.txt_result.controls.append(ft.Text(f"{l} : {self._model.grafo[n][l]["weight"]}"))
        self._view.update_page()

    def handle_search(self, e):
        list,p = self._model.findPath()
        for l in list:
            self._view.txt_result3.controls.append(ft.Text(f"{l}"))
        self._view.update_page()
