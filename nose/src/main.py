import flet as ft
from controllers.UserControllers import AuthController
from controllers.TareasControllers import TareaController
from view.loginView import LoginView
from view.dashboard import DashboardView

def main(page: ft.Page):
    auth_ctrl = AuthController()
    tarea_ctrl = TareaController() 
    
    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginView(page, auth_ctrl))
        elif page.route == "/dashboard":
            page.views.append(DashboardView(page, auth_ctrl, tarea_ctrl))
        page.update()
    
    page.on_route_change = route_change
    page.go("/")
    
def main():
    ft.app(target=start)

if __name__ == "__main__":
    ft.run(main)
    