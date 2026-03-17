from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_openai import ChatOpenAI

# 1. 문서 준비
documents = [
    "테크스타트는 2020년에 설립도니 AI 전문 스타트업입니다.",
    "서울 강남구에 본사를 두고 있습니다.",
    "현재 50명의 직원이 근무하고 있습니다",
    "핵심 서비스는 AI 챗봇 솔루션입니다",
    "Python, FastaPAI, LangChain을 주로 사용합니다.",
    "현재 백엔드 개발자를 채용 중입니다.",
    "경력 3년이상, Python 필수 입니다.",
    "연봉은 5000~7000만원 입니다.",
    "복리후생으로 점심 식대, 간식, 자기개발비를 지원합니다.",
    "재택근무는 주 2회 가능합니다.",
]


# 2. 벡터 Db생성

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
vectordb = Chroma.from_texts(texts=documents, embedding=embeddings)

print("벡터 DB 생성 완료!")

# 검색 테스트
query = "채용 조건이 뭐야?"
results = vectordb.similarity_search(query=query, k=3)

print(f"\n검색어: {query}")
print("검색결과:")
for i, doc in enumerate(results):
    print(f"{i+1}. {doc.page_content}")