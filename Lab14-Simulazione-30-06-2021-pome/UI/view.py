import flet as ft


class View(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        # page stuff
        self._page = page
        self._page.title = "Template application using MVC and DAO"
        self._page.horizontal_alignment = 'CENTER'
        self._page.theme_mode = ft.ThemeMode.LIGHT
        # controller (it is not initialized. Must be initialized in the main, after the controller is created)
        self._controller = None

        # graphical elements
        self._title = None
        self.txt_name = None
        self.btn_graph = None
        self.btn_countedges = None
        self.btn_search = None
        self.btn_statistiche = None
        self.ddLocalizzazione = None
        self.txt_result = None
        self.txt_result2 = None
        self.txt_result3 = None
        self.txt_container = None

    def load_interface(self):
        # title
        self._title = ft.Text("Lab14-Simulazione esame gene_small", color="blue", size=24)
        self._page.controls.append(self._title)
        self.ddLocalizzazione = ft.Dropdown(label = "Localizazione")
        row1 = ft.Row([self.ddLocalizzazione],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row1)
        # List View where the reply is printed
        self.txt_result = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self.controller.fillDD()
        self._page.controls.append(self.txt_result)
        self._page.update()
        self.btn_statistiche = ft.ElevatedButton(text="Statistiche", on_click=self._controller.handle_statistiche)
        row2 = ft.Row([self.btn_statistiche],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row2)
        # List View where the reply is printed
        self.txt_result2 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result2)
        self._page.update()
        self.btn_search = ft.ElevatedButton(text="Cerca cammino", on_click=self._controller.handle_search)
        row3 = ft.Row([self.btn_search],
                      alignment=ft.MainAxisAlignment.CENTER)
        self._page.controls.append(row3)
        # List View where the reply is printed
        self.txt_result3 = ft.ListView(expand=1, spacing=10, padding=20, auto_scroll=True)
        self._page.controls.append(self.txt_result3)
        self._page.update()
    @property
    def controller(self):
        return self._controller

    @controller.setter
    def controller(self, controller):
        self._controller = controller

    def set_controller(self, controller):
        self._controller = controller

    def create_alert(self, message):
        dlg = ft.AlertDialog(title=ft.Text(message))
        self._page.dialog = dlg
        dlg.open = True
        self._page.update()

    def update_page(self):
        self._page.update()
