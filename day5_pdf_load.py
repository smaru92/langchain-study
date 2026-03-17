from langchain_community.document_loaders import PyPDFLoader

# PDF 로드
loader = PyPDFLoader("company_info.pdf")
pages = loader.load()

print(f"총 {len(pages)} 페이지\n")

# 내용 확인
for i, page in enumerate(pages):
    print(f"=== 페이지 {i+1} ===")
    print(page.page_content[:500])  # 앞 500자만
    print()