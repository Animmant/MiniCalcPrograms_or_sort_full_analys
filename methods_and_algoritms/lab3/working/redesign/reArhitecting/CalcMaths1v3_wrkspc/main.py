# -*- coding: utf-8 -*-
"""
Головний файл проєкту CalcMaths.

Цей файл є точкою входу в програму та ініціалізує інтерфейс користувача.
"""

import flet as ft
from ui import UIManager

def main(page: ft.Page):
    """
    Головна функція, яка ініціалізує UI та передає керування UIManager.
    
    Args:
        page (ft.Page): Об'єкт сторінки Flet
    """
    UIManager(page)

# Запуск додатку з функцією main як точкою входу
if __name__ == "__main__":
    ft.app(target=main) 