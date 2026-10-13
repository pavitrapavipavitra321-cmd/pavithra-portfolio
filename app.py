
import streamlit as st
from pathlib import Path
import base64
import streamlit.components.v1 as components


# --------------------------------------------------
# PAGE SETTINGS
# --------------------------------------------------

st.set_page_config(
    page_title="Pavithra GV | Portfolio",
    page_icon="👩‍💻",
    layout="wide"
)


# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown("""
<style>

.main-title {
    font-size: 48px;
    font-weight: 700;
    color: #16823B;
    margin-bottom: 5px;
}

.subtitle {
    font-size: 22px;
    color: #555555;
    margin-bottom: 20px;
}

.section-title {
    font-size: 30px;
    font-weight: 600;
    color: #16823B;
    border-bottom: 2px solid #16823B;
    padding-bottom: 8px;
    margin-top: 35px;
    margin-bottom: 20px;
}

.skill-box {
    padding: 15px;
    border: 1px solid #dddddd;
    border-radius: 10px;
    text-align: center;
    margin-bottom: 10px;
    font-size: 17px;
}

.project-box {
    padding: 20px;
    border: 1px solid #dddddd;
    border-radius: 10px;
    margin-bottom: 15px;
}

</style>
""", unsafe_allow_html=True)


# Navigation Menu

st.markdown("""
<div style="
    text-align: center;
    padding: 12px;
    margin-bottom: 25px;
    border-bottom: 1px solid #dddddd;
">
    <a href="#about-me" style="margin: 0 18px; text-decoration: none; color: #16823B;">
        About
    </a>
    <a href="#skills" style="margin: 0 18px; text-decoration: none; color: #16823B;">
        Skills
    </a>
    <a href="#projects" style="margin: 0 18px; text-decoration: none; color: #16823B;">
        Projects
    </a>
    <a href="#education" style="margin: 0 18px; text-decoration: none; color: #16823B;">
        Education
    </a>
    <a href="#certifications" style="margin: 0 18px; text-decoration: none; color: #16823B;">
        Certifications
    </a>
    <a href="#contact" style="margin: 0 18px; text-decoration: none; color: #16823B;">
        Contact
    </a>
</div>
""", unsafe_allow_html=True)


# --------------------------------------------------
# HEADER WITH PROFILE PHOTO
# --------------------------------------------------

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown(
        """
        <style>
        div[data-testid="stImage"] img {
            border-radius: 50%;
            width: 180px;
            height: 180px;
            object-fit: cover;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.image("images/profile.jpg", width=180)

with col2:
    st.markdown(
        '<div class="main-title">Pavithra G V</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="subtitle">'
        'Artificial Intelligence & Machine Learning Student'
        '</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Passionate about Python, Artificial Intelligence, "
        "Machine Learning and building practical projects."
    )


col1, col2 = st.columns(2)

with col1:
    st.link_button(" View My Projects", "#projects")

with col2:
    st.link_button(" Contact Me", "#contact")


st.divider()

# --------------------------------------------------
# ABOUT ME
# --------------------------------------------------

st.markdown(
    '<div class="section-title">About Me</div>',
    unsafe_allow_html=True
)

st.write(
    "I am currently pursuing Artificial Intelligence and Machine Learning. "
    "I enjoy learning Python, Machine Learning and developing practical projects. "
    "I am interested in improving my technical skills and working on real-world problems."
)


# --------------------------------------------------
# SKILLS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Skills</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div class="skill-box"> C Programming</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="skill-box">Python</div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div class="skill-box"> Java</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="skill-box">Data Structures</div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div class="skill-box"> Artificial Intelligence</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="skill-box"> DBMS</div>',
        unsafe_allow_html=True
    )


# --------------------------------------------------
# PROJECTS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Projects</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Student Performance Prediction")
    st.write(
        "A Machine Learning project that predicts student performance "
        "using academic and related features."
    )
    st.caption("Python • Machine Learning")

with col2:
    st.markdown("### Disease Prediction")
    st.write(
        "A Machine Learning project for disease prediction "
        "using medical datasets."
    )
    st.caption("Python • Machine Learning")

col3, col4 = st.columns(2)

with col3:
    st.markdown("### FarmGrid")
    st.write(
        "A smart agriculture platform designed to connect farmers "
        "with useful services and support."
    )
    st.caption("Ongoing Project")


# --------------------------------------------------
# EDUCATION
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Education</div>',
    unsafe_allow_html=True
)

st.markdown("### Bachelor of Engineering")

st.write(
    "**Artificial Intelligence and Machine Learning**"
)

st.write(
    "Jawaharlal Nehru New College of Engineering, shivamogga"
)

st.write(
    "CGPA: 9.3"
)

# --------------------------------------------------
# HACKATHONS
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Hackathons</div>',
    unsafe_allow_html=True
)

st.markdown("### NEXORA '26 Hackathon")
st.caption("National Level Spectrum · Participation")

st.write(
    "Participated in NEXORA '26 Hackathon, organized by "
    "Byte Brigade Club at Jawaharlal Nehru New College of "
    "Engineering on 10th and 11th September 2026."
)

st.markdown("---")

st.markdown("### Smart India Hackathon (SIH) 2026")
st.caption("College-Level Internal Round")

st.write(
    "Cleared the college internal round with Team Go-Gitters. "
    "Worked on an AI-based Smart Governance & Compliance "
    "Monitoring System for Coal Mines."
)


# =========================================================
# CERTIFICATIONS
# =========================================================

st.markdown("""
<style>

/* Green View and Hide buttons */
div.stButton > button {
    background-color: #16823B;
    color: white;
    border: 1px solid #16823B;
    border-radius: 8px;
    font-weight: 600;
}

div.stButton > button:hover {
    background-color: #10652D;
    color: white;
    border: 1px solid #10652D;
}

/* Certificate images: rectangular, not circular */
div[data-testid="stImage"] img {
    border-radius: 0 !important;
    object-fit: contain !important;
}

</style>
""", unsafe_allow_html=True)


st.markdown(
    '<div id="certifications" class="section-title">Certifications</div>',
    unsafe_allow_html=True
)


# Certificates folder
certificate_folder = Path(__file__).resolve().parent / "certifications"


# NEW: Zoomable certificate display
def show_zoomable_certificate(certificate_path, title):

    with open(certificate_path, "rb") as file:
        image_data = base64.b64encode(file.read()).decode("utf-8")

    if certificate_path.suffix.lower() == ".png":
        image_type = "image/png"
    else:
        image_type = "image/jpeg"

    components.html(
        f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <style>
                body {{
                    margin: 0;
                    padding: 8px;
                    font-family: Arial, sans-serif;
                }}

                .toolbar {{
                    display: flex;
                    gap: 8px;
                    justify-content: center;
                    margin-bottom: 12px;
                    flex-wrap: wrap;
                }}

                .toolbar button {{
                    background-color: #16823B;
                    color: white;
                    border: none;
                    border-radius: 6px;
                    padding: 8px 16px;
                    cursor: pointer;
                    font-size: 14px;
                }}

                .toolbar button:hover {{
                    background-color: #10652D;
                }}

                .image-area {{
                    width: 100%;
                    height: 560px;
                    overflow: auto;
                    border: 1px solid #dddddd;
                    background: #f5f5f5;
                    text-align: center;
                }}

                #certificate {{
                    display: block;
                    width: 100%;
                    max-width: none;
                    height: auto;
                    margin: 0 auto;
                    transform-origin: top left;
                }}
            </style>
        </head>

        <body>

            <div class="toolbar">
                <button onclick="zoomIn()">Zoom +</button>
                <button onclick="zoomOut()">Zoom −</button>
                <button onclick="fitImage()">Fit</button>
            </div>

            <div class="image-area" id="imageArea">
                <img
                    id="certificate"
                    src="data:{image_type};base64,{image_data}"
                    alt="Certificate"
                >
            </div>

            <script>
                const image = document.getElementById("certificate");
                const area = document.getElementById("imageArea");

                let zoom = 1;

                function applyZoom() {{
                    image.style.width = (area.clientWidth * zoom) + "px";
                    image.style.maxWidth = "none";
                }}

                function zoomIn() {{
                    zoom = Math.min(zoom + 0.25, 3);
                    applyZoom();
                }}

                function zoomOut() {{
                    zoom = Math.max(zoom - 0.25, 0.5);
                    applyZoom();
                }}

                function fitImage() {{
                    zoom = 1;
                    area.scrollTop = 0;
                    area.scrollLeft = 0;
                    applyZoom();
                }}

                image.onload = function() {{
                    fitImage();
                }};

                window.addEventListener("resize", function() {{
                    applyZoom();
                }});
            </script>

        </body>
        </html>
        """,
        height=650,
        scrolling=False
    )


def certificate_row(filename, title, key):

    certificate_path = certificate_folder / filename
    state_key = "show_" + key

    if state_key not in st.session_state:
        st.session_state[state_key] = False

    col1, col2 = st.columns([5, 1])

    with col1:
        st.write(" " + title)

    with col2:
        button_text = "Hide" if st.session_state[state_key] else "View"

        if st.button(button_text, key=key):
            st.session_state[state_key] = not st.session_state[state_key]

    # Display the selected certificate
    if st.session_state[state_key]:

        if certificate_path.exists():

            st.markdown(
                f"### {title}",
                unsafe_allow_html=True
            )

            # NEW: Show certificate with Zoom +, Zoom − and Fit
            show_zoomable_certificate(certificate_path, title)

        else:
            st.error(
                "Certificate not found: " + str(certificate_path)
            )


# 1. MongoDB Basics for Students
certificate_row(
    "mongodb_basics.jpeg",
    "MongoDB Basics for Students",
    "view_mongodb_basics"
)


# 2. Building RAG Apps Using MongoDB
certificate_row(
    "mongodb_rag.jpeg",
    "Building RAG Apps Using MongoDB",
    "view_mongodb_rag"
)


# 3. Building AI Agents with MongoDB
certificate_row(
    "mongodb_agents.jpeg",
    "Building AI Agents with MongoDB",
    "view_mongodb_agents"
)


# 4. AI and Innovation
certificate_row(
    "mongodb_ai_innovation.jpeg",
    "AI and Innovation: How MongoDB Enables a Resilient AI Strategy",
    "view_mongodb_innovation"
)


# 5. MongoDB Vector Search
certificate_row(
    "mongodb_vector_search.jpeg",
    "Building AI-powered Search with MongoDB Vector Search",
    "view_mongodb_vector_search"
)


# 6. Introduction to Deep Learning
certificate_row(
    "deep_learning.jpeg",
    "Introduction to Deep Learning",
    "view_deep_learning"
)


# 7. Generative AI Foundations
certificate_row(
    "generative_ai.jpeg",
    "Generative AI Foundations",
    "view_generative_ai"
)


# 8. Introduction to Python
certificate_row(
    "python.jpeg",
    "Introduction to Python",
    "view_python"
)


# --------------------------------------------------
# CONTACT
# --------------------------------------------------

st.markdown(
    '<div class="section-title">Contact</div>',
    unsafe_allow_html=True
)


st.markdown(
    "**GitHub:** [Visit my GitHub](https://github.com/pavitrapavipavitra321-cmd)"
)


st.markdown(
    "**LinkedIn:** [Visit my LinkedIn](https://www.linkedin.com/in/pavithra-g-v-0813903a2/)"
)

st.markdown(
    "**Email:** [pavitrapavipavitra321@gmail.com](mailto:pavitrapavipavitra321@gmail.com)"
)

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    """
    <div style="
        text-align: center;
        padding: 15px;
        color: #666666;
        font-size: 14px;
    ">
        <b>Pavithra G V</b><br>
        Artificial Intelligence & Machine Learning Student<br>
        © 2026 Pavithra GV
    </div>
    """,
    unsafe_allow_html=True
)
