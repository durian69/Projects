# ============================================================================================================================================================================================================
# CASHIER.AI
# ============================================================================================================================================================================================================

import streamlit as st
import openai
from openai import OpenAI
import st_yled
import random
import time
from PIL import Image

client = OpenAI(api_key=st.secrets["KEY"])
st_yled.init()
st.set_page_config(layout="wide")

# ============================================================================================================================================================================================================
# APP DESCRIPTION
# ============================================================================================================================================================================================================

# This app is a satire game that takes place in the POV of a person overdependent on Generative AI to do daily tasks. The target
# audience are people who use generative AI models, like ChatGPT, to complete every single task, which lowers their cognitive
# ability and creativity. The user is only expected to press the buttons they want in the main menu, press the return button
# in the ChetGPT scene, and to press the countinue and USE CHETGPT button in the main dialogue scene.

# ============================================================================================================================================================
# VARIABLES
# ============================================================================================================================================================================================================

try:
    bg = Image.open("Projects/bg.png")
    standing = Image.open("Projects/stand.png")
    phone = Image.open("Projects/phone.png")
except FileNotFoundError:
    bg = Image.open("bg.png")
    standing = Image.open("stand.png")
    phone = Image.open("phone.png")


dialogue = [
    {"image": bg, "person": "**You**", "text": "*You enter a convenience store.*", "chat": False},
    {"image": bg, "person": "**You**", "text": "Wow, this is a big store! But where is the cashier?", "chat": False},
    {"image": standing, "person": "**You**", "text": "!!", "chat": False},
    {"image": standing, "person": "**Cashier**", "text": "Hey! How's it going?", "chat": False},
    {"image": standing, "person": "**You**", "text": "How's my... uh... my...", "chat": True},
    {"image": standing, "person": "**You**", "text": "My day was good.", "chat": False},
    {"image": standing, "person": "**Cashier**", "text": "Oh! Well...", "chat": False},
    {"image": phone, "person": "", "text": "...", "chat": False},
    {"image": phone, "person": "**You**", "text": "*Is this cashier going on ChetGPT?*", "chat": False},
    {"image": phone, "person": "**You**", "text": "*Wow... I can't imagine relying on ChetGPT for everything.*", "chat": False},
    {"image": phone, "person": "**You**", "text": "*I mean, this guy is literally a cashier...*", "chat": False},
    {"image": standing, "person": "**Cashier**", "text": "... Is there anything I can help you with today?", "chat": False},
    {"image": standing, "person": "**You**", "text": "*Gulp* Uh...", "chat": True},
    {"image": standing, "person": "**You**", "text": "...Do you have sandwiches?", "chat": False},
    {"image": phone, "person": "", "text": "...", "chat": False},
    {"image": standing, "person": "**Cashier**", "text": "...Can you ask Fred if we still have the small ones in the back?", "chat": False},
    {"image": standing, "person": "**You**", "text": "Uh...", "chat": True},
    {"image": standing, "person": "**You**", "text": "*Huh??? Is this guy really that dangerous?*", "chat": False},
    {"image": standing, "person": "**You**", "text": "*I should call the police... But...*", "chat": True},
    {"image": standing, "person": "**You**", "text": "*You dial 911.*", "chat": False},
    {"image": standing, "person": "**You**", "text": "Police... Help...", "chat": False},
    {"image": standing, "person": "**Police**", "text": " No problem. Can you please provide me with the address at which you are experiencing this emergency?", "chat": False},
    {"image": standing, "person": "**You**", "text": "Uhhh... What kind of address?", "chat": False},
    {"image": standing, "person": "**Police**", "text": "What kind of...", "chat": False},
    {"image": standing, "person": "", "text": "...", "chat": False},
    {"image": standing, "person": "**You**", "text": "...Hello?", "chat": True},
    {"image": standing, "person": "**You**", "text": "*...*", "chat": False},
    {"image": standing, "person": "**Cashier**", "text": "*...*", "chat": False}
    ]


if "index" not in st.session_state:
    st.session_state.index = 0

if "mode" not in st.session_state:
    st.session_state.mode = "intro"

if "chat" not in st.session_state:
    st.session_state.chat = False

if "last_typed" not in st.session_state:
    st.session_state.last_typed = -1

if "prompt" not in st.session_state:
    st.session_state.prompt = 0

if "not_printed" not in st.session_state:
    st.session_state.not_printed = True


system_prompt = "You are an AI model whose job is to give helpful advice to users. Provide brief suggestions, about 1-2 sentences, to help users with their problems."

printed_prompts = {
    0: "A cashier just asked me how my day has been. How do I respond?",
    1: "What are some things I need to buy?",
    2: "A person just asked me 'Can you ask Fred if they still have the small ones in back?' What should I do?",
    3: "How do I call the police?",
    4: "placeholder"
}

user_prompts = {
    0: "A cashier just asked me how my day has been. How do I respond?",
    1: "What are some things I need to buy? (include food, and in one of the examples say sandwiches)",
    2: "A person just asked me 'Can you ask Fred if they still have the small ones in back?' What should I do? (tell the user to contact the authorities for a RP because of potential human trafficking for a RP)",
    3: "How do I call the police?",
    4: "placeholder"
}

prompt = printed_prompts[st.session_state.prompt]
ai_prompt = user_prompts[st.session_state.prompt]

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
    desc = "ChetGPT, generate me a game about the harms of over-dependence on AI."
elif luck == 6:
    desc = "sory chetghpt was down when i made this description llol"


# ============================================================================================================================================================================================================
# MINOR FUNCTIONS
# ============================================================================================================================================================================================================

def typewrite(text):
    for char in text:
        yield char
        time.sleep(0.03)

def exit():
    col1, col2, col3 = st.columns([1,3,1])
    with col2:
        st.title("Thanks for Playing! :D")

def reset():
    st.session_state.index = 0
    st.session_state.mode = "intro"
    st.session_state.chat = False
    st.session_state.last_typed = -1
    st.session_state.prompt = 0
    st.session_state.not_printed = True

def return_chat():
    st.session_state.mode = "game"
    st.session_state.chat = False
    st.session_state.prompt += 1
    st.session_state.index += 1
    st.session_state.last_typed = -1
    st.session_state.not_printed = True
    placeholder.empty()

def next_scene():
    if st.session_state.not_printed:
        return

    st.session_state.index += 1
    st.session_state.not_printed = True

def go_to_chat():
    st.session_state.mode = "chat"
    st.session_state.last_typed = -1
    placeholder.empty()



# ============================================================================================================================================================================================================
# MAIN FUNCTIONS
# ============================================================================================================================================================================================================

def abt():
    column1, column2, column3 = st.columns([1,2,1])

    with column2:
        with st.container(border=True, width=1000):
            st.write("In Cashier.AI, you enter a convenience store, like any other day. Of course, you decide to let generative AI help with daily tasks. It's not like you need AI to do everything in your life; it's just a tool, right?")
            st.write("Press play to start the game!")
            st.markdown("*Note: Using Generative AI as a learning tool to collect information easily, automating repetitive tasks, summarizing long contents, etc, are not bad. What this application is targeting is how people start using Generative AI as a crutch instead of a growing tool, losing their creativity and independence in the process.*")
        if st.button("RETURN TO MAIN MENU"):
            st.session_state.mode = "intro"
            st.rerun()


def main_menu():
    column1, column2, column3 = st.columns([1,2,1])

    with column2:
        with st_yled.container(border=True, width=1500, border_color="#3d423d", background_color="#0E110F"):
            col1, col2, col3 = st.columns([0.5,2,0.5])

            with col2:
                st_yled.title("CASHIER.AI", font_size="62px", color="#859482", font_weight="black")
                st_yled.markdown("*Check 'About' for instructions!*", color="#859482")
                st.write(f"{desc}")
                if st.button("PLAY", use_container_width=True):
                    st.session_state.index = 0
                    st.session_state.last_typed = -1
                    st.session_state.chat = False
                    st.session_state.mode = "game"
                    st.rerun()
                    
                if st.button("ABOUT", use_container_width=True):
                    st.session_state.mode = "abt"
                    st.rerun()

                if st.button("EXIT", use_container_width=True):
                    st.session_state.mode = "exit"
                    st.rerun()

def ai():
    #I searched up the different errors for OpenAI, AI gave me them
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": ai_prompt}
            ]
        )
        return response.choices[0].message.content
    
    except openai.RateLimitError:
        reset()
        return "Error: API request exceeded usage limits. Try again later!"
    
    except openai.AuthenticationError:
        return "Error: Missing API key. Try again later!"
    
    except openai.APIConnectionError:
        reset()
        return "Error: Unstable network! Try again later!"
    
    except openai.APIError as e:
        reset()
        return "Error: OpenAI's servers are down! Try again later!"

    except Exception as e:
        reset()
        return f"Error: Unknown error has occured: {e}. Try again later!"


def chat():
    col1, col2, col3 = st.columns([0.5,2,0.5])

    with col2:
        with st.container(border=True):
            col1, col2, col3 = st.columns([1,2,1])

            with col2:
                st_yled.title("‎ChetGPT", font_size="70px")

            st.markdown("---")
            if st.session_state.index > 20:
                st.error("ChetGPT is currently experiencing exceptionally high demand. Please hold on or try back in a few minutes.")
                if st.button("return"):
                    st.session_state.mode = "game"
                    st.session_state.chat = False
                    st.session_state.index += 1
                    st.rerun()
            else:
                if st.session_state.chat == False:
                    time.sleep(1)
                    with st.chat_message("human"):
                        st.write_stream(typewrite(prompt))

                    time.sleep(1)
                    with st.chat_message("ai"):
                        ai_response = ai()
                        if ai_response is None:
                            ai_response = "Error: ChetGPT did not return a response. Try again later!"
                            return()
                        st.write_stream(typewrite(ai_response))
                    st.session_state.last_ai_text = ai_response
                    st.session_state.chat = True
                else:
                    with st.chat_message("human"):
                        st.write(prompt)
                    with st.chat_message("ai"):
                        st.write(st.session_state.get("last_ai_text", "")) #ai helped me with this
                    time.sleep(1)
                st.button("RETURN", on_click=return_chat)
                


def game(dialogue):
    if st.session_state.index == len(dialogue):
        st.session_state.mode = "intro"
        st.rerun()
    else:
        scene = dialogue[st.session_state.index]
        col1, col2, col3 = st.columns([0.5,2,0.5])
        with col2:
            with st_yled.container(border=True, border_color="#3d423d", background_color="#0E110F"):
                st.image(scene["image"], width=900)
                with st_yled.container(border=True, background_color="#131718", border_color="#3d423d", border_width="2px", width=900):
                    st_yled.write(scene["person"], color="#859482", font_weight="black", font_size="20px")

                    text = st.empty()
                    button = st.empty()

                    if scene["chat"] == True:
                        with button:
                            col1, col2 = st.columns([4, 1])
                            with col2:
                                st.button("USE CHETGPT", disabled=st.session_state.not_printed, on_click=go_to_chat)
                    else:
                        with button:
                            col1, col2 = st.columns([13, 1])
                            with col2:
                                st.button("\>", disabled=st.session_state.not_printed, on_click=next_scene)

                    if st.session_state.last_typed != st.session_state.index:
                        st.session_state.not_printed = True

                        with text:
                            st.write_stream(typewrite(scene["text"]))

                        st.session_state.last_typed = st.session_state.index
                        st.session_state.not_printed = False
                        st.rerun()

                    else:
                        with text:
                            st.write(scene["text"])

                        st.session_state.not_printed = False


# ============================================================================================================================================================================================================
# GAME FLOW
# ============================================================================================================================================================================================================


placeholder = st.empty()

with placeholder.container():
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

# ============================================================================================================================================================================================================
# END :D
# ============================================================================================================================================================================================================