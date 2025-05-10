from tools.db_utils import fetch_documents_by_date_range

async def get_documents_summary(start_date: str, end_date: str) -> str:
    results = await fetch_documents_by_date_range(start_date, end_date)
    if not results:
        return "No documents found in the given date range."
    return "\n\n".join([f"Title: {r[0]}\nSummary: {r[1]}" for r in results])
