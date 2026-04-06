import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["KEY"])

st.header("Email Generator")

with st.container(border=True):
    col1, col2 = st.columns(2)
    with col1:
        user = st.text_input("Insert the name of the sender.")
        recip = st.text_input("Insert the name of the recipient.")
    with col2:
        person = st.radio("Writing Style", ["Agressive", "Calm", "Mysterious", "Chaotic", "Formal", "Childish"])
    content = st.text_area("What is the content of your email?")
    custom = st.checkbox("Make a custom request")
    if custom == True:
        request = st.text_input("What is your request?")
    gen = st.button("Generate Email")

    if gen == True:
        if user == "" or recip == "" or person == "" or content == "":
            st.error("Please enter all required fields.")
        elif custom == True:
            if request == "":
                st.error("Please enter all required fields.")
        else:
            user_prompt = ""
            if custom == False:
                user_prompt = f"You are an email genarator who helps users generate emails based on their needs and preferences. While writing each email, be sure to write about the wanted content, which is {content}. Include the recipient, who is {recip}, and the sender, who is {user}. Write the email in this writing style: {person}."
            elif custom == True:
                user_prompt = f"You are an email genarator who helps users generate emails based on their needs and preferences. While writing each email, be sure to write about the wanted content, which is {content}. Include the recipient, who is {recip}, and the sender, who is {user}. Write the email in this writing style: {person}. Write the email also according to this request: {request}."

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "user", "content": user_prompt}
                ]
            )
            # 5
            st.write(response.choices[0].message.content)

# My code will generate any email based on the fields entered by the use. These fields are the sender's name, the recipient's name, what the email is about, what tone the user wants the email to be written in, and to make a custom request. The user input can be as long as they want it to be, as long as it is not empty or makes sense under the requirements of the input. 