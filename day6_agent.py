from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

# 1. 도구 정의
@tool(description="두 숫자를 더합니다")
def add(a: int, b: int) -> int:
    return a + b

@tool(description="두 숫자를 곱합니다")
def multiply(a: int, b: int) -> int:
    return a * b


# 2. LLM 준비
llm = ChatOpenAI(model="gpt-3.5-turbo")


# 3. Agent 생성
tools = [add, multiply]
agent = create_react_agent(llm, tools)

# 4. 실행
print("=== Agent 테스트 ===\n")

questions = [
    "3 + 5는 뭐야?",
    "7 곱하기 8은?",
    "12 더하기 3 하고, 그 결과에 4를 곱해줘",
    "오늘날씨는?",
    "파이썬이뭐야??",
]

for q in questions:
    print(f"질문: {q}")
    result = agent.invoke({"messages": [("human", q)]})
    answer = result["messages"][-1].content
    print(f"답변: {answer}\n")