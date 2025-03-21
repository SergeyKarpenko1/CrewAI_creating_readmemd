import os
import json
from datetime import datetime
from typing import Type
from pydantic import BaseModel, Field
from crewai.tools import BaseTool

# Исключаемые директории
EXCLUDED_DIRS = {'.venv', 'venv', '.env', '__pycache__', '.git', 'node_modules', '.idea'}

class ScanDirectoryInput(BaseModel):
    """Input schema for RecursiveDirectoryScanner."""
    directory: str = Field(..., description="Absolute path to the directory to scan.")

class RecursiveDirectoryScanner(BaseTool):
    name: str = "Recursive Directory Scanner"
    description: str = (
        "Recursively scans the provided directory (excluding system/venv folders) and returns a JSON list "
        "of all files with relative and absolute paths, sizes, and modification times."
    )
    args_schema: Type[BaseModel] = ScanDirectoryInput

    def _run(self, directory: str) -> str:
        directory = directory.rstrip('/')
        if not os.path.exists(directory):
            return f"Error: Directory does not exist at {directory}"

        file_structure = []

        for root, dirs, files in os.walk(directory):
            dirs[:] = [d for d in dirs if d not in EXCLUDED_DIRS]

            for file in files:
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, directory)
                try:
                    file_info = {
                        "path": rel_path,
                        "absolute_path": full_path,
                        "size": os.path.getsize(full_path),
                        "modified": datetime.fromtimestamp(os.path.getmtime(full_path)).isoformat(),
                        "type": "file"
                    }
                except Exception as e:
                    file_info = {
                        "path": rel_path,
                        "absolute_path": full_path,
                        "error": str(e)
                    }
                file_structure.append(file_info)

        return json.dumps(file_structure, indent=2)