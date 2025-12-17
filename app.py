import streamlit as st

from utils.text_extraction import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.similarity import compute_similarity
from utils.skills import compare_skills


st.set_page_config(page_title="Resume–JD Matcher", layout="centered")

st.title("Smart Resume–Job Description Matcher")
st.write(
    "Analyze how well a resume matches a job description using NLP-based similarity "
    "and skill gap analysis."
)

st.divider()

# --- Resume Input ---
st.subheader("Resume Input")

resume_pdf = st.file_uploader(
    "Upload Resume (PDF) — optional",
    type=["pdf"]
)

resume_text_input = st.text_area(
    "Or paste resume text (recommended for accuracy):",
    height=180,
    placeholder="Paste full resume text here..."
)

st.divider()

# --- Job Description Input ---
st.subheader("Job Description")

jd_text_input = st.text_area(
    "Paste the job description:",
    height=200,
    placeholder="Paste job description here..."
)

st.divider()

# --- Action ---
analyze_clicked = st.button("Analyze")

# --- Processing ---
if analyze_clicked:
    resume_text = ""

    if resume_text_input.strip():
        resume_text = resume_text_input
    elif resume_pdf is not None:
        resume_text = extract_text_from_pdf(resume_pdf)

    if not resume_text.strip():
        st.error("Please upload a resume PDF or paste resume text.")
        st.stop()

    if not jd_text_input.strip():
        st.error("Please paste the job description.")
        st.stop()

    resume_clean = preprocess_text(resume_text)
    jd_clean = preprocess_text(jd_text_input)

    similarity_score = compute_similarity(resume_clean, jd_clean)
    matched_skills, missing_skills = compare_skills(resume_clean, jd_clean)

    st.success("Analysis Complete")

    st.subheader("Resume–JD Similarity")
    st.metric(label="Match Percentage", value=f"{similarity_score}%")

    st.subheader("Matched Skills")
    if matched_skills:
        st.write(", ".join(sorted(matched_skills)))
    else:
        st.write("No matched skills found.")

    st.subheader("Missing Skills (present in JD but not in Resume)")
    if missing_skills:
        st.write(", ".join(sorted(missing_skills)))
    else:
        st.write("No missing skills 🎉")
