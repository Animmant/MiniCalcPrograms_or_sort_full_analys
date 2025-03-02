import flet as ft
from ui import UIManager

def main(page: ft.Page):
    UIManager(page)

ft.app(target=main)
