import sys
import logging
import os
from pathlib import Path

# добавляем корневую папку проекта в sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

# перенаправляем логи в stdout
logging.basicConfig(stream=sys.stdout)

# импортируем приложение Flask
from app import app

# создаем экземпляр приложения
application = app
