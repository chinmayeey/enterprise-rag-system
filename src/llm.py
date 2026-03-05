from openai import OpenAI
import os

def generate_answer(context, query):
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    prompt = f"""
    Use the following context to answer the question clearly and professionally.

    Context:
    {context}

    Question:
    {query}

    Answer:
    """
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    
    return response.choices[0].message.content