import streamlit as st
from datetime import date
import pandas as pd
import os

# ---------- CONFIGURAZIONE BASE ----------
st.set_page_config(
    page_title="Dream Weekend in Southern Utah",
    page_icon="💚",
    layout="centered"
)

# ---------- STILE PERSONALIZZATO (TONI DI VERDE) ----------
st.markdown("""
    <style>
    .main {
        background-color: #f4fff8;
    }
    h1, h2, h3 {
        color: #1b4332;
    }
    .stButton > button {
        background-color: #40916c;
        color: white;
        border-radius: 999px;
        border: none;
        padding: 0.6rem 1.5rem;
        font-weight: 600;
    }
    .stButton > button:hover {
        background-color: #1b4332;
    }
    </style>
""", unsafe_allow_html=True)

# ---------- FUNZIONE PER SALVARE LE RISPOSTE (OPZIONALE) ----------
RESPONSES_FILE = "responses.csv"

def save_response(data: dict):
    df_new = pd.DataFrame([data])
    if os.path.exists(RESPONSES_FILE):
        df_old = pd.read_csv(RESPONSES_FILE)
        df = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df = df_new
    df.to_csv(RESPONSES_FILE, index=False)

# ---------- SIDEBAR ----------
st.sidebar.header("💚 Your Birthday Gift")
st.sidebar.write("A personalized, magical weekend in **Southern Utah**.")
st.sidebar.write("Planned with love by **THE ITALIAN** 🇮🇹")
st.sidebar.write("Answer the questions and let's shape your dream weekend together.")

# Se vuoi caricare un logo o una foto piccola nella sidebar:
# st.sidebar.image("images/small_photo.jpg", use_container_width=True)

# ---------- HERO SECTION ----------
st.title("Make Your Dream Weekend Come True 💚")

st.subheader("Gift Voucher – A Magical Weekend in Southern Utah")

st.markdown("""
Don't miss out on this one-time offer:  
**A magical weekend in Southern Utah**, brought to you by yours truly,  
**THE ITALIAN** 🇮🇹

Happy Birthday! 🎉  
This little website is here to plan **your** perfect weekend away –  
exactly how *you* want it.
""")

st.divider()

# ---------- SEZIONE FOTO + INFO TRIP ----------
st.header("✨ About the Weekend")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
Imagine:
- Red rock canyons  
- Starry skies 🌌  
- Road trip vibes  
- Coffee, playlists, and zero stress  

We'll choose together where to go and what to do – this is **your** dream weekend.
""")

with col2:
    # Qui metti le tue immagini locali, per esempio:
    # st.image("images/utah1.jpg", caption="Desert vibes", use_container_width=True)
    # st.image("images/utah2.jpg", caption="Canyons & sunsets", use_container_width=True)
    st.info("Here you can add a couple of beautiful photos from Southern Utah 🌄\n\n"
            "_Replace this box with `st.image(...)` when you have your pictures ready._")

st.divider()

# ---------- QUESTIONARIO ----------
st.header("💌 Help Me Plan Your Perfect Weekend")

st.write("Answer a few questions so I can tailor everything to what you love most.")

with st.form("rsvp_form"):
    name = st.text_input("Your name (so I know it's really you 💚)", "")
    
    excitement = st.slider(
        "How excited are you about a weekend in Southern Utah?",
        min_value=1, max_value=10, value=8
    )

    weekend_style = st.radio(
        "What kind of weekend are you dreaming of?",
        [
            "Mostly adventure (hikes, exploring, being active)",
            "Mostly relax (slow mornings, cozy vibes, spa/hot tub)",
            "A perfect mix of both"
        ]
    )

    activities = st.multiselect(
        "What sounds most fun to you? (you can pick more than one)",
        [
            "Scenic hikes 🥾",
            "Sunset watching 🌅",
            "Stargazing 🌌",
            "Photo stops everywhere 📸",
            "Cute cafés / brunch ☕",
            "Hot tub / spa time 🛁",
            "Just being together and doing nothing"
        ]
    )

    preferred_month = st.selectbox(
        "Roughly when would you like to go?",
        [
            "As soon as possible 😏",
            "Spring vibes",
            "Summer",
            "Fall colors",
            "Surprise me, you choose!"
        ]
    )

    message = st.text_area(
        "Anything you want to tell me? Fears, wishes, secret desires for this weekend…",
        placeholder="Write whatever you want here 💚"
    )

    submitted = st.form_submit_button("Send your answers 💚")

if submitted:
    response_data = {
        "date": date.today().isoformat(),
        "name": name,
        "excitement": excitement,
        "weekend_style": weekend_style,
        "activities": ", ".join(activities),
        "preferred_month": preferred_month,
        "message": message
    }

    # Salva su CSV (solo lato tuo / server)
    save_response(response_data)

    st.success("Thank you! Your answers have been sent 💚")
    st.balloons()

st.divider()

# ---------- MESSAGGIO FINALE ----------
st.header("🌿 From THE ITALIAN, with love")

st.markdown("""
No matter what you choose, the most important part of this trip is **you**  
(and maybe also snacks, but mostly you).

Can't wait to go on this adventure together. 💚
""")

# Se vuoi vedere le risposte quando apri l'app (solo per te)
with st.expander("🔐 (For me) Show collected answers"):
    if os.path.exists(RESPONSES_FILE):
        df = pd.read_csv(RESPONSES_FILE)
        st.dataframe(df)
    else:
        st.caption("No answers collected yet.")
