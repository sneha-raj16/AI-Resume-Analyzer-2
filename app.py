import streamlit as st
import plotly.graph_objects as go

from utils import extract_resume_text
from ai import analyze_resume
from report import generate_pdf



# ===============================
# PAGE CONFIG
# ===============================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)



# ===============================
# LOAD CSS
# ===============================

with open("styles.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )



# ===============================
# SIDEBAR
# ===============================


with st.sidebar:


    st.markdown(
        """
        <h1 style="
        font-size:32px;
        ">
        🤖 ResumeAI
        </h1>

        <p style="
        color:#94a3b8;
        ">
        AI Career Intelligence Platform
        </p>
        """,
        unsafe_allow_html=True
    )


    st.divider()


    st.markdown(
        """
        ### 🚀 Features

        ✅ ATS Score Analysis

        ✅ Resume Optimization

        ✅ Skill Gap Detection

        ✅ Interview Preparation

        ✅ Career Suggestions

        """
    )


    st.divider()


    st.success(
        "🔥 Powered by Llama 3.3 AI"
    )





# ===============================
# HERO SECTION
# ===============================


st.markdown(
"""
<div class="hero-box">


<h1>
AI Resume Analyzer
</h1>


<p>
Transform your resume into an AI-powered career profile.
Get ATS scores, missing skills, improvements and interview preparation.
</p>


</div>

""",
unsafe_allow_html=True
)



st.write("")



# ===============================
# STATS
# ===============================


c1,c2,c3 = st.columns(3)



with c1:

    st.markdown(
    """
    <div class="feature">

    <h3>🎯 ATS Score</h3>

    <p>
    Check how recruiters' systems rank your resume.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



with c2:

    st.markdown(
    """
    <div class="feature">

    <h3>🧠 AI Review</h3>

    <p>
    Get expert-level resume feedback instantly.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



with c3:

    st.markdown(
    """
    <div class="feature">

    <h3>🚀 Career Boost</h3>

    <p>
    Prepare for your next opportunity.
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



st.write("")

# ===============================
# RESUME ANALYSIS WORKSPACE
# ===============================


st.markdown(
"""
<div class="dashboard-header">

<h2>
📄 Resume Analysis Workspace
</h2>

<p>
Upload your resume and let AI evaluate your career profile.
</p>

</div>
""",
unsafe_allow_html=True
)


st.write("")



left,right = st.columns(
    [1,1],
    gap="large"
)



# ===============================
# LEFT UPLOAD CARD
# ===============================


with left:


    st.markdown(
    """
    <div class="glass-card">

    <h3>
    📤 Upload Resume
    </h3>

    <p>
    Supported formats: PDF, DOCX, TXT
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


    uploaded_file = st.file_uploader(
        "",
        type=[
            "pdf",
            "docx",
            "txt"
        ]
    )



    st.write("")



    job_role = st.selectbox(
        "🎯 Target Job Role",

        [
            "AI/ML Engineer",
            "Software Engineer",
            "Data Scientist",
            "Data Analyst",
            "Frontend Developer",
            "Backend Developer",
            "Full Stack Developer",
            "Cloud Engineer"
        ]
    )



    st.write("")



    analyze_btn = st.button(
        "🚀 Analyze Resume With AI",
        use_container_width=True
    )






# ===============================
# RIGHT INFORMATION CARD
# ===============================


with right:


    st.markdown(
    """
    <div class="glass-card">


    <h3>
    🤖 What AI Will Analyze
    </h3>


    <br>


    <p>
    ✨ ATS Compatibility Score
    </p>


    <p>
    ✨ Technical Skill Matching
    </p>


    <p>
    ✨ Missing Keywords
    </p>


    <p>
    ✨ Resume Improvements
    </p>


    <p>
    ✨ Interview Questions
    </p>


    </div>
    """,
    unsafe_allow_html=True
    )





# ===============================
# ANALYSIS PROCESS
# ===============================



if analyze_btn:


    if uploaded_file is None:


        st.warning(
            "Please upload your resume first."
        )


    else:


        with st.spinner(
            "🤖 AI is analyzing your resume..."
        ):


            resume_text = extract_resume_text(
                uploaded_file
            )



            result = analyze_resume(
                resume_text,
                job_role
            )

            st.session_state.analysis = result


            st.session_state.resume_text = resume_text


            st.success(
                "Analysis completed successfully 🚀"
            )


# ===============================
# AI RESULT DASHBOARD
# ===============================


if "analysis" in st.session_state:


    analysis = st.session_state.analysis


    # Safety check
    if isinstance(analysis, str):

        st.error(
            "AI returned invalid response. Please check ai.py JSON formatting."
        )

        st.code(analysis)


        st.stop()



    st.markdown(
    """
    <div class="dashboard-header">

    <h2>
    🧠 AI Resume Intelligence Report
    </h2>

    <p>
    Personalized insights generated by AI
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )


    st.divider()



    # ===============================
    # RESUME SUMMARY
    # ===============================


    st.markdown(
    f"""
    <div class="glass-card">

    <h3>
    📝 AI Resume Summary
    </h3>

    <p>
    {analysis.get(
        "summary",
        "No summary available"
    )}
    </p>

    </div>
    """,
    unsafe_allow_html=True
    )



    st.write("")



    # ===============================
    # SKILLS + IMPROVEMENTS
    # ===============================


    col1,col2 = st.columns(2)



    with col1:


        st.markdown(
        """
        <div class="glass-card">

        <h3>
        🛠 Detected Skills
        </h3>

        """,
        unsafe_allow_html=True
        )


        skills = analysis.get(
            "skills",
            []
        )


        if skills:


            for skill in skills:


                st.success(
                    f"✓ {skill}"
                )


        else:


            st.warning(
                "No skills detected"
            )



        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )




    with col2:


        st.markdown(
        """
        <div class="glass-card">

        <h3>
        💡 Improvement Suggestions
        </h3>

        """,
        unsafe_allow_html=True
        )



        improvements = analysis.get(
            "improvements",
            []
        )


        if improvements:


            for item in improvements:


                st.info(
                    f"→ {item}"
                )


        else:


            st.info(
                "No suggestions available"
            )



        st.markdown(
        "</div>",
        unsafe_allow_html=True
        )




    # ===============================
    # ATS SCORE
    # ===============================


    st.write("")


    st.markdown(
    """
    <div class="dashboard-header">

    <h2>
    🎯 Resume Score
    </h2>

    </div>
    """,
    unsafe_allow_html=True
    )



    score = analysis.get(
        "ats_score",
        0
    )


    try:

        score = int(score)

    except:

        score = 0



    st.progress(
        score / 100
    )


    st.success(
        f"ATS Compatibility Score: {score}%"
    )





    # ===============================
    # IMPROVEMENT PLAN
    # ===============================


    st.markdown(
    """
    <div class="dashboard-header">

    <h2>
    🚀 AI Improvement Plan
    </h2>

    </div>
    """,
    unsafe_allow_html=True
    )



    suggestions = analysis.get(
        "suggestions",
        []
    )



    for suggestion in suggestions:


        st.markdown(
        f"""
        <div class="glass-card">

        🔥 {suggestion}

        </div>

        <br>

        """,
        unsafe_allow_html=True
        )





    # ===============================
    # INTERVIEW QUESTIONS
    # ===============================


    st.markdown(
    """
    <div class="dashboard-header">

    <h2>
    🎤 Interview Preparation
    </h2>

    </div>
    """,
    unsafe_allow_html=True
    )



    questions = analysis.get(
        "interview_questions",
        []
    )



    for index,question in enumerate(
        questions,
        start=1
    ):


        st.markdown(
        f"""
        <div class="glass-card">

        <b>
        Q{index}.
        </b>

        {question}

        </div>

        <br>

        """,
        unsafe_allow_html=True
        )




# ===============================
# FOOTER
# ===============================


st.write("")


st.markdown(
"""
<br>

<div style="
text-align:center;
padding:30px;
border-top:1px solid rgba(255,255,255,.1);
color:#94a3b8;
">


<h3 style="
color:white;
">
🤖 ResumeAI
</h3>


<p>
AI powered career intelligence platform
</p>


<p>
Built with Streamlit • Groq Llama 3.3 • Python
</p>


</div>

""",
unsafe_allow_html=True
)







