import json
import pymysql

with open("data_pipeline/raw_data.json") as f:
    data = eval(f.read())

conn = pymysql.connect(host="localhost", user="root", password="", database="ragdb")
cursor = conn.cursor()

docs = data["results"]

for doc in docs:
    cursor.execute(
        """
        INSERT INTO federal_register (title, document_number, publication_date, summary)
        VALUES (%s, %s, %s, %s)
        """,
        (
            doc.get("title"),
            doc.get("document_number"),
            doc.get("publication_date"),
            doc.get("summary")
        )
    )

conn.commit()
conn.close()