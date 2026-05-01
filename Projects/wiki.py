import streamlit as st

wiki_data = {
    "Zeus": {
        "name": "Zeus",
        "history": "Zeus is the king of the Olympian gods and ruler of Mount Olympus. He overthrew his father Cronus and divided the world among his brothers.",
        "characteristics": "God of the sky and thunder. Known for wielding a lightning bolt. Often depicted as a powerful bearded man.",
        "trivia": ["His Roman equivalent is Jupiter.", "He had over 100 children.", "His symbol is the eagle."]
    },
    "Athena": {
        "name": "Athena",
        "history": "Athena is the goddess of wisdom and war strategy. She was born fully armored from the forehead of Zeus.",
        "characteristics": "Known for intelligence over brute strength. Patron goddess of Athens. Often shown with an owl and olive branch.",
        "trivia": ["Her Roman equivalent is Minerva.", "She never had a romantic partner.", "She gifted the olive tree to Athens."]
    },
    "The Underworld": {
        "name": "The Underworld",
        "history": "The Underworld is the realm of the dead ruled by Hades. Souls travel there after death guided by Hermes.",
        "characteristics": "Divided into regions like Elysium and Tartarus. Surrounded by rivers including the Styx and Lethe.",
        "trivia": ["The three-headed dog Cerberus guards the entrance.", "Only a few heroes ever escaped alive.", "Charon ferries souls across the Styx."]
    },
    "The Olympians": {
        "name": "The Olympians",
        "history": "The Twelve Olympians are the major gods who reside on Mount Olympus. They rose to power after defeating the Titans.",
        "characteristics": "Each controls a domain of life. They interact with mortals frequently and often quarrel among themselves.",
        "trivia": ["There are actually 14 gods sometimes listed.", "They drink nectar and eat ambrosia.", "Mount Olympus is the highest peak in Greece."]
    },
    "The Trojan War": {
        "name": "The Trojan War",
        "history": "The Trojan War was a legendary conflict between Greece and Troy. It began after Paris of Troy took Helen from her husband Menelaus.",
        "characteristics": "Lasted ten years. Involved gods taking sides. Ended with the famous Trojan Horse trick.",
        "trivia": ["Homer's Iliad covers part of the war.", "Troy is believed to be in modern-day Turkey.", "Achilles was the greatest Greek warrior."]
    }
}

st.sidebar.subheader("Pages")

st.title("📖 Ancient Greek Mythology Wiki")
st.markdown("---")
placeholder = st.empty()
with placeholder:
    st.info("Select a page from the sidebar to start reading.")
for page in wiki_data.keys():
    if st.sidebar.button(page, use_container_width=True):
        placeholder.empty()
        selected = page
        data = wiki_data[selected]
        st.title(data["name"])
        st.markdown("---")
        left, right = st.columns(2)

        with left:
            st.subheader("History")
            st.write(data["history"])
            st.subheader("Characteristics")
            st.write(data["characteristics"])
        with right:
            st.subheader("Trivia")
            num = 1
            for j in data["trivia"]:
                st.write(f"{num}. {j}")
                num += 1




