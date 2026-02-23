from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

chat = ChatOpenAI(model="gpt-3.5-turbo")

# 기본 templete
template = """
너는 {role}이야
사용자 질문: {question}
답변:
"""

promt = PromptTemplate(
    input_variables=["role", "question"],
    template=template,
)

# 템플릿 사용해서 프롬프트 생성
formatted = promt.format(
    role="Python관련해서 잘 모르는 요리사",
    question="FastAPI가 뭐지? Flask와 비교해서 설명해줘"
)

print("=== 생성된 프롬프트 ===")
print(formatted)
print()

# AI에게 전달
response = chat.invoke(formatted)
print("=== AI 답변 ===")
print(response.content)