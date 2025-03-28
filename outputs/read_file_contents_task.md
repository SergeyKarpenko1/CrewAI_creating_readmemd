{
  "project_purpose": {
    "description": "ReadmeMD is a Python application that uses the CrewAI framework to automatically generate comprehensive README.md files for projects. It analyzes project structures, source code, and configuration files to create well-structured documentation.",
    "problem_solved": "Automates the tedious and often overlooked task of creating detailed documentation for software projects, ensuring consistent and comprehensive README files.",
    "source_files": ["main.py", "crew.py", "pyproject.toml"]
  },
  "installation_and_startup": {
    "dependencies": [
      "crewai==0.108.0",
      "crewai_tools==0.38.1",
      "langchain_openai==0.3.9",
      "pydantic==2.10.6",
      "python-dotenv==1.0.1"
    ],
    "installation_steps": [
      "1. Clone the repository",
      "2. Install the dependencies: `pip install -r requirements.txt`",
      "3. Set up the environment variables in a `.env` file (see Environment Variables section)"
    ],
    "environment_variables": [
      {
        "name": "OPENROUTER_API_KEY",
        "description": "API key for OpenRouter, used to access AI models",
        "required": true
      },
      {
        "name": "OPENAI_API_KEY",
        "description": "Alternative API key for OpenAI (commented out in the example)",
        "required": false
      }
    ],
    "run_commands": [
      "readmemd: Run the README generation tool",
      "run_crew: Alternative command to run the README generation",
      "train: Train the crew for a given number of iterations",
      "replay: Replay the crew execution from a specific task",
      "test: Test the crew execution and returns the results"
    ],
    "source_files": ["requirements.txt", ".env", "pyproject.toml", "main.py"]
  },
  "project_architecture": {
    "main_components": [
      {
        "name": "Readmemd Class",
        "file": "crew.py",
        "description": "Core class that sets up and orchestrates the CrewAI agents and tasks"
      },
      {
        "name": "Agents",
        "file": "config/agents.yaml",
        "description": "Three specialized agents: Project Information Collector, File Content Reader, and README File Creator"
      },
      {
        "name": "Tasks",
        "file": "config/tasks.yaml",
        "description": "Sequential tasks: gather project info, read file contents, and generate README"
      },
      {
        "name": "Custom Tools",
        "file": "tools/custom_tool.py",
        "description": "RecursiveDirectoryScanner tool to analyze project structure"
      }
    ],
    "workflow": "The system works sequentially: first scanning the project structure, then reading relevant file contents, and finally generating a comprehensive README.md based on the collected information.",
    "source_files": ["crew.py", "config/agents.yaml", "config/tasks.yaml", "tools/custom_tool.py"]
  },
  "usage": {
    "basic_usage": "Run the tool by executing `readmemd` or `run_crew` command after installation.",
    "advanced_options": [
      "Training: `train <iterations> <filename>`",
      "Replaying: `replay <task_id>`",
      "Testing: `test <iterations> <openai_model_name>`"
    ],
    "example_inputs": {
      "topic": "AI LLMs",
      "current_year": "Automatically set to the current year"
    },
    "source_files": ["main.py", "crew.py"]
  },
  "features": {
    "main_features": [
      "Recursive project structure scanning",
      "Intelligent file content analysis",
      "Multi-agent AI system using CrewAI framework",
      "Comprehensive README generation with standard sections",
      "Support for both English and Russian documentation",
      "Configurable through YAML files"
    ],
    "source_files": ["crew.py", "config/tasks.yaml"]
  },
  "technologies": {
    "framework": "CrewAI",
    "language": "Python (>=3.10,<3.13)",
    "ai_models": ["Anthropic Claude 3.7 Sonnet (via OpenRouter)", "Google Gemini Flash 1.5 (for testing)"],
    "key_libraries": ["langchain_openai", "pydantic", "python-dotenv"],
    "source_files": ["requirements.txt", "crew.py", "tools/test_code.py"]
  },
  "license": {
    "type": "Not explicitly specified in the provided files",
    "recommendation": "Consider adding a LICENSE file to the project"
  },
  "user_info": {
    "name": "Karpenko Sergey",
    "role": "Data Scientist/AI Engineer",
    "interests": "AI Agents/NLP",
    "location": "Moscow, Russia",
    "github": "https://github.com/SergeyKarpenko1",
    "source_file": "knowledge/user_preference.txt"
  }
}