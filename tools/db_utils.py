import pymysql
import asyncio

async def fetch_documents_by_date_range(start_date, end_date):
    conn = pymysql.connect(host="localhost", user="root", password="", database="ragdb")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT title, summary FROM federal_register WHERE publication_date BETWEEN %s AND %s", 
        (start_date, end_date)
    )
    results = cursor.fetchall()
    conn.close()
    return results