import random

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

#.env 파일 불러오기
load_dotenv()

model = "gpt-3.5-turbo"
# 여러 질문 테스트
questions = [
    "Python이 뭐야? 한 줄로 설명해줘",
    "FastAPI 장점 3가지 알려줘",
    "LangChain과 LangGraph가 뭐야?",
    "백엔드 개발자가 뭐하는 사람이야?",
    "RAG가 뭐야?",
]

for q in questions:
    # ChatOpenAI 모델 생성
    temperature = random.random()
    chat = ChatOpenAI(
        model=model,
        temperature=temperature
    )

    print(f"\n질문(온도{temperature}): {q}")
    response = chat.invoke(q)
    print(f"답변: {response.content}")
    print("-" * 50)