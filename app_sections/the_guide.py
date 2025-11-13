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
            width: 260px;
            height: auto;
            border-radius: 24px;
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
            gap: 2.2rem;
            margin-bottom: 2.5rem;
            margin-top: 1rem;
        }

        .guide-chip {
            background: rgba(255,255,255,0.95);
            border-radius: 18px;
            padding: 1.2rem 1.3rem;
            box-shadow: 0 10px 26px rgba(0,0,0,0.08);
            font-size: 0.95rem;
            color: #000000;
            margin-bottom: 0.4rem;
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

        .guide-chip-img-third {
            width: 32%;
            border-radius: 14px;
            margin-bottom: 0.5rem;
            object-fit: cover;
            max-height: 140px;
            display: inline-block;
        }

        .guide-chip-img-fourth {
            width: 24%;
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
    lasagna_b64   = _get_base64_image(os.path.join("images", "lasagna.jpg"))
    lasagna2_b64  = _get_base64_image(os.path.join("images", "lasagna2.jpg"))
    lasagna3_b64  = _get_base64_image(os.path.join("images", "lasagna3.jpg"))
    lasagna4_b64  = _get_base64_image(os.path.join("images", "lasagna4.jpg"))
    suzzara_b64   = _get_base64_image(os.path.join("images", "suzzara.jpg"))
    suzzara2_b64  = _get_base64_image(os.path.join("images", "suzzara2.jpg"))
    suzzara3_b64  = _get_base64_image(os.path.join("images", "suzzara3.jpg"))
    suzzara4_b64  = _get_base64_image(os.path.join("images", "suzzara4.jpg"))
    suzzara5_b64  = _get_base64_image(os.path.join("images", "suzzara5.jpg"))
    family_b64    = _get_base64_image(os.path.join("images", "family.jpg"))
    friends_b64   = _get_base64_image(os.path.join("images", "friends.jpg"))
    friends2_b64  = _get_base64_image(os.path.join("images", "friends2.jpg"))
    friends3_b64  = _get_base64_image(os.path.join("images", "friends3.jpg"))
    friends4_b64  = _get_base64_image(os.path.join("images", "friends4.jpg"))
    milan_b64     = _get_base64_image(os.path.join("images", "milan.jpg"))
    polimi_b64    = _get_base64_image(os.path.join("images", "polimi.jpg"))
    sleep_b64     = _get_base64_image(os.path.join("images", "sleep.jpg"))
    sleep2_b64    = _get_base64_image(os.path.join("images", "sleep2.jpg"))
    autumn_b64    = _get_base64_image(os.path.join("images", "autumn.jpg"))
    sister_b64    = _get_base64_image(os.path.join("images", "sister.jpg"))
    pizza_b64     = _get_base64_image(os.path.join("images", "pizza.jpg"))
    mountain_b64  = _get_base64_image(os.path.join("images", "mountain.jpg"))
    mountain2_b64 = _get_base64_image(os.path.join("images", "mountain2.jpg"))
    mountain3_b64 = _get_base64_image(os.path.join("images", "mountain3.jpg"))

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

    # Favorite food – now with 4 photos
    st.markdown(f"""
        <div class="guide-chip">
            <div class="guide-chip-label">Favorite food</div>
            <div>
                <img src="data:image/jpeg;base64,{lasagna_b64}" class="guide-chip-img-fourth" />
                <img src="data:image/jpeg;base64,{lasagna2_b64}" class="guide-chip-img-fourth" />
                <img src="data:image/jpeg;base64,{lasagna3_b64}" class="guide-chip-img-fourth" />
                <img src="data:image/jpeg;base64,{lasagna4_b64}" class="guide-chip-img-fourth" />
            </div>
            <div>
                My mom’s lasagna – even though anything she cooks is perfect.<br>
                She always says cooking is a form of love, because it takes time,
                patience, and focus... but when it’s for the people we love, it just
                comes naturally.
            </div>
        </div>
    """, unsafe_allow_html=True)

    # ... (tutto il resto del file – Suzzara, Milan, Friends, Sleep, ecc. – rimane uguale all’ultima versione che ti ho dato)
