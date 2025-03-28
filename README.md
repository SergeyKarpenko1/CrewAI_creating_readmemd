![resized_pixel_art_3120x800_recreation](https://github.com/user-attachments/assets/c3b3c64b-1fb8-4d98-b956-f456a312d631)


# ReadmeMD 🚀

![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-0.108.0-orange)
![License](https://img.shields.io/badge/license-MIT-green)

Automated README.md generator powered by AI agents using CrewAI framework.

**[English](#english) | [Русский](#russian)**

<a name="english"></a>

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies and Libraries](#technologies-and-libraries)
- [Project Architecture](#project-architecture)
- [Installation and Running](#installation-and-running)
- [How It Works](#how-it-works)
- [Additional Information](#additional-information)
- [License](#license)

## Introduction

ReadmeMD is a Python application that uses the CrewAI framework to automatically generate comprehensive README.md files for projects. It analyzes project structures, source code, and configuration files to create well-structured documentation.

This tool solves the tedious and often overlooked task of creating detailed documentation for software projects, ensuring consistent and comprehensive README files that follow best practices.

## Features

- 📁 **Recursive project structure scanning** - Automatically analyzes your entire project directory
- 📝 **Intelligent file content analysis** - Extracts relevant information from source code and config files
- 🤖 **Multi-agent AI system** - Uses specialized agents via CrewAI framework for different documentation tasks
- 📊 **Comprehensive README generation** - Creates standardized documentation with all essential sections
- 🌐 **Multilingual support** - Generates documentation in both English and Russian
- ⚙️ **Configurable through YAML files** - Easily customize agents and tasks to your needs

## Technologies and Libraries

### Core Framework and Architecture
- **Python** (>=3.10,<3.13)
- **CrewAI** - Framework for orchestrating AI agents
- **LangChain** - For AI model integration

### AI Models
- Anthropic Claude 3.7 Sonnet (via OpenRouter)
- Google Gemini Flash 1.5 (for testing)

### Dependencies
```
crewai==0.108.0
crewai_tools==0.38.1
langchain_openai==0.3.9
pydantic==2.10.6
python-dotenv==1.0.1
```

## Project Architecture

### Directory Structure
```
readmemd/
├── .gitignore
├── pyproject.toml
├── knowledge/
│   └── user_preference.txt
└── src/
    └── readmemd/
        ├── __init__.py
        ├── crew.py
        ├── main.py
        ├── config/
        │   ├── agents.yaml
        │   └── tasks.yaml
        └── tools/
            ├── __init__.py
            ├── custom_tool.py
            └── test_code.py
```

### Main Components

#### Core Components
- **Readmemd Class** (`crew.py`) - Core class that sets up and orchestrates the CrewAI agents and tasks
- **Main Entry Point** (`main.py`) - Provides CLI interface and execution commands

#### Configuration
- **Agents** (`config/agents.yaml`) - Three specialized agents:
  - Project Information Collector
  - File Content Reader
  - README File Creator
- **Tasks** (`config/tasks.yaml`) - Sequential tasks:
  - Gather project information
  - Read file contents
  - Generate README

#### Tools
- **Custom Tools** (`tools/custom_tool.py`) - Includes `RecursiveDirectoryScanner` for analyzing project structures
- **Testing Utilities** (`tools/test_code.py`) - For testing the system

### Workflow
The system works sequentially:
1. First scanning the project structure
2. Then reading relevant file contents
3. Finally generating a comprehensive README.md based on the collected information

## Installation and Running

### Prerequisites
- Python 3.10 or higher
- Access to OpenRouter or OpenAI API

### Installation Steps

1. Clone the repository
   ```bash
   git clone [<repository-url>](https://github.com/SergeyKarpenko1/CrewAI_creating_readmemd)
   cd readmemd
   ```

2. Install the dependencies
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables in a `.env` file
   ```
   OPENROUTER_API_KEY=your_openrouter_api_key
   # OPENAI_API_KEY=your_openai_api_key  # Alternative
   ```

### Required Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| OPENROUTER_API_KEY | API key for OpenRouter, used to access AI models | Yes |
| OPENAI_API_KEY | Alternative API key for OpenAI | No |

### Running the Application

#### Basic Usage
```bash
readmemd
```
or
```bash
run_crew
```

#### Advanced Options
```bash
# Train the crew for a specific number of iterations
train <iterations> <filename>

# Replay the crew execution from a specific task
replay <task_id>

# Test the crew execution and return results
test <iterations> <openai_model_name>
```

## How It Works

ReadmeMD uses a multi-agent approach powered by the CrewAI framework to generate comprehensive documentation:

1. **Project Information Collector Agent** scans the project structure using the `RecursiveDirectoryScanner` tool, identifying key files and directories.

2. **File Content Reader Agent** analyzes the content of important files to extract:
   - Project purpose and description
   - Dependencies and requirements
   - Installation instructions
   - Usage examples
   - Configuration options

3. **README File Creator Agent** takes all the gathered information and generates a well-structured README.md file with:
   - Clear project description
   - Feature highlights
   - Installation steps
   - Usage instructions
   - Architecture overview
   - License information

The process is configured through YAML files that define the agents' roles, capabilities, and the sequence of tasks they perform.

Example of agent configuration:
```yaml
# Simplified example from agents.yaml
agents:
  - name: Project Information Collector
    role: Project Structure Analyzer
    goal: Gather comprehensive information about the project structure
    backstory: You are an expert in analyzing software projects...
```

## Additional Information

This project was created by Karpenko Sergey, a Data Scientist/AI Engineer based in Moscow, Russia, with interests in AI Agents and NLP.

GitHub: [https://github.com/SergeyKarpenko1](https://github.com/SergeyKarpenko1)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<a name="russian"></a>

# ReadmeMD 🚀

![Python](https://img.shields.io/badge/python-3.10%20%7C%203.11%20%7C%203.12-blue)
![CrewAI](https://img.shields.io/badge/CrewAI-0.108.0-orange)
![License](https://img.shields.io/badge/license-MIT-green)

Автоматический генератор README.md файлов с использованием AI-агентов на основе фреймворка CrewAI.

## Содержание

- [Введение](#введение)
- [Возможности](#возможности)
- [Технологии и библиотеки](#технологии-и-библиотеки)
- [Архитектура проекта](#архитектура-проекта)
- [Установка и запуск](#установка-и-запуск)
- [Как это работает](#как-это-работает)
- [Дополнительная информация](#дополнительная-информация)
- [Лицензия](#лицензия)

## Введение

ReadmeMD — это приложение на Python, использующее фреймворк CrewAI для автоматического создания подробных README.md файлов для проектов. Оно анализирует структуру проекта, исходный код и конфигурационные файлы для создания хорошо структурированной документации.

Этот инструмент автоматизирует утомительную и часто упускаемую из виду задачу создания детальной документации для программных проектов, обеспечивая последовательные и полные README файлы, соответствующие лучшим практикам.

## Возможности

- 📁 **Рекурсивное сканирование структуры проекта** - Автоматически анализирует весь каталог проекта
- 📝 **Интеллектуальный анализ содержимого файлов** - Извлекает релевантную информацию из исходного кода и конфигурационных файлов
- 🤖 **Мультиагентная AI-система** - Использует специализированных агентов через фреймворк CrewAI для различных задач документирования
- 📊 **Комплексная генерация README** - Создает стандартизированную документацию со всеми необходимыми разделами
- 🌐 **Многоязычная поддержка** - Генерирует документацию на английском и русском языках
- ⚙️ **Настраиваемость через YAML-файлы** - Легко настраивайте агентов и задачи под свои нужды

## Технологии и библиотеки

### Основной фреймворк и архитектура
- **Python** (>=3.10,<3.13)
- **CrewAI** - Фреймворк для оркестрации AI-агентов
- **LangChain** - Для интеграции с AI-моделями

### AI-модели
- Anthropic Claude 3.7 Sonnet (через OpenRouter)
- Google Gemini Flash 1.5 (для тестирования)

### Зависимости
```
crewai==0.108.0
crewai_tools==0.38.1
langchain_openai==0.3.9
pydantic==2.10.6
python-dotenv==1.0.1
```

## Архитектура проекта

### Структура директорий
```
readmemd/
├── .gitignore
├── pyproject.toml
├── knowledge/
│   └── user_preference.txt
└── src/
    └── readmemd/
        ├── __init__.py
        ├── crew.py
        ├── main.py
        ├── config/
        │   ├── agents.yaml
        │   └── tasks.yaml
        └── tools/
            ├── __init__.py
            ├── custom_tool.py
            └── test_code.py
```

### Основные компоненты

#### Базовые компоненты
- **Класс Readmemd** (`crew.py`) - Основной класс, который настраивает и оркеструет агентов CrewAI и задачи
- **Точка входа** (`main.py`) - Предоставляет CLI-интерфейс и команды выполнения

#### Конфигурация
- **Агенты** (`config/agents.yaml`) - Три специализированных агента:
  - Сборщик информации о проекте
  - Читатель содержимого файлов
  - Создатель README-файла
- **Задачи** (`config/tasks.yaml`) - Последовательные задачи:
  - Сбор информации о проекте
  - Чтение содержимого файлов
  - Генерация README

#### Инструменты
- **Пользовательские инструменты** (`tools/custom_tool.py`) - Включает `RecursiveDirectoryScanner` для анализа структуры проекта
- **Утилиты тестирования** (`tools/test_code.py`) - Для тестирования системы

### Рабочий процесс
Система работает последовательно:
1. Сначала сканирует структуру проекта
2. Затем читает содержимое релевантных файлов
3. Наконец, генерирует подробный README.md на основе собранной информации

## Установка и запуск

### Предварительные требования
- Python 3.10 или выше
- Доступ к API OpenRouter или OpenAI

### Шаги установки

1. Клонируйте репозиторий
   ```bash
   git clone [<url-репозитория>](https://github.com/SergeyKarpenko1/CrewAI_creating_readmemd)
   cd readmemd
   ```

2. Установите зависимости
   ```bash
   pip install -r requirements.txt
   ```

3. Настройте переменные окружения в файле `.env`
   ```
   OPENROUTER_API_KEY=ваш_ключ_api_openrouter
   # OPENAI_API_KEY=ваш_ключ_api_openai  # Альтернатива
   ```

### Необходимые переменные окружения

| Переменная | Описание | Обязательно |
|------------|----------|-------------|
| OPENROUTER_API_KEY | API-ключ для OpenRouter, используемый для доступа к AI-моделям | Да |
| OPENAI_API_KEY | Альтернативный API-ключ для OpenAI | Нет |

### Запуск приложения

#### Базовое использование
```bash
readmemd
```
или
```bash
run_crew
```

#### Расширенные опции
```bash
# Обучение команды для определенного числа итераций
train <количество_итераций> <имя_файла>

# Повторное выполнение команды с определенной задачи
replay <id_задачи>

# Тестирование выполнения команды и возврат результатов
test <количество_итераций> <имя_модели_openai>
```

## Как это работает

ReadmeMD использует мультиагентный подход на основе фреймворка CrewAI для генерации комплексной документации:

1. **Агент-сборщик информации о проекте** сканирует структуру проекта с помощью инструмента `RecursiveDirectoryScanner`, идентифицируя ключевые файлы и директории.

2. **Агент-читатель содержимого файлов** анализирует содержимое важных файлов для извлечения:
   - Назначения и описания проекта
   - Зависимостей и требований
   - Инструкций по установке
   - Примеров использования
   - Параметров конфигурации

3. **Агент-создатель README-файла** берет всю собранную информацию и генерирует хорошо структурированный файл README.md с:
   - Четким описанием проекта
   - Выделением основных возможностей
   - Шагами установки
   - Инструкциями по использованию
   - Обзором архитектуры
   - Информацией о лицензии

Процесс настраивается через YAML-файлы, которые определяют роли агентов, их возможности и последовательность выполняемых ими задач.

Пример конфигурации агента:
```yaml
# Упрощенный пример из agents.yaml
agents:
  - name: Project Information Collector
    role: Project Structure Analyzer
    goal: Gather comprehensive information about the project structure
    backstory: You are an expert in analyzing software projects...
```

## Дополнительная информация

Этот проект создан Карпенко Сергеем, специалистом по Data Science и инженером по искусственному интеллекту из Москвы, Россия, с интересами в области AI-агентов и NLP.

GitHub: [https://github.com/SergeyKarpenko1](https://github.com/SergeyKarpenko1)

## Лицензия

Этот проект лицензирован по лицензии MIT - см. файл LICENSE для подробностей.
