
![image](https://github.com/user-attachments/assets/fa937135-1a2d-4717-afc5-03f46a244499)

# Генератор README.md с использованием CrewAI
( Этот README.md создан при помощи этого агента)

## Введение

Данный проект представляет собой инструмент для автоматического создания файлов README.md для программных проектов. Используя фреймворк CrewAI и технологии искусственного интеллекта, инструмент анализирует структуру проекта, содержимое файлов и генерирует подробную документацию в формате Markdown. Это позволяет разработчикам сэкономить время на создании качественной документации, одновременно обеспечивая полноту и структурированность информации о проекте.

## Возможности

- **Автоматический анализ структуры проекта** — рекурсивное сканирование директорий и файлов
- **Извлечение ключевой информации** — определение технологий, зависимостей и архитектуры проекта
- **Интеллектуальная генерация содержимого** — создание согласованного и информативного README.md
- **Настраиваемые шаблоны** — возможность адаптации под предпочтения пользователя
- **Поддержка различных форматов проектов** — работа с Python, JavaScript и другими типами проектов
- **Многоагентная архитектура** — использование специализированных AI-агентов для различных задач

## Технологии и библиотеки

### Основные компоненты и архитектура
- **Python** (>=3.10, <3.13) — основной язык программирования
- **CrewAI** (v0.108.0) — фреймворк для создания рабочих процессов с AI-агентами
- **YAML** — формат для конфигурации агентов и задач
- **JSON** — для хранения и передачи структурированных данных
- **Markdown** — формат итогового README-файла

### Используемые библиотеки
- **CrewAI Tools** (v0.38.1) — инструменты для агентов CrewAI
- **Langchain OpenAI** (v0.3.9) — интеграция с языковыми моделями
- **Pydantic** (v2.10.6) — валидация данных
- **Python-dotenv** (v1.0.1) — управление переменными окружения
- **OpenRouter API** — для доступа к AI-моделям (Claude-3.7-Sonnet и Gemini Flash 1.5)

## Архитектура проекта

Проект организован как Python-пакет `readmemd` со следующей структурой:

```
/readmemd/
├── .gitignore               # Файл игнорирования Git
├── pyproject.toml           # Конфигурация Python-проекта
├── knowledge/               # Директория базы знаний
│   └── user_preference.txt  # Пользовательские предпочтения
└── src/                     # Исходный код
    └── readmemd/            # Основной пакет
        ├── __init__.py      # Инициализация пакета
        ├── crew.py          # Реализация CrewAI (основная логика)
        ├── main.py          # Точка входа в приложение
        ├── config/          # Директория конфигурации
        │   ├── agents.yaml  # Конфигурации агентов
        │   └── tasks.yaml   # Определения задач
        └── tools/           # Директория пользовательских инструментов
            ├── __init__.py  # Инициализация пакета
            ├── custom_tool.py # Реализация пользовательских инструментов
            └── test_code.py # Утилиты тестирования
```

### Ключевые компоненты

1. **Агенты (agents.yaml)**
   - **Project Information Collector** — собирает метаданные проекта, сканирует директории
   - **File Content Reader** — читает и анализирует содержимое файлов
   - **README File Creator** — генерирует итоговый файл README.md

2. **Задачи (tasks.yaml)**
   - **gather_project_info_task** — анализ структуры проекта
   - **read_file_contents_task** — чтение содержимого файлов
   - **generate_readme_task** — создание README.md

3. **Инструменты (tools)**
   - **RecursiveDirectoryScanner** — рекурсивное сканирование директорий
   - **FileReadTool** — чтение содержимого файлов

4. **Основные файлы**
   - **crew.py** — основная логика работы CrewAI
   - **main.py** — точка входа приложения

## Установка и запуск

### Предварительные требования
- Python 3.10-3.12
- Ключ API OpenRouter

### Шаги установки
1. Клонируйте репозиторий:
   ```bash
   git clone <url-репозитория>
   cd Сreating_readmeMD
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` с вашими API-ключами:
   ```
   OPENROUTER_API_KEY='ваш-api-ключ'
   ```

### Запуск приложения
Основная точка входа — файл `main.py`, который предоставляет несколько команд:

```bash
# Запуск генерации README по умолчанию
python -m readmemd.main

# Обучение экипажа для определенного числа итераций
python -m readmemd.main train [iterations] [filename]

# Повторное выполнение конкретной задачи
python -m readmemd.main replay [task_id]

# Тестирование экипажа с определенными параметрами
python -m readmemd.main test [iterations] [model_name]
```

Вы также можете запустить приложение, импортируя и используя класс Readmemd:

```python
from readmemd.crew import Readmemd

project_dir = "/путь/к/вашему/проекту"
readme_crew = Readmemd(project_directory=project_dir)
readme_crew.run()
```

### Переменные окружения
Обязательные переменные окружения:
- `OPENROUTER_API_KEY`: API-ключ для доступа к моделям AI через OpenRouter

## Как это работает

Процесс генерации README.md происходит в три основных этапа:

1. **Сбор информации о проекте**
   - Агент Project Information Collector использует инструмент RecursiveDirectoryScanner для анализа структуры проекта
   - Сканер исключает системные директории (.venv, __pycache__ и т.д.)
   - Результаты сохраняются в файл project_info.json с путями к файлам, размерами и временем модификации

2. **Анализ содержимого файлов**
   - Агент File Content Reader использует FileReadTool для чтения содержимого файлов, идентифицированных на предыдущем этапе
   - Извлекается информация об установке, использовании, API и т.д.
   - Результаты структурируются и сохраняются в readme_data.json

3. **Генерация README**
   - Агент README File Creator использует данные из readme_data.json для создания README.md
   - Следует структурированному формату со стандартными разделами
   - Генерирует итоговый файл README.md

Пример потока данных:

```
Исходный проект -> RecursiveDirectoryScanner -> project_info.json -> 
FileReadTool -> readme_data.json -> README Generator -> README.md
```

Агенты используют модели AI (Claude-3.7-Sonnet и Gemini Flash 1.5) через OpenRouter API для анализа и генерации содержимого.

## Дополнительная информация

### Настройка и кастомизация
Проект можно настроить через:
- Конфигурационные файлы в директории `config/`
- Пользовательские предпочтения в `knowledge/user_preference.txt`
- Переменные окружения в файле `.env`

### Пользовательские предпочтения
Система может использовать информацию о пользователе, хранящуюся в `user_preference.txt`:
- Имя пользователя: Карпенко Сергей
- Профессия: Специалист по данным/AI инженер
- Интересы: AI Агенты/NLP
- Местоположение: Москва, Россия
- GitHub: https://github.com/SergeyKarpenko1

### Конфигурация проекта
Проект использует стандартную конфигурацию Python-проекта:
- Имя пакета: readmemd
- Версия: 0.1.0
- Описание: "readmeMD using crewAI"
- LLM по умолчанию: gpt-4-turbo

## Лицензия

Проект распространяется под лицензией MIT.

```
MIT License

Copyright (c) 2023 Карпенко Сергей

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
