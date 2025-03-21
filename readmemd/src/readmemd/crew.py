import os
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import FileReadTool
from langchain_openai import ChatOpenAI
from tools.custom_tool import RecursiveDirectoryScanner

from dotenv import load_dotenv

# ✅ Загрузка переменных окружения
load_dotenv()

import warnings
warnings.filterwarnings('ignore')

# scan_tool = RecursiveDirectoryScanner(directory='project_directory')
# file_tool = FileReadTool()

@CrewBase
class Readmemd():
    """Readmemd crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    def __init__(self, project_directory="project_directory"):
        self.project_directory = project_directory

        self.llm = ChatOpenAI(
            model="openrouter/anthropic/claude-3.7-sonnet",
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=os.getenv("OPENROUTER_API_KEY"),

        # self.llm = litellm.LLM(
        #     model="google/gemini-flash-1.5",  # Убираем "openrouter/" в названии модели
        #     api_base="https://openrouter.ai/api/v1",
        #     api_key=os.getenv("OPENROUTER_API_KEY"),
        )
        

            
    @agent
    def project_info_gatherer(self) -> Agent:
        return Agent(
            config=self.agents_config['project_info_gatherer'],
            tools=[RecursiveDirectoryScanner()],
            llm=self.llm
        )

    @agent
    def file_content_reader(self) -> Agent:
        return Agent(
            config=self.agents_config['file_content_reader'],
            tools=[FileReadTool()],
            llm=self.llm
        )

    @agent
    def readme_generator(self) -> Agent:
        return Agent(
            config=self.agents_config['readme_generator'],
            llm=self.llm
        )


    @task
    def gather_project_info_task(self) -> Task:
        return Task(
            config=self.tasks_config['gather_project_info_task'],
            tools=[RecursiveDirectoryScanner()],
            output_file="outputs/gather_project_info_task.md"
        )

    @task
    def read_file_contents_task(self) -> Task:
        return Task(
            config=self.tasks_config['read_file_contents_task'],
            tools=[FileReadTool()],
            output_file="outputs/read_file_contents_task.md"
        )

    @task
    def generate_readme_task(self) -> Task:
        return Task(
            config=self.tasks_config['generate_readme_task'],
            output_file="outputs/README.md"
        )


    @crew
    def crew(self) -> Crew:
        """Creates the Readme crew"""
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            planning=True,
            planning_llm=self.llm

        )
    def run(self):
        """Запуск CrewAI"""
        print(f"Запуск CrewAI для директории: {self.project_directory}")
        self.crew().kickoff(inputs={"project_directory": self.project_directory})

# Запуск с аргументом директории
if __name__ == "__main__":
    project_dir = "/Users/sergey/Desktop/CrewAI/Сreating_readmeMD"  # Укажите путь к вашему проекту
    readme_crew = Readmemd(project_directory=project_dir)
    readme_crew.run()
    
