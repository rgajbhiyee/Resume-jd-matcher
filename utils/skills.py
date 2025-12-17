SKILL_LIST = [
    # Programming Languages
    "python", "c", "c++", "java", "javascript",

    # CS Fundamentals
    "data structures", "algorithms", "operating systems",
    "computer networks", "dbms", "database",

    # Tools & Tech
    "git", "github", "linux", "sql",

    # ML / Data
    "machine learning", "data analysis", "statistics",
    "numpy", "pandas", "scikit learn",

    # Web (basic)
    "html", "css", "react", "node"
]

def extract_skills(text):
    """
    Extracts skills present in the given text
    based on predefined SKILL_LIST.
    """
    found_skills = set()

    for skill in SKILL_LIST:
        if skill in text:
            found_skills.add(skill)

    return found_skills


def compare_skills(resume_text, jd_text):
    """
    Compares resume skills with JD skills.
    Returns matched and missing skills.
    """
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    matched_skills = resume_skills.intersection(jd_skills)
    missing_skills = jd_skills.difference(resume_skills)

    return matched_skills, missing_skills

