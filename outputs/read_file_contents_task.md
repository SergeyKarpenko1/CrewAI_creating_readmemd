# Project Information: README.md Generator

## Project Overview
This project is a README.md generator tool built using the CrewAI framework. It's designed to automatically analyze project directories and generate comprehensive README.md files by leveraging AI agents to extract relevant information from project files.

## Project Structure
```
/Users/sergey/Desktop/CrewAI/Сreating_readmeMD/
├── .env                         # Environment variables configuration
├── requirements.txt             # Project dependencies
├── readmemd/                    # Main project package
│   ├── .gitignore               # Git ignore file
│   ├── pyproject.toml           # Python project configuration
│   ├── knowledge/               # Knowledge base directory
│   │   └── user_preference.txt  # User preferences for README generation
│   └── src/                     # Source code directory
│       └── readmemd/            # Main package
│           ├── __init__.py      # Package initialization
│           ├── crew.py          # CrewAI implementation (main logic)
│           ├── main.py          # Application entry point
│           ├── config/          # Configuration directory
│           │   ├── agents.yaml  # Agent configurations
│           │   └── tasks.yaml   # Task definitions
│           └── tools/           # Custom tools directory
│               ├── __init__.py  # Package initialization
│               ├── custom_tool.py # Custom tools implementation
│               └── test_code.py # Testing utilities
```

## Project Purpose
This project automates the creation of README.md documentation for software projects. It:
1. Scans a project directory to collect information about files and structure
2. Reads and analyzes file contents to extract key information
3. Generates a comprehensive README.md file with proper formatting and sections

The system uses AI agents (via CrewAI) to perform specific tasks in a workflow to achieve the README generation goal.

## Technologies and Dependencies
- **Python** (>=3.10, <3.13)
- **CrewAI** (v0.108.0) - Framework for creating AI agent workflows
- **CrewAI Tools** (v0.38.1) - Tools for CrewAI agents
- **Langchain OpenAI** (v0.3.9) - LLM integration
- **Pydantic** (v2.10.6) - Data validation
- **Python-dotenv** (v1.0.1) - Environment variable management
- **OpenRouter API** - For accessing AI models (Claude-3.7-Sonnet and Gemini Flash 1.5)

## Project Architecture

### Agents
The project uses three AI agents, each with a specific role:

1. **Project Information Collector (project_info_gatherer)**
   - Scans project directories and extracts metadata
   - Identifies technologies, directory layout, and auxiliary files
   - Uses the RecursiveDirectoryScanner tool

2. **File Content Reader (file_content_reader)**
   - Reads and analyzes file contents
   - Extracts key information for README sections
   - Uses the FileReadTool

3. **README File Creator (readme_generator)**
   - Generates the final README.md file
   - Organizes content according to best practices
   - Ensures comprehensive documentation

### Tasks
The workflow consists of three sequential tasks:

1. **gather_project_info_task**
   - Uses RecursiveDirectoryScanner to analyze project structure
   - Outputs project_info.json with file listings

2. **read_file_contents_task**
   - Reads contents of files identified in project_info.json
   - Extracts information about installation, usage, API, etc.
   - Outputs readme_data.json with structured information

3. **generate_readme_task**
   - Uses the data from readme_data.json to create a README.md
   - Follows a structured format with standard sections
   - Outputs the final README.md file

### Tools
1. **RecursiveDirectoryScanner**
   - Custom tool that scans directories recursively
   - Excludes system directories like .venv, __pycache__, etc.
   - Returns JSON with file paths, sizes, and modification times

2. **FileReadTool**
   - Provided by CrewAI tools
   - Reads file contents for analysis

## Installation and Setup

### Prerequisites
- Python 3.10-3.12
- OpenRouter API key

### Installation Steps
1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your API keys:
   ```
   OPENROUTER_API_KEY='your-api-key'
   ```

## Usage

### Running the Application
The main entry point is through the `main.py` file, which provides several commands:

```python
# Run the default README generation
python -m readmemd.main

# Train the crew for a specific number of iterations
python -m readmemd.main train [iterations] [filename]

# Replay a specific task
python -m readmemd.main replay [task_id]

# Test the crew with specific parameters
python -m readmemd.main test [iterations] [model_name]
```

You can also run the application by importing and using the Readmemd class:

```python
from readmemd.crew import Readmemd

project_dir = "/path/to/your/project"
readme_crew = Readmemd(project_directory=project_dir)
readme_crew.run()
```

### Customization
The project can be customized through:
- Configuration files in the `config/` directory
- User preferences in `knowledge/user_preference.txt`
- Environment variables in the `.env` file

## Configuration

### pyproject.toml
The project uses a standard Python project configuration:
- Package name: readmemd
- Version: 0.1.0
- Description: "readmeMD using crewAI"
- Default LLM: gpt-4-turbo

### Environment Variables
Required environment variables:
- `OPENROUTER_API_KEY`: API key for accessing AI models via OpenRouter

## User Preferences
The system can use user information stored in `user_preference.txt`:
- User name: Karpenko Sergey
- Profession: Data Scientist/AI Engineer
- Interests: AI Agents/NLP
- Location: Moscow, Russia
- GitHub: https://github.com/SergeyKarpenko1

## License
The project does not explicitly specify a license in the provided files.