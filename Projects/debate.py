import streamlit as st
from openai import OpenAI
import json
import st_yled

st_yled.init()
client = OpenAI(api_key=st.secrets["KEY"])
st.set_page_config(layout="wide")

#================================================================
#   Session States
#================================================================

DEFAULT_TOPIC = "Pibbles are cuter than Meowls"

if "debate_generated" not in st.session_state:
    st.session_state.debate_generated = False

if "pibble" not in st.session_state:
    st.session_state.pibble = "OG Pibb"

if "meowl" not in st.session_state:
    st.session_state.meowl = "OG Meowl"

if "page" not in st.session_state:
    st.session_state.page = "setup"

if "finished" not in st.session_state:
    st.session_state.finished = False

if "show_debaters" not in st.session_state:
    st.session_state.show_debaters = False

if "topic" not in st.session_state:
    st.session_state.topic = DEFAULT_TOPIC

#================================================================
#   VARIABLES
#================================================================
    

og_meowl = "data:image/jpeg;base64,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"
evil_meowl = "https://i.pinimg.com/736x/6f/34/c7/6f34c7c7f73b17c4f37c5a465e948765.jpg"
gentle_meowl = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRzZFbPOYDVE0J7ddr3-ZZ39_CrBdUptDa2sg&s"
alien_meowl = "https://i.pinimg.com/236x/9a/18/7b/9a187b71e1403e95e6e33af8dee126f7.jpg"
cute_meowl = "https://i.pinimg.com/236x/e6/80/36/e68036cc9982338025a8eb22e8741584.jpg"

meowls = {"1": "OG Meowl", "2": "Evil Meowl", "3": "Gentleman Meowl", "4": "Alien Meowl", "5": "Cute Meowl"}
meowl_pics = {"OG Meowl": og_meowl, "Evil Meowl": evil_meowl, "Gentleman Meowl": gentle_meowl, "Alien Meowl": alien_meowl, "Cute Meowl": cute_meowl}
meowl_person = {"OG Meowl": "friendly, owl-like, wise", "Evil Meowl": "evil, unfriendly, aggresive, uses mean words", "Gentleman Meowl": "formal, polite, knowledgable", "Alien Meowl": "speaks alien language, alien-like", "Cute Meowl": "soft, caring, cute"}



og_pib = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQCE9CtsAqzOG9ElKx5YjWB__wVe3vjNSwqLw&s"
geeble = "https://i.redd.it/i-need-help-finding-the-original-source-of-this-stupidly-v0-n1rhx0owqhqa1.jpg?width=1080&format=pjpg&auto=webp&s=c67d2f8cd5add89ae9d5411b3c2e53029ad06bcb"
gmail = "https://static.wikia.nocookie.net/2c58faf3-2fa6-4bb3-98e7-c9b71670e4ab/scale-to-width/755"
pb = "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRDjRzh9aJ8VZysWHjM-K9szZWQ_josig68gNCNzr339lmr5Yz2"
washington = "https://i1.sndcdn.com/artworks-4lyzb1CUF41VcRNY-AptOOg-t500x500.jpg"

pibbles = { "1": "OG Pibb", "2": "Gmail", "3": "Washington", "4": "Geeble", "5": "PB Cup"}
pibble_pics = {"OG Pibb": og_pib, "Gmail": gmail, "Washington": washington, "Geeble": geeble, "PB Cup": pb}
pibble_person = {"OG Pibb": "nonchalant, chill", "Gmail": "zesty, kind", "Washington": "formal, polite, knowledgable", "Geeble": "speaks alien language, alien-like, mean", "PB Cup": "soft, caring, cute"}


meowl_names = []
pibble_names = []
for i in meowls:
    meowl_names.append(meowls[i])
for k in pibbles:
    pibble_names.append(pibbles[k])


#================================================================
#   Opening
#================================================================

def opening(history):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=history
    )
    message = response.choices[0].message.content
    history.append({"role": "assistant", "content": message})
    return message

#================================================================
#   Middle
#================================================================


def rebuttals(historya, historyb):
    last_message = historyb[-1]["content"] 
    historya.append({
        "role": "user",
        "content": f"Your opponent said: {last_message}. Respond with your rebuttal."
    })

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=historya
    )
    message = response.choices[0].message.content
    historya.append({"role": "assistant", "content": message})
    return message

#================================================================
#   Ending
#================================================================

def ending(history):
    history.append({
    "role": "user",
    "content": "Give your closing statement. Give 1-3 sentences, stay in character and keep your stance."})
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=history
    )
    message = response.choices[0].message.content
    history.append({"role": "assistant", "content": message})
    return message

#================================================================
#   RESET
#================================================================

def reset_debate(keep_topic=True):
    old_topic = st.session_state.topic if keep_topic else DEFAULT_TOPIC

    delete = ["chat_history_meowl", "chat_history_pibble","opening_meowl","opening_pibble","rebuttal_meowl","rebuttal_pibble","closing_meowl","closing_pibble","debate_generated"]

    for key in delete:
        if key in st.session_state:
            del st.session_state[key]

    st.session_state.page = "setup"          
    st.session_state.show_debaters = False
    st.session_state.finished = False
    st.session_state.topic = old_topic
    st.session_state.meowl = "OG Meowl"
    st.session_state.pibble = "OG Pibb"
    st.session_state.debate_generated = "False"

def start_new_debate():
    reset_debate(keep_topic=False)
    st.rerun()


#================================================================
#   Generate 
#================================================================

def generate_debate():
    if st.session_state.get("debate_generated", False):
        return

    chat_history_meowl = st.session_state.chat_history_meowl
    chat_history_pibble = st.session_state.chat_history_pibble

    st.session_state.opening_pibble = opening(chat_history_pibble)
    st.session_state.opening_meowl = opening(chat_history_meowl)

    st.session_state.rebuttal_pibble = []
    st.session_state.rebuttal_meowl = []

    for _ in range(3):
        st.session_state.rebuttal_pibble.append(
            rebuttals(chat_history_pibble, chat_history_meowl)
        )
        st.session_state.rebuttal_meowl.append(
            rebuttals(chat_history_meowl, chat_history_pibble)
        )

    st.session_state.closing_pibble = ending(chat_history_pibble)
    st.session_state.closing_meowl = ending(chat_history_meowl)

    st.session_state.debate_generated = True

#================================================================
#   Set Up
#================================================================


st_yled.title("ULTIMATE PIBBLE VS MEOWL DEBATE", font_weight="black", font_size="78px")
st.markdown("---")
col1, col2, col3 = st.columns([1,3,1])

with st.sidebar:
    st_yled.title("Pages", font_weight="black", font_size="10000px")
    if st.button("Set Up", icon=":material/star:", use_container_width=True):
        if st.session_state.debate_generated == True:
            st.error("""Click "Start Another Debate" in "Debate"!""")
        else: st.session_state.page = "setup"
    if st.sidebar.button("View Debaters", icon=":material/star:", use_container_width=True):
        st.session_state.page = "person"
    if st.button("Debate", icon=":material/star:", use_container_width=True):
        st.session_state.page = "debate"

if st.session_state.page == "setup":
    with col2:
        col1, col2 = st.columns([1,3])
        with col1:
            st_yled.write("Sir Charles Barkley", font_weight="black", font_size="21px")
            st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqaLolKl1dSLmZxwnUCv58fqwehjkuc1Bhjw&s")
        with col2:
            with st.container(border=True):
                st.markdown("""Welcome to the Ultimate Pibble VS Meowl Debate! I am Sir Charles Barkley, the host of this debate session. A Pibble and a Meowl is chosen from our batch, and they will debate about the topic you give them! To start...""")
                st_yled.selectbox("Choose the debate topic!",["Pibbles are cuter than Meowls", "Pibbles are stronger than Meowls", "Washing your belly is important", "Pibbles are better pets than Meowls",],key="topic", font_size="16px")
                topic = st.session_state.topic
                if st.button("DONE"):
                    st.session_state.show_debaters = True
                if st.session_state.show_debaters == True:
                    st.write("Great choice! Now, you can choose your debaters!")
                    c1, c2 = st.columns(2)
                    with c1: 
                        st.session_state.meowl = st_yled.selectbox("Choose your Meowl", meowl_names, font_size="16px")
                        meowl = st.session_state.meowl
                        st.image(meowl_pics[meowl], width=200)
                    with c2:
                        st.session_state.pibble = st_yled.selectbox("Choose your Pibble", pibble_names, font_size="16px")
                        pibble = st.session_state.pibble
                        st.image(pibble_pics[pibble], width=200)
                    if st.button("FINISH"):
                        st.session_state.finished = True
                        st.write("You're all done! Now you can click the 'Debate' button on the sidebar! Have a good time!")



#================================================================
#   Debate
#================================================================

if st.session_state.page == "debate":
    if st.session_state.finished == False:
        st.write("Complete the set up in 'Set Up' in the sidebar!")
    else:
        meowl_prompt = f"""You are {st.session_state.meowl}, a {meowl_person[st.session_state.meowl]} debater.
        You are arguing against the topic: {st.session_state.topic}.
        Follow these rules:
        - Present logical arguments with supporting evidence
        - Directly address points made by your opponent
        - Stay on topic and maintain your position
        - Keep responses between 1-3 sentences
        - Do not concede your position, but acknowledge valid counterpoints

        Each response should include:
        - A main argument or counterargument
        - Supporting reasoning or evidence
        - A question or challenge to your opponent
        
        Reminder:
        - You are a Meowl. You don't need to speak too formally unless instructed too. Encourage less advanced vocabulary."""
        

        pib_prompt = f"""You are {st.session_state.pibble}, a {pibble_person[st.session_state.pibble]} debater.
        You are arguing for the topic: {st.session_state.topic}.
        Follow these rules:
        - Present logical arguments with supporting evidence
        - Directly address points made by your opponent
        - Stay on topic and maintain your position
        - Keep responses between 1-3 sentences
        - Do not concede your position, but acknowledge valid counterpoints

        Each response should include:
        - A main argument or counterargument
        - Supporting reasoning or evidence
        - A question or challenge to your opponent
        
        Reminder:
        - You are a Pibble. You don't need to speak too formally unless instructed too. Encourage less advanced vocabulary."""

        if "chat_history_meowl" not in st.session_state:
            st.session_state.chat_history_meowl = [
                    {"role": "system", "content": meowl_prompt},
                    {"role": "user", "content": f"Give your opening statement on: {st.session_state.topic}"}
                ]
            
        chat_history_meowl = st.session_state.chat_history_meowl

        if "chat_history_pibble" not in st.session_state:
            st.session_state.chat_history_pibble = [
                {"role": "system", "content": pib_prompt},
                {"role": "user", "content": f"Give your opening statement on: {st.session_state.topic}"}]
            
        chat_history_pibble = st.session_state.chat_history_pibble


        generate_debate()
                
        st_yled.title("OPENING STATEMENTS", font_weight="black", font_size="100px")

        pibble1, pibble2 = st.columns([3,1])
        meowl1, meowl2 = st.columns([1,3])

        pibble2.image(pibble_pics[st.session_state.pibble], width=400)
        with pibble1.container(border=True):
            st.write(st.session_state.opening_pibble)

        meowl1.image(meowl_pics[st.session_state.meowl], width=400)
        with meowl2.container(border=True):
            st.write(st.session_state.opening_meowl)




        st.markdown("---")
        st_yled.title("REBUTTALS", font_weight="black", font_size="100px")
        for i in range(3):
            st.subheader(f"Round {i+1}")
            pibble1, pibble2 = st.columns([3,1])
            meowl1, meowl2 = st.columns([1,3])

            pibble2.image(pibble_pics[st.session_state.pibble], width=400)
            with pibble1.container(border=True):
                st.write(st.session_state.rebuttal_pibble[i])

            meowl1.image(meowl_pics[st.session_state.meowl], width=400)
            with meowl2.container(border=True):
                st.write(st.session_state.rebuttal_meowl[i])




        st.markdown("---")
        st_yled.title("CLOSING STATEMENTS", font_weight="black", font_size="100px")
        pibble1, pibble2 = st.columns([3,1])
        meowl1, meowl2 = st.columns([1,3])

        pibble2.image(pibble_pics[st.session_state.pibble], width=400)
        with pibble1.container(border=True):
            st.write(st.session_state.closing_pibble)

        meowl1.image(meowl_pics[st.session_state.meowl], width=400)
        with meowl2.container(border=True):
            st.write(st.session_state.closing_meowl)
        
        st.markdown("---")
        if st.button("Start Another Debate"):
            reset_debate()
            start_new_debate()


if st.session_state.page == "person":
    st.title("Meowls")
    st.markdown("---")
    for meowl in meowl_person:
        st.header(meowl)
        meowls1, meowls2 = st.columns([1,4])
        with meowls1:
            st.image(meowl_pics[meowl])
        with meowls2:
            st.write(meowl_person[meowl])

    st.markdown("---")
    st.title("Pibbles")
    st.markdown("---")
    for pibble in pibble_person:
        st.header(pibble)
        pibbles1, pibbles2 = st.columns([1,4])
        with pibbles1:
            st.image(pibble_pics[pibble])
        with pibbles2:
            st.write(pibble_person[pibble])


# My application is a debate engine that makes a Meowl and a Pibble debate over existing topics.
# When the user first enters, they are met by Sir Charles Barkley, who introduces them to the website.
# Then, he lets the user choose the topic in a selectbox. Then, the user can choose which Pibble and
# Meowl they want to use in the debate, each with their own personality. Then, the chosen Meowl and
# Pibble will debate about the chosen topic, the Meowl against the topic and the Pibble for. The user
# user is expected to choose one of the options in the selectboxes. After it is done, the user can choose
# to start anotehr debate.