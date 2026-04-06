import streamlit as st
from openai import OpenAI
import json
import st_yled

st_yled.init()
st.set_page_config(layout="wide")
client = OpenAI(api_key=st.secrets["KEY"])

template = {"Common":{
"Name": "NAME",
"Lore": "LORE",
"Cookies": "COOKIES",
"Trivia": "TRIVIA",},
"Rare":{
"Name": "NAME",
"Lore": "LORE",
"Cookies": "COOKIES",
"Trivia": "TRIVIA",},
"Epic":{
"Name": "NAME",
"Lore": "LORE",
"Cookies": "COOKIES",
"Trivia": "TRIVIA",},
"Super Epic":{
"Name": "NAME",
"Lore": "LORE",
"Cookies": "COOKIES",
"Trivia": "TRIVIA",},
"Legendary":{
"Name": "NAME",
"Lore": "LORE",
"Cookies": "COOKIES",
"Trivia": "TRIVIA",},
"Ancient":{
"Name": "NAME",
"Lore": "LORE",
"Cookies": "COOKIES",
"Trivia": "TRIVIA",},
"Special":{
"Name": "NAME",
"Lore": "LORE",
"Cookies": "COOKIES",
"Trivia": "TRIVIA",},
}

system_prompt = f"""Create a wiki about each rarities in Cookie Run: Kingdom. Include the rarity's name, it's importance or lore in the game, a few cookies who are part of the rarity and a one sentence description of each one, and add a few trivia facts, whether it be about the process of the creation of the rarity or lore fun facts. Respond in JSON in this format: {template}. Replace the variable that are all caps with the appropriate information. Replace COOKIES with a string. Do not make up any information and make sure it is accurate and true and source it from the actual wiki. Do not add any other sentences, only include the wiki. In your response, do NOT print "```json" or "```". Make sure your information is up to date. Use double quotes to enclose your information."""

# 4
@st.cache_data
def get():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": system_prompt}
        ]
    )
    return json.loads(response.choices[0].message.content)

message = get()

if "selected" not in st.session_state:
    st.session_state.selected = None

#for the cache function, I looked at the streamlit api documentation and researched abt it. And Gemini AI helped a bit bc of the webpage summarization tool.

#-----------B81414




with st.sidebar:
    st_yled.title("Pages", font_weight="black", font_size="10000px")

col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    st.image("https://static.wikia.nocookie.net/cookierunkingdom/images/3/3b/Wiki_logo.png/revision/latest/scale-to-width-down/350?cb=20240413202126", width=500)
    st_yled.subheader("Welcome to the Cookie Run: Kingdom Wiki! Check out the pages on the sidebar to start reading.",
                font_size="20px",
                font_weight="bold")

for page in message.keys():
    with st.sidebar:
        if st_yled.button(page, border_style=None, icon=":material/star:", use_container_width=True):
            st.session_state.selected = page
if st.session_state.selected:
    selected = st.session_state.selected
    data = message[selected]

    st.markdown("---")
    st.title(data["Name"])
    st.markdown("---")

    left, right = st.columns(2)

    with left:
        st.subheader("Lore")
        st.write(data["Lore"])
        st.subheader("Cookies")
        st.write(data["Cookies"])
    with right:
        st.subheader("Trivia")
        st.write(data["Trivia"])
        
st.markdown("---")

st.image("https://static.wikia.nocookie.net/cookierun/images/4/4f/Cookie_Run_Kingdom_Title_Screen.png/revision/latest?cb=20210130210729")

# My aplication is a wikipedia about the game Cookie Run: Kingdom. It is about the rarities of the cookies you can get in the game, which is the name, lore, trivia, and cookies in that rarity. The user is expected to choose a page from the sidebar to access the information of the rarities.


