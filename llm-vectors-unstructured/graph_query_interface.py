import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from neo4j import GraphDatabase

llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_neo4j_driver():
    driver = GraphDatabase.driver(
        os.getenv('NEO4J_URI'),
        auth=(
            os.getenv('NEO4J_USERNAME'),
            os.getenv('NEO4J_PASSWORD')
        )
    )

    driver.verify_connectivity()
    return driver

"""
criar semantic/dynamic search interface para seguintes queries:

MATCH (t:Topic{name:"semantic search"})<-[:MENTIONS]-(p:Paragraph)<-[:CONTAINS]-(l:Lesson)
RETURN DISTINCT l.name, l.url

MATCH (t:Topic)<-[:MENTIONS]-(p:Paragraph)<-[:CONTAINS]-(l:Lesson)
RETURN t.name, COUNT(DISTINCT l) as lessons
ORDER BY lessons DESC
"""