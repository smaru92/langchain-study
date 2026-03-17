from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

# 1. 문서 준비
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


# 2. 벡터 Db생성

embeddings = HuggingFaceEmbeddings(
    model_name="jhgan/ko-sroberta-multitask"
)
vectordb = Chroma.from_texts(texts=documents, embedding=embeddings)

# 3. LLM 준비
chat = ChatOpenAI(model="gpt-3.5-turbo")

# 4. RAG 프롬프트
prompt = ChatPromptTemplate.from_template("""
아래 문서를 참고해서 질문에 답변해주세요.
문서에 없는 내용은 "문서에 해당정보가 없습니다" 라고 답해주세요.

[참고문서]
{context}

[질문]
{question}

[답변]
""")

# 5. RAG 함수
def ask_rag(question):
    # 관련 문서 검색
    docs = vectordb.similarity_search(question, k=3)
    context = "\n".join([doc.page_content for doc in docs])

    # LLM에게 질문
    chain = prompt | chat
    response = chain.invoke({"context": context, "question": question})

    return response.content

# 6. 테스트
questions = [
    "회사가 언제 설립됐지?",
    "채용 조건이 뭐야?",
    "복리후생이 뭐 있어?",
    "재택근무가 가능해?",
    "회사 주가가 얼마야?",
]

for question in questions:
    print(f"Q:{question}")
    print(f"A:{ask_rag(question)}")
    print("-" * 50)

