import streamlit as st
# from openai import OpenAI
import st_yled
import random
import time

# client = OpenAI(api_key=st.secrets["KEY"])
st_yled.init()

# ================================================
# VARIABLES
# ================================================
bg = "https://cdn.discordapp.com/attachments/1299848186181193788/1497497368072028212/IMG_4891.png?ex=69f1085a&is=69efb6da&hm=5d9aec36dbef521b3efe5c4d8b90325d89484b54d056ffa80e367f8aa09b5513&"
standing = "https://cdn.discordapp.com/attachments/1299848186181193788/1497497379732197526/IMG_4890.png?ex=69f1085d&is=69efb6dd&hm=cfc1785d6ba2948842d1ebf0b039c5542877f06a6e10c2e9e99b38af02cdcc45&"
phone = "https://cdn.discordapp.com/attachments/1299848186181193788/1497497372505280572/IMG_4892.png?ex=69f1085b&is=69efb6db&hm=5bc607b6c6e81fb1f6c23288714f29840c0a383ad0a05235714ca00a3f67fcdd&"

placeholder = st.empty()

dialogue = [
    {"image": bg, "person": "You", "text": "*You enter a convenience store.*", "chat": False},
    {"image": bg, "person": "You", "text": "Wow, this is a big store! But where is the cashier?", "chat": False},
    {"image": standing, "person": "You", "text": "!!", "chat": False},
    {"image": standing, "person": "Cashier", "text": "Hey! How's it going?", "chat": False},
    {"image": standing, "person": "You", "text": "How's my... uh... my...", "chat": True}
    ]

if "index" not in st.session_state:
    st.session_state.index = 0

if "mode" not in st.session_state:
    st.session_state.mode = "intro"

if "chat" not in st.session_state:
    st.session_state.chat = False

luck = random.randint(1,6)
desc = ""
if luck == 1:
    desc = "Creativity is overated anyways."
elif luck == 2:
    desc = "just remember, ai is trained off the best artists and improves more in a day then you 'real artists' could in your whole lives #BreakThePencil"
elif luck == 3:
    desc = "The game — an ostensibly illuminating interactive parable — demonstrates how excessive dependence on artificial intelligence can precipitate intellectual atrophy, diminished agency, and catastrophic decision - making under the polished illusion of efficiency."
elif luck == 4:
    desc = "Why are you reading this?"
elif luck == 5:
    desc = "ChatGPT, generate me a game about the harms of over-dependence on AI."
elif luck == 6:
    desc = "sory chatghpt was down when i made this description llol"



# ================================================
# FUNCTIONS
# ================================================

def typewrite(text):
    for char in text:
        yield char
        time.sleep(0.05)

def abt():
    with st.container(border=True):
        st.write("In Cashier.AI, you enter a convenience store, like any other day. Of course, you decide to let generative AI help with daily tasks. It's not like you need AI to do everything in your life; it's just a tool, right?")
        st.markdown("*Note: Using Generative AI as a learning tool to collect information easily, automating repetitive tasks, summarizing long contents, etc, are not bad. What this application is targeting is how people start using Generative AI as a crutch instead of a growing tool, losing their creativity and independence in the process.*")
    if st.button("RETURN TO MAIN MENU"):
        st.session_state.mode = "intro"
        st.rerun()

def exit():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.title("Thanks for Playing! :D")

def main_menu():
    with st.container(border=True):

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st_yled.title("CASHIER.AI", font_size="50px")
            st.write(f"{desc}")
            if st.button("PLAY", use_container_width=True):
                st.session_state.mode = "game"
                st.rerun()
                
            if st.button("ABOUT", use_container_width=True):
                st.session_state.mode = "abt"
                st.rerun()

            if st.button("EXIT", use_container_width=True):
                st.session_state.mode = "exit"
                st.rerun()


def chat():
    with st.container(border=True):
        st.markdown('<div style="page-break-after: always;"></div>', unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1,2,1])

        with col2:
            st_yled.title("‎ChatGPT", font_size="70px")

        st.markdown("---")

        if st.session_state.chat == False:
            time.sleep(1)
            with st.chat_message("human"):
                human_text = "HELP ME PLS"
                st.write_stream(typewrite(human_text))

            time.sleep(1)
            with st.chat_message("ai"):
                text = "haha no"
                st.write_stream(typewrite(text))
            st.session_state.chat = True
        else:
            human_text = st.chat_message("human")
            human_text.write("HELP ME PLS")

            ai_text = st.chat_message("ai")
            ai_text.write("haha no")

            time.sleep(1)
        if st.button("return"):
            st.session_state.mode = "game"
            st.session_state.chat = False
            st.rerun()
            
def game(dialogue):
    st.markdown('<div style="page-break-after: always;"></div>', unsafe_allow_html=True)
    for scene in dialogue:
        with placeholder.container():
            st.image(scene["image"])
            st.write(scene["person"])
            st.write_stream(typewrite(scene["text"]))
            if scene["chat"] == True:
                if st.button("USE CHATGPT"):
                    st.session_state.mode = "chat"
                    st.rerun()
            else:
                if st.button("NEXT"):
                    st.session_state.index += 1
                if st.session_state.index >= len(dialogue):
                    st.session_state.index = len(dialogue) - 1
                st.rerun()
        time.sleep(2)
# ================================================
# GAME FLOW
# ================================================

if st.session_state.mode == "intro":
    main_menu()
elif st.session_state.mode == "abt":
    abt()
elif st.session_state.mode == "exit":
    exit()
elif st.session_state.mode == "chat":
    chat()
elif st.session_state.mode == "game":
    game(dialogue)
