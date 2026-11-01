"""
Happy Birthday web app (Streamlit)
Run locally:   pip install -r requirements.txt   then   streamlit run app.py
"""
import html
import os

import streamlit as st

# ===================== EDIT THESE =====================
CONFIG = {
    "name": "นายณรงค์ชัย จารุทรัพย์สดใส",
    "from": "จากน้องที่น่ารักที่สุด",
    "title": "พี่ชายยอดเยี่ยมแห่งปี",
    # (emoji, award title, short description)
    "awards": [
        ("🍜", "รางวัลเลี้ยงข้าวใจป้ำ", "เลี้ยงน้องบ่อยที่สุดในโลก"),
        ("🛡️", "รางวัลฮีโร่ประจำบ้าน", "มีปัญหาอะไรพี่ช่วยได้เสมอ"),
        ("😂", "รางวัลสายซับยอดเยี่ยม", "ขอบคุณที่คอยซับพอร์ตน้องคนนี้"),
        ("🧠", "รางวัลที่ปรึกษาสุดเจ๋ง", "ให้คำแนะนำดีกว่าใครทั้งนั้น"),
    ],
    "letter": (
        "ถึงพี่ชายที่รัก\n\n"
        "ขอบคุณที่เป็นพี่ชายที่ดีของน้องมาตลอด ขอบคุณที่คอยซับพอร์ตกันเสมอมา "
        "และตอนที่อยู่ข้าง ๆ กันในวันที่ลำบาก\n\n"
        "ปีนี้ขอให้พี่แป็กสุขภาพแข็งแรง หล่อวันหล่อคืน และมีแต่เรื่องดี ๆ เข้ามานะ\n"
        "คิดสิ่งใดขอให้สมปรารถนา มีความสุขมากๆเด้อ \n\n"
        "Happy Birthday to my lovely brother. \n\n"
        "รักพี่เสมอ\nจากน้องคนนี้\n\n"

        "Ps. I'll always by your side. สุขสันต์วันเกิดนะค้าา"
    ),
    "photo": "brother.jpg",  # optional: put a photo with this name next to app.py (jpg/png)
    "caption": "พี่ชายที่น่าร้ากกก 💙",
}
# ======================================================

st.set_page_config(page_title="สุขสันต์วันเกิด 🎂", page_icon="🎂", layout="centered")

st.markdown(
    """<style>
.block-container{max-width:560px;padding-top:2rem}
.hero{text-align:center;font-size:2.3rem;line-height:1.3;margin:.2rem 0 .4rem;font-weight:700}
.hero span{color:#ff7a1a}
.sub{text-align:center;color:#4f6580;margin:0 0 .4rem}
.cake{width:260px;max-width:80%;margin:0 auto;display:block}
.flame{transform-origin:center bottom;transform-box:fill-box;animation:flick .5s infinite alternate ease-in-out}
@keyframes flick{from{transform:scale(1,1) rotate(-3deg)}to{transform:scale(.9,1.12) rotate(3deg)}}
.cert{background:#fff;border:3px double #f5b324;border-radius:16px;padding:22px 16px;text-align:center;box-shadow:0 8px 30px rgba(0,0,0,.1)}
.cert .t{color:#d9a00f;font-weight:700}
.cert .who{font-size:1.7rem;font-weight:700;color:#ff7a1a}
.award{background:#fff;border:2px solid #1fa3a3;border-radius:16px;padding:14px 10px;text-align:center;min-height:120px}
.award b{font-size:1.6rem;display:block}
.award small{color:#4f6580}
.letter{background:#fff;border:1px solid #cfe0f5;border-radius:16px;padding:18px;white-space:pre-line}
div.stButton>button{border-radius:999px;font-weight:700;width:100%}
</style>""",
    unsafe_allow_html=True,
)

ss = st.session_state
ss.setdefault("blown", False)
ss.setdefault("opened", [])


def blow():
    ss.blown = True
    ss.celebrate = True


def open_award(i):
    if i not in ss.opened:
        ss.opened = ss.opened + [i]
    ss.just = i


def reset():
    ss.blown, ss.opened = False, []


def cake_svg(lit):
    flames = ""
    if lit:
        flames = "".join(
            f'<path class="flame" style="animation-delay:{d}s" d="M{x} {y}c-9-9-3-18 0-26 3 8 9 17 0 26z" fill="#f5b324"/>'
            for x, y, d in ((93, 62, 0), (130, 54, .15), (167, 62, .3))
        )
    return (
        '<svg class="cake" viewBox="0 0 260 250" xmlns="http://www.w3.org/2000/svg">'
        '<ellipse cx="130" cy="228" rx="120" ry="14" fill="#000" opacity=".12"/>'
        '<rect x="30" y="150" width="200" height="74" rx="14" fill="#5fc4c4" stroke="#1fa3a3" stroke-width="3"/>'
        '<rect x="50" y="108" width="160" height="50" rx="12" fill="#ffd9b8"/>'
        '<path d="M50 124q10 22 20 0t20 0 20 0 20 0 20 0 20 0 20 0v-6a12 12 0 0 0-12-10H62a12 12 0 0 0-12 10z" fill="#fff6ec"/>'
        '<circle cx="75" cy="188" r="6" fill="#fff6ec"/><circle cx="130" cy="196" r="6" fill="#fff6ec"/>'
        '<circle cx="185" cy="188" r="6" fill="#fff6ec"/>'
        '<rect x="88" y="66" width="10" height="44" rx="3" fill="#ff7a1a"/>'
        '<rect x="125" y="58" width="10" height="52" rx="3" fill="#f5b324"/>'
        '<rect x="162" y="66" width="10" height="44" rx="3" fill="#8fb8ff"/>'
        f"{flames}</svg>"
    )


esc = html.escape
st.markdown(f"<p class='sub'>{esc(CONFIG['from'])}</p>", unsafe_allow_html=True)
st.markdown(
    f"<div class='hero'>สุขสันต์วันเกิด<br><span>{esc(CONFIG['name'])}</span> 🎉</div>",
    unsafe_allow_html=True,
)

if not ss.blown:
    st.markdown("<p class='sub'>มีของขวัญเล็ก ๆ รออยู่ ต้องเป่าเทียนก่อนนะ!</p>", unsafe_allow_html=True)
st.markdown(cake_svg(lit=not ss.blown), unsafe_allow_html=True)

if not ss.blown:
    st.button("🕯️ เป่าเทียน", on_click=blow, type="primary")
else:
    if ss.pop("celebrate", False):
        st.balloons()
    st.markdown("<p class='sub'>🎂 สุขสันต์วันเกิด! ขอให้สมหวังทุกอย่างนะ</p>", unsafe_allow_html=True)

    st.markdown(
        f"<div class='cert'><div class='t'>🏆 ใบประกาศเกียรติคุณ 🏆</div>"
        f"<p style='margin:6px 0;color:#4f6580'>ขอมอบรางวัลนี้ให้</p>"
        f"<div class='who'>{esc(CONFIG['name'])}</div>"
        f"<p style='margin:0'>ในฐานะ {esc(CONFIG['title'])}</p></div>",
        unsafe_allow_html=True,
    )

    st.subheader("🎖️ รางวัลพิเศษประจำตัวพี่")
    st.caption("แตะการ์ดเพื่อเปิดรางวัล")
    if (j := ss.pop("just", None)) is not None:
        st.toast(f"{CONFIG['awards'][j][0]} {CONFIG['awards'][j][1]}")
    cols = st.columns(2)
    for i, (icon, title, desc) in enumerate(CONFIG["awards"]):
        with cols[i % 2]:
            if i in ss.opened:
                st.markdown(
                    f"<div class='award'><b>{icon}</b><strong>{esc(title)}</strong><br><small>{esc(desc)}</small></div>",
                    unsafe_allow_html=True,
                )
            else:
                st.button("🎁 แตะเพื่อเปิด", key=f"award{i}", on_click=open_award, args=(i,))

    photo = os.path.join(os.path.dirname(os.path.abspath(__file__)), CONFIG["photo"])
    if os.path.exists(photo):
        st.subheader("📷  Your are the best brother ever")
        st.image(photo, caption=CONFIG["caption"], use_container_width=True)

    st.subheader("💌 ข้อความจากน้อง")
    st.markdown(f"<div class='letter'>{esc(CONFIG['letter'])}</div>", unsafe_allow_html=True)
    st.caption("ทำด้วยความรัก ❤️")
    st.button("🔄 เป่าเทียนอีกครั้ง", on_click=reset)