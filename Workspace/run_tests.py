import os
import sys
import pytest

# Додаємо каталог src до PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

# Запускаємо тести
if __name__ == "__main__":
    # Можна додати параметри за потребою
    sys.exit(pytest.main(['-v', 'src/tests'])) 