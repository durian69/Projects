import streamlit as st
from openai import OpenAI
import json
import st_yled
import time
import random

st_yled.init()
client = OpenAI(api_key=st.secrets["KEY"])
st.set_page_config(layout="wide")

if "intro_done" not in st.session_state:
    st.session_state.intro_done = False

if "mode" not in st.session_state:
    st.session_state.mode = "intro"

if "name" not in st.session_state:
    st.session_state.name = ""

if "choice" not in st.session_state:
    st.session_state.choice = ""

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "current_scene" not in st.session_state:
   st.session_state.current_scene = None

if "level" not in st.session_state:
   st.session_state.level = 1

if "xp" not in st.session_state:
   st.session_state.xp = 0

if "new_xp" not in st.session_state:
    st.session_state.new_xp = 0

choice = st.session_state.choice


def stream_text(text):
    for char in text:
        yield char
        time.sleep(0.009)
#I got this function from the documentation in the StreamLit website for st.write_stream()

def level_up():
    lucky = random.randint(15, 40)
    return lucky

def print_scene(message_dict):
    situation = list(message_dict.keys())[0] 
    choices = message_dict[situation]
    st.write(stream_text(situation))
    for key, text in choices.items():
        st.write(stream_text(f"{key} {text}"))
# I created this function using AI in my last assignment

def generate_scene():
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.chat_history,
    )

    assistant_text = response.choices[0].message.content

    assistant_response = json.loads(response.choices[0].message.content)

    st.session_state.chat_history.append(
        {"role": "assistant", "content": assistant_text}
    )

    return assistant_response["message"]


def start_game():
    st.session_state.chat_history = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"The player's name is {st.session_state.name}"},
    ]
    st.session_state.current_scene = generate_scene()


def do_choice(choice):
    st.session_state.new_xp = level_up()
    st.session_state.xp += st.session_state.new_xp

    if st.session_state.xp >= 100:
        st.session_state.xp -= 100
        st.session_state.level += 1

    st.session_state.chat_history.append({
        "role": "user",
        "content": f"The player made this choice: {choice}. Respond with the consequence of the action and three more actions they can take."
    })

    st.session_state.current_scene = generate_scene()
    st.session_state.choice = ""
    st.rerun()


def scene(desc):
  column1, column2 = st.columns(2)
  
  with column2:
     with st_yled.container(border=True, border_color="#0F995A"):
        st_yled.write(f"You've gained {st.session_state.new_xp} XP.", font_size="10px")
          
        st_yled.slider(f"LEVEL {st.session_state.level}",
                       min_value=0, 
                       max_value=100,
                       value=st.session_state.xp, 
                       color="#0F995A",
                       disabled=True,
                        key=f"xp_slider_{st.session_state.level}_{st.session_state.xp}")
        #i asked chat_gpt how to fix my slider bc it didnt work, so it gave me the key==f"xp_slider_{st.session_state.level}_{st.session_state.xp}")
        st_yled.write("CONTROL PANEL",font_size="30px",font_weight="semi-bold")
        if st_yled.button("Option 1", border_color="#0F995A"):
          do_choice(1)
        if st_yled.button("Option 2", border_color="#0F995A"):
          do_choice(2)
        if st_yled.button("Option 3", border_color="#0F995A"):
          do_choice(3)

  with column1:
      print_scene(desc)

bg = "https://i.pinimg.com/1200x/67/c5/39/67c53974b3e9eb5d7b9f4dd50b80202c.jpg"
setting = """Once a cutting-edge orbital station researching genetic adaptability, Aegis-7 has been dark for years. It is now a drifting ruin of broken glass, frosted metal, and overgrown, mutated flora that has escaped the bio-labs. 

Your mission is to recover a secret lab experiment. This organism could spell out the end of human existence in its entirety. However, you will face multiple challenges, such as the  unstable enviroment, broken down robot guards, and unknown abandoned creatures.

Before you start..."""

#I got the setting information in the first sentence from AI

system_prompt= """ You are the Dungeon Master of this dungeon crawler game. The game takes place in a post-apocalyptic sci-fi world. The player is exploring an abandoned dangerous lab.
Once a cutting-edge orbital station researching genetic adaptability, Aegis-7 has been dark for years. It is now a drifting ruin of broken glass, frosted metal,
and overgrown, mutated flora that has escaped the bio-labs.The player is trying to recover a secret lab experiment. This organism could spell out the end of human existence in its entirety.
However, the player will have to face multiple challenges, such as the abondonded unstable enviroment, broken down robot guards, and unknown abandoned creatures.


You MUST ONLY output valid JSON.
Do NOT output explanations.
Do NOT output text outside JSON.
Do NOT change the structure.
Do NOT add extra keys.

The JSON MUST follow this exact template:

{"message": {
    "<CURRENT_SITUATION>": {
      "1.": "<OPTION_1>",
      "2.": "<OPTION_2>",
      "3.": "<OPTION_3>"}}}

- Replace <CURRENT_SITUATION> with a short description of what is happening.
- Replace each <OPTION_X> with a possible action.
- Always include exactly 3 numbered options.
- The situation must be a sentence.
- The options must be action sentences.
- The player must choose between the listed options.
- Do NOT rename keys.
- USE DOUBLE QUOTES

Example of valid output:

{
  "message": {
    "Welcome, Blingus, to the Kingdom of Eldoria. The dragon Ciraxia has been terrorizing the land, and you have been chosen to venture into the treacherous dungeons beneath the castle to slay the beast": {
      "1.": "Equip your sword and shield",
      "2.": "Light a torch to guide your way.",
      "3.": "Descend into the dark dungeons."
    }
  }
}

Now generate the situation."""

if not st.session_state.intro_done:
  st_yled.write(stream_text("DUNGEON CRAWLER"), font_size="40px", font_weight="extra-bold")
  time.sleep(1.2)
else:
  st_yled.write("DUNGEON CRAWLER", font_size="40px", font_weight="extra-bold")

if st.session_state.mode == "intro":
  with st_yled.container(border=True, border_color="#0F995A"):
    col1, col2 = st.columns(2)
    with col1:
      if not st.session_state.intro_done:
            st_yled.write(stream_text("MISSION-124"), font_size="30px", font_weight="bold")
      else:
          st_yled.write("MISSION-124", font_size="30px", font_weight="bold")
      st.image(bg)
      time.sleep(1)
    with col2:
      if not st.session_state.intro_done:
            st.write_stream(stream_text(setting))
      else:
          st.write(setting)
      st.session_state.name = st_yled.text_input("What is your name?",
                          background_color="#0D0E14",
                          border_color="#0F995A",
                          font_size="16px")
      st.session_state.intro_done = True
      if st.session_state.name != "":
        st.write_stream(stream_text(f"Agent {st.session_state.name}, are you ready to start?"))
        if st.button("YES"):
          st.session_state.mode = "game"
          st.rerun()

elif st.session_state.mode == "game":
  if st.session_state.current_scene is None:
    start_game()

  scene(st.session_state.current_scene)


# My application is a dungeon crawler game where an AI
# model is the game master. After the user inputs 
# their name, the AI will generate a scene based on the
# setting.Then, the user will have to choose one out of 
# 3 choices to make. The AI will reply with another scene
# based on the choice. This will continue infinitely. The
# user is expected to enter their name in the intro, then
# is expected to choose one option during each scene of
# the game.