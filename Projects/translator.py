import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["KEY"])

options = ["Chinese", "Malay", "Indonesian", "English", "Spanish"]

st.header("Translator 9000")

text = st.text_area("Enter your text:")

selected = []
for opt in options:
    if st.checkbox(opt, key=f"opt_{opt}"):
        selected.append(opt)


if st.button("Generate"):
    if text == "":
        st.warning("Please enter some text to translate.")
    elif selected == []:
        st.warning("Please select at least one language.")
    else:
        user_prompt = f"Translate {text} into the language(s) in {selected}. Preserve the original meaning, tone, and formatting. Do not add or omit information. Don't add any uneccessary special characters."

        # 4
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "user", "content": user_prompt}
            ]
        )

        # 5
        st.write(response.choices[0].message.content)

#In this translator, the code will translate the text inputted from the user to either Chinese, Malay, Indonesian, English, or Spanish, based on the user's choice. The user can pick more than one language to translate their text into. There is no limits on what the user can input, so it can be one word or a paragraph. 