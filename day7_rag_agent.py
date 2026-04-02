from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.tools import DuckDuckGoSearchRun
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

load_dotenv()

# 1. 회사 문서 준비
documents = [
    "테크스타트는 2020년에 설립된 AI 전문 스타트업입니다.",
    "서울 강남구에 본사를 두고 있습니다.",
    "현재 50명의 직원이 근무하고 있습니다.",
    "핵심 서비스는 AI 챗봇 솔루션입니다.",
    "Python, FastAPI, LangChain을 주로 사용합니다.",
    "현재 백엔드 개발자를 채용 중입니다.",
    "경력 3년 이상, Python 필수입니다.",
    "연봉은 5000만원~7000만원입니다.",
    "복리후생으로 점심 식대, 간식, 자기개발비를 지원합니다.",
    "재택근무는 주 2회 가능합니다.",
]

# 2. 벡터 DB 생성
print("벡터 DB 생성 중...")
embeddings = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask"
)
vectordb = Chroma.from_texts(texts=documents, embedding=embeddings)
print("벡터 DB 준비 완료!\n")


# 3. RAG 도구 정의
@tool(description="회사 내부 문서에서 정보를 검색합니다. 회사 정보, 채용, 복리후생 등 내부 정보 질문에 사용하세요.")
def search_company_docs(query: str) -> str:
    docs = vectordb.similarity_search(query, k=3)
    if not docs:
        return "관련 문서를 찾을 수 없습니다."
    return "\n".join([doc.page_content for doc in docs])


# 4. 웹 검색 도구
search = DuckDuckGoSearchRun()


@tool(description="인터넷에서 최신 정보를 검색합니다. 뉴스, 날씨, 일반 지식 등 외부 정보 질문에 사용하세요.")
def search_web(query: str) -> str:
    return search.run(query)


# 5. 계산 도구
@tool(description="수학 계산을 수행합니다.")
def calculate(expression: str) -> str:
    import numexpr

    try:
        result = numexpr.evaluate(expression)
        return str(result)
    except (SyntaxError, TypeError, KeyError) as e:
        return f"계산할 수 없습니다: {e}"


# 6. LLM + Agent 생성
llm = ChatOpenAI(model="gpt-3.5-turbo")
tools = [search_company_docs, search_web, calculate]

agent = create_react_agent(
    model=llm,
    tools=tools,
)

# 7. 대화형 실행
print("=" * 50)
print("RAG + Agent 시스템 준비 완료!")
print("질문을 입력하세요. (종료: q)")
print("=" * 50 + "\n")

while True:
    question = input("질문: ")
    if question.lower() == 'q':
        print("종료합니다.")
        break

    result = agent.invoke({"messages": [("human", question)]})
    answer = result["messages"][-1].content
    print(f"답변: {answer}\n")