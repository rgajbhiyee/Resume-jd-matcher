import re
import string
from nltk.corpus import stopwords

STOP_WORDS = set(stopwords.words('english'))


def preprocess_text(text):
    if not text:
        return ""

    text = text.lower()

    text = re.sub(r'http\S+|www\S+', ' ', text)

    text = text.translate(str.maketrans('', '', string.punctuation))

    text = re.sub(r'\d+', ' ', text)

    text = re.sub(r'\s+', ' ', text).strip()

    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]

    return " ".join(words)
