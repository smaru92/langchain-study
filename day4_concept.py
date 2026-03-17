from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 가짜문서
documents = """
회사명: 테크스타트
설립일: 2020년 3월
직원수: 50명
주요서비스: AI 챗봇 솔루션
대표이사: 김철수
위치: 서울 강남구
"""

# 문서 기반 질문 템플릿
prompt = ChatPromptTemplate.from_template("""
아래 문서를 참고해서 질문에 답변해 주세요.
문서에 없는 내용은 "문서에 해당정보가 없습니다."라고 답해주세요.

[문서]
{context}

[질문]
{question}

[답변]
""")

chain = prompt | chat

# 테스트
questions = [
    "회사 이름이 뭐야?",
    "직원이 몇 명이야?",
    "연봉은 얼마야?", # 문서에 없는 정보
]


for question in questions:
    response = chain.invoke({"context": documents, "question": question})
    print(f"Q: {question}")
    print(f"A: {response.content}\n")