# Project Information

## Project Structure

```
/Users/sergey/Desktop/CrewAI/Сreating_readmeMD/
├── .env
├── requirements.txt
└── readmemd/
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

## Project Overview

This project appears to be a Python application called "readmemd" that uses the CrewAI framework to automatically generate README.md files for projects. The project is organized as a proper Python package with a defined structure.

## Key Files and Their Purpose

### Configuration Files
- **pyproject.toml**: Package configuration file for the Python project (509 bytes)
- **.env**: Environment variables configuration (278 bytes)
- **requirements.txt**: Lists project dependencies (99 bytes)
- **.gitignore**: Specifies files to ignore in git repository (28 bytes)

### Source Code
- **main.py**: Entry point for the application (1741 bytes)
- **crew.py**: Contains CrewAI implementation for the README generation (3082 bytes)
- **tools/custom_tool.py**: Custom tools implementation for the CrewAI framework (2032 bytes)
- **tools/test_code.py**: Testing utilities for the code (919 bytes)

### Configuration
- **config/agents.yaml**: Configuration for the AI agents (4739 bytes)
- **config/tasks.yaml**: Defines tasks for the AI agents to perform (3653 bytes)
- **knowledge/user_preference.txt**: User preferences for README generation (179 bytes)

## Technologies and Dependencies

Based on the file structure and names, this project appears to use:
- **Python**: The main programming language
- **CrewAI**: A framework for orchestrating AI agents
- **YAML**: For configuration files
- **Environment Variables**: For configuration through .env file

## Installation and Setup

The project follows a standard Python package structure with:
- A `pyproject.toml` file for package configuration
- A `requirements.txt` file for dependencies
- A proper `src` layout suggesting it can be installed via pip

## Project Purpose

This appears to be a tool that uses AI agents (via CrewAI) to automatically generate README.md files for projects. The agents are configured in YAML files, and the system likely analyzes project structures to create appropriate documentation.

## Features

Based on the file structure and sizes:
1. Uses multiple AI agents working together (defined in agents.yaml)
2. Has a defined workflow of tasks (in tasks.yaml)
3. Implements custom tools for the agents to use
4. Takes into account user preferences for README generation
5. Organized as a proper Python package that can be distributed

This information provides a comprehensive overview of the project structure and purpose, which can be used to generate a detailed README.md file.