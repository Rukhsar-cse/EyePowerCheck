import streamlit as st

st.set_page_config(
    page_title="EyePowerCheck",
    page_icon="👁️",
    layout="wide"
)

# ---------- CSS ----------
st.markdown("""
<style>
.stApp {
    background-color: #f5f9fc;
}

.hero {
    padding: 70px 8% 40px 8%;
}

.tag {
    color: #087f8c;
    font-size: 14px;
    font-weight: bold;
    letter-spacing: 2px;
}

.title {
    font-size: 55px;
    font-weight: 800;
    color: #102a43;
    line-height: 1.1;
    margin-top: 15px;
}

.highlight {
    color: #087f8c;
}

.description {
    font-size: 18px;
    color: #627d98;
    max-width: 650px;
    line-height: 1.7;
}

.card {
    background: white;
    padding: 35px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.06);
    text-align: center;
}

.section-title {
    font-size: 38px;
    font-weight: bold;
    color: #102a43;
}

.disclaimer {
    color: #829ab1;
    font-size: 13px;
}
</style>
""", unsafe_allow_html=True)


# ---------- SESSION ----------
if "page" not in st.session_state:
    st.session_state.page = "home"


def go_to(page):
    st.session_state.page = page


# ==================================================
# HOME
# ==================================================

if st.session_state.page == "home":

    st.markdown("""
    <div class="hero">

        <div class="tag">
            SMART EYESIGHT SCREENING
        </div>

        <div class="title">
            Check your vision.<br>
            <span class="highlight">From anywhere.</span>
        </div>

        <p class="description">
            EyePowerCheck is a digital preliminary eyesight
            screening system designed to help users perform
            a simple vision check using their device.
        </p>

    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.4, 0.8])

    with col1:

        if st.button("Start Eye Check →", type="primary"):
            go_to("instructions")
            st.rerun()

        st.markdown("""
        <p class="disclaimer">
        ⚠️ This is a preliminary screening tool and not
        a substitute for a professional eye examination.
        </p>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card">

            <div style="font-size:90px;">
                👁️
            </div>

            <h2>Your vision matters.</h2>

            <p>
                Let's perform a quick screening.
            </p>

        </div>
        """, unsafe_allow_html=True)


# ==================================================
# INSTRUCTIONS
# ==================================================

elif st.session_state.page == "instructions":

    st.markdown(
        '<div class="tag">STEP 01</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Before we begin</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Follow these instructions for a better screening experience."
    )

    col1, col2 = st.columns(2)

    with col1:
        st.info("""
        📱 **Keep your device steady**

        Place your phone or laptop in a stable position.
        """)

        st.info("""
        📏 **Maintain the recommended distance**

        Position yourself at the distance shown by the system.
        """)

    with col2:
        st.info("""
        💡 **Good lighting**

        Make sure your face is clearly visible.
        """)

        st.info("""
        👓 **Follow the test instructions**

        Follow each instruction carefully during the screening.
        """)

    if st.button("Continue →", type="primary"):
        go_to("camera")
        st.rerun()

    if st.button("← Back"):
        go_to("home")
        st.rerun()


# ==================================================
# CAMERA
# ==================================================

elif st.session_state.page == "camera":

    st.markdown(
        '<div class="tag">STEP 02</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Position yourself</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Position yourself correctly before starting the eye test."
    )

    st.info(
        "📷 Camera functionality will be connected in the next step."
    )

    st.markdown("""
    <div class="card">

        <div style="font-size:80px;">
            🙂
        </div>

        <h2>Camera Preview</h2>

        <p>
            Your camera preview will appear here.
        </p>

    </div>
    """, unsafe_allow_html=True)

    if st.button("Begin Eye Test →", type="primary"):
        go_to("test")
        st.rerun()

    if st.button("← Back"):
        go_to("instructions")
        st.rerun()


# ==================================================
# EYE TEST
# ==================================================

elif st.session_state.page == "test":

    st.markdown(
        '<div class="tag">STEP 03</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Visual Acuity Test</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Look at the character and select the option that matches what you see."
    )

    st.markdown("""
    <div class="card">

        <div style="font-size:150px;font-weight:bold;">
            E
        </div>

    </div>
    """, unsafe_allow_html=True)

    answer = st.radio(
        "Which character do you see?",
        ["E", "F", "P", "T"],
        horizontal=True
    )

    if st.button("Submit Answer →", type="primary"):
        go_to("result")
        st.rerun()

    if st.button("← Back"):
        go_to("camera")
        st.rerun()


# ==================================================
# RESULT
# ==================================================

elif st.session_state.page == "result":

    st.markdown(
        '<div class="tag">SCREENING COMPLETE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-title">Your screening is complete</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Your preliminary result has been generated."
    )

    st.markdown("""
    <div class="card">

        <div style="font-size:60px;">
            ✓
        </div>

        <h2>Preliminary Result</h2>

        <h1 style="color:#087f8c;">
            Normal Range
        </h1>

        <p>
            This is currently a demonstration result.
            The actual screening algorithm will be connected later.
        </p>

    </div>
    """, unsafe_allow_html=True)

    st.warning(
        "This is not a medical diagnosis. "
        "Consult an eye-care professional for an accurate examination."
    )

    if st.button("Back to Home", type="primary"):
        go_to("home")
        st.rerun()