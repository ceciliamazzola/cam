# pages/the_guide.py
import streamlit as st
import os
import base64

def _get_base64_image(path: str) -> str:
    with open(path, "rb") as img:
        return base64.b64encode(img.read()).decode()

def render():
    # CSS specific for this page
    st.markdown("""
    <style>
        .guide-container {
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-top: 4rem;
            margin-bottom: 2rem;
        }

        .guide-card {
            background: rgba(255, 255, 255, 0.9);
            border-radius: 32px;
            padding: 2.5rem 3rem;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
            max-width: 850px;
            backdrop-filter: blur(8px);
            animation: fadeIn 1.4s ease-out;
        }

        .guide-inner {
            display: flex;
            flex-wrap: wrap;
            gap: 2rem;
            align-items: center;
            justify-content: center;
        }

        .guide-photo {
            width: 260px;             /* o 240/280, come ti piace */
            height: auto;             /* mantiene le proporzioni originali */
            border-radius: 24px;      /* angoli morbidi ma non tonda */
            object-fit: cover;
            box-shadow: 0 12px 32px rgba(0,0,0,0.18);
        }

        .guide-info-title {
            font-size: 1.8rem;
            font-weight: 700;
            color: #1b4332;
            margin-bottom: 0.5rem;
        }

        .guide-info-subtitle {
            font-size: 1rem;
            color: #2b6b4a;
            margin-bottom: 1rem;
        }

        .guide-info-table {
            font-size: 0.95rem;
            color: #000000;
        }

        .guide-info-label {
            font-weight: 600;
            color: #1b4332;
            padding-right: 0.5rem;
            white-space: nowrap;
        }

        .guide-info-row {
            margin-bottom: 0.25rem;
        }

        .guide-section-title {
            font-size: 1.5rem;
            font-weight: 700;
            color: #1b4332;
            margin-top: 2.5rem;
            margin-bottom: 0.5rem;
        }

        .guide-section-sub {
            color: #2b6b4a;
            margin-bottom: 1.5rem;
            font-size: 0.98rem;
        }

        .guide-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 2.2rem;              /* più spazio orizzontale e verticale tra le cards */
            margin-bottom: 2.5rem;    /* più spazio dal fondo */
            margin-top: 1rem;         /* più spazio dall’alto */
        }

        .guide-chip {
            background: rgba(255,255,255,0.95);
            border-radius: 18px;
            padding: 1.2rem 1.3rem;   /* un filo più grande e “arioso” */
            box-shadow: 0 10px 26px rgba(0,0,0,0.08);
            font-size: 0.95rem;
            color: #000000;
            margin-bottom: 0.4rem;    /* ulteriore distacco interno tra una card e l’altra */
        }


        .guide-chip-label {
            font-weight: 600;
            color: #1b4332;
            margin-bottom: 0.25rem;
        }

        .guide-chip-img {
            width: 100%;
            border-radius: 14px;
            margin-bottom: 0.5rem;
            object-fit: cover;
            max-height: 160px;
        }

        .guide-chip-img-half {
            width: 49%;
            border-radius: 14px;
            margin-bottom: 0.5rem;
            object-fit: cover;
            max-height: 140px;
            display: inline-block;
        }

        @media (max-width: 700px) {
            .guide-card {
                padding: 2rem 1.5rem;
                margin: 0 1rem;
            }
            .guide-inner {
                flex-direction: column;
            }
            .guide-photo {
                width: 180px;
                height: 180px;
            }
        }
    </style>
    """, unsafe_allow_html=True)

    # ---------- MAIN CARD: PHOTO + BASIC INFO ----------
    image_path = os.path.join("images", "guide.jpg")
    img_b64 = _get_base64_image(image_path)

    st.markdown(f"""
    <div class="guide-container">
        <div class="guide-card">
            <div class="guide-inner">
                <div>
                    <img src="data:image/jpeg;base64,{img_b64}" class="guide-photo" />
                </div>
                <div>
                    <div class="guide-info-title">The Guide: CECILIA</div>
                    <div class="guide-info-subtitle">
                        Italian girl temporarily lost in the US
                    </div>
                    <div class="guide-info-table">
                        <div class="guide-info-row">
                            <span class="guide-info-label">Age:</span>
                            <span>24</span>
                        </div>
                        <div class="guide-info-row">
                            <span class="guide-info-label">Date of birth:</span>
                            <span>October 3rd, 2001</span>
                        </div>
                        <div class="guide-info-row">
                            <span class="guide-info-label">Citizenship:</span>
                            <span>Italian</span>
                        </div>
                        <div class="guide-info-row">
                            <span class="guide-info-label">Height:</span>
                            <span>Just enough to reach your lips</span>
                        </div>
                        <div class="guide-info-row">
                            <span class="guide-info-label">Weight:</span>
                            <span>Enough to carry you when you're tired</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ---------- EXTRA INFO SECTION ----------
    st.markdown(
        '<div class="guide-section-title">A few more things about your guide 🤓</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="guide-section-sub">'
        '<i>Important note:</i> this guide is inexperienced and slightly clueless; '
        'everything is at your own risk (but hopefully very fun).'
        '</div>',
        unsafe_allow_html=True
    )

    # ---------- PREPARE IMAGES FOR CARDS ----------
    lasagna_b64 = _get_base64_image(os.path.join("images", "lasagna.jpg"))
    suzzara_b64 = _get_base64_image(os.path.join("images", "suzzara.jpg"))
    family_b64  = _get_base64_image(os.path.join("images", "family.jpg"))
    friends_b64 = _get_base64_image(os.path.join("images", "friends.jpg"))
    milan_b64   = _get_base64_image(os.path.join("images", "milan.jpg"))
    polimi_b64  = _get_base64_image(os.path.join("images", "polimi.jpg"))
    sleep_b64   = _get_base64_image(os.path.join("images", "sleep.jpg"))
    autumn_b64  = _get_base64_image(os.path.join("images", "autumn.jpg"))
    sister_b64  = _get_base64_image(os.path.join("images", "sister.jpg"))
    pizza_b64   = _get_base64_image(os.path.join("images", "pizza.jpg"))

    # ---------- Small info cards ----------
    st.markdown('<div class="guide-grid">', unsafe_allow_html=True)

    # Favorite color
    st.markdown("""
        <div class="guide-chip">
            <div class="guide-chip-label">Favorite color</div>
            <div>
                <span style="color:#0b4f46; font-weight:600;">
                    Deep teal / petrol green
                </span>
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Favorite movie
    st.markdown("""
        <div class="guide-chip">
            <div class="guide-chip-label">Favorite movie</div>
            <div><i>La La Land</i></div>
            <div style="margin-top:0.3rem; font-size:0.9rem;">
                Favorite line: “Here’s to the fools who dream.”
            </div>
        </div>
    """, unsafe_allow_html=True)

        # Favorite song – Bella Storia
    st.markdown("""
        <div class="guide-chip">
            <div class="guide-chip-label">Favorite song</div>
            <div><i>Bella Storia - Fedez</i></div>
            <div style="margin-top:0.3rem; font-size:0.9rem;">
                A love song about wanting to try, to make things work, and to build a beautiful story together.<br>
                Because if there’s one thing I might love even more than sleeping, it’s love itself.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Favorite food (with lasagna photo)
    # Favorite food (with lasagna photo)
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Favorite food</div>
            <img src="data:image/jpeg;base64,{lasagna_b64}" class="guide-chip-img" />
            <div>
                My mom’s lasagna – even though anything she cooks is perfect.<br>
                She always says cooking is a form of love, because it takes time,
                patience, and focus... but when it’s for the people we love, it just
                comes naturally.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Favorite season (with autumn photo)
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Favorite season</div>
            <img src="data:image/jpeg;base64,{autumn_b64}" class="guide-chip-img" />
            <div>Autumn. Always.</div>
        </div>
    """, unsafe_allow_html=True)

    # Where I'm from (Suzzara)
    # Where I'm from (Suzzara)
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Where I’m from</div>
            <img src="data:image/jpeg;base64,{suzzara_b64}" class="guide-chip-img" />
            <div>
                Suzzara, in the province of Mantua – a small town famous for basically nothing,<br>
                but it’s home. I love it because everything feels calm and slow; you can breathe<br>
                (even if the air is technically kind of polluted, lol), run along the Po river,<br>
                and watch sunsets from the levee. When I’m there, I really embrace the idea of<br>
                the Italian <i>“vita lenta”</i>.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Where I've lived the last 5 years – Milan
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Where I’ve lived the last 5 years</div>
            <img src="data:image/jpeg;base64,{milan_b64}" class="guide-chip-img" />
            <div>
                Milan: big city, a thousand opportunities, chaotic, and always moving fast.<br>
                I had fun, met so many beautiful people, and built friendships I’ll carry for life;<br>
                but it also drained me.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Studies – Politecnico di Milano
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Studies</div>
            <img src="data:image/jpeg;base64,{polimi_b64}" class="guide-chip-img" />
            <div>
                I studied at Politecnico di Milano.<br>
                I studied way too much, honestly, and I’m very grateful to be done with exams.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Family card
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Family</div>
            <img src="data:image/jpeg;base64,{family_b64}" class="guide-chip-img" />
            <div>
                I’m very close to my family and I love them with all my heart.<br>
                They’re my safe place.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Friends card
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Friends</div>
            <img src="data:image/jpeg;base64,{friends_b64}" class="guide-chip-img" />
            <div>
                I would do absolutely anything for my friends, <br>
                and for the people I love in general.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # What I love to do – Sleeping
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">What I love to do</div>
            <img src="data:image/jpeg;base64,{sleep_b64}" class="guide-chip-img" />
            <div>
                Sleeping. My superpower: being able to fall asleep anywhere, in any situation –<br>
                on the floor, in the car, on a plane, on a chair, on a train…
            </div>
        </div>
    """, unsafe_allow_html=True)

    # What I miss – Sister & pizza (two photos)
  # What I miss – Sister & pizza (two photos)
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">What I miss</div>
            <div>
                <img src="data:image/jpeg;base64,{sister_b64}" class="guide-chip-img-half" />
                <img src="data:image/jpeg;base64,{pizza_b64}" class="guide-chip-img-half" />
            </div>
            <div>
                <b>My sister:</b> my favorite person on this planet. She’s brilliant, knows what she wants from life, always has my back, and basically helped raise me.<br><br>
                <b>Pizza:</b> I miss eating it straight from the box, still burning hot, after class in the university garden with a big spritz in my hand.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # Current status
    st.markdown("""
        <div class="guide-chip">
            <div class="guide-chip-label">Current status</div>
            <div>
                Confused but happy, unsure about the future, and absolutely without a well-defined plan (yet). MOOD: CARPE DIEM!
            </div>
        </div>
    """, unsafe_allow_html=True)

    # What my heart cares about
    st.markdown("""
        <div class="guide-chip">
            <div class="guide-chip-label">What my heart cares about right now</div>
            <div>
                Road-tripping across the US, having fun,<br>
                and making the cutest, kindest, sweetest blonde girl very, very happy.<br><br>
                Final goal (for now): kidnapping said Nebraska girl<br>
                with a one-way ticket to Italy (jk… but also not really).
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)

    # Little closing line
    st.markdown(
        "<br><span style='color:#000000; font-style:italic;'>"
        "Work in progress: me, my life, and this whole ‘future’ thing. But at least they told me the guide is cute."
        "</span>",
        unsafe_allow_html=True
    )