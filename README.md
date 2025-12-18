# Smart Resume–Job Description Matcher

A lightweight NLP-based application that analyzes how well a resume matches a job description by computing textual similarity and identifying skill gaps.

## Problem Statement

Recruiters often receive hundreds of resumes for a single role. Manually assessing resume relevance against job descriptions is time-consuming and subjective. This project aims to automate resume–JD matching using interpretable NLP techniques.

## Approach

1. Extract resume text (PDF upload or manual input)
2. Clean and preprocess text (lowercasing, stopword removal)
3. Compute resume–JD similarity using TF-IDF and cosine similarity
4. Perform rule-based skill extraction to identify matched and missing skills

Due to inherent limitations of PDF parsing for multi-column resumes, the system supports manual text input for improved accuracy.

## Tech Stack

- Python
- Streamlit
- scikit-learn
- NLTK
- PyPDF2

## Features

- Resume–JD similarity scoring
- Skill gap analysis (matched & missing skills)
- Interactive web interface
- Robust handling of generic job descriptions


## How to Run

```bash
python -m pip install -r requirements.txt
python -m streamlit run app.py
```
