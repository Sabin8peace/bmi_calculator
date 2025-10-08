"""

Now we have our vector database from pdf

now we will use groq to do qna in this

now we will use UI using streamlist
where user can enter question and get answer from rag agent
learn streamlist for that


"""
from groq import Groq
from dotenv import load_dotenv
import os
from pinecone import Pinecone
import streamlit as st
from create_vectors import embed_text, vector_index

load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
groq_client = Groq(api_key=GROQ_API_KEY)


st.title("this is title hai")
st.subheader("this is  sub title hai")
user_query = st.text_input("Enter Question")
submit_btn = st.button("Submit")


if submit_btn and user_query:
    vector = embed_text(user_query)
    query_response = vector_index.query(
        vector=vector,
        top_k=1,
        include_metadata=True
    )

    similar_documents = ""
    for match in query_response["matches"]:
        similar_documents += match["metadata"]["text"]+"\n\n"

    print("Similar doc found: ", similar_documents)

    system_prompt = {
        "role": "system",
        "content": f"""you are a helpful assistant that helps to answer question asked by user , answer on the basis of document provided
        use the following context to answer the question
        context:{similar_documents}
        for General questions not related to document, politely inform them that you dont know the answer """

    }
    user_prompt = {
        "role": "user",
        "content": user_query
    }
    llm_response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[system_prompt, user_prompt],
        max_tokens=1024,
        temperature=0.2,
    )
    llm_answer = llm_response.choices[0].message.content
    st.write("Answer: ")
    st.write(llm_answer)
