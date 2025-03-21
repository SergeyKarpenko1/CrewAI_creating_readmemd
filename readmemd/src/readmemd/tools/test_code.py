from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# ✅ Загрузка переменных окружения
load_dotenv()

class LLMTester:
    def __init__(self):
        self.llm = ChatOpenAI(
            model="google/gemini-flash-1.5",
            openai_api_base="https://openrouter.ai/api/v1",
            openai_api_key=os.getenv("OPENROUTER_API_KEY")
        )

    def test_model(self, prompt: str):
        """Отправляет запрос в LLM и возвращает ответ."""
        try:
            response = self.llm.invoke(prompt)
            return response
        except Exception as e:
            return f"Ошибка: {e}"

if __name__ == "__main__":
    tester = LLMTester()
    prompt = "Расскажи анекдот про программистов."
    response = tester.test_model(prompt)
    print("Ответ модели:", response)