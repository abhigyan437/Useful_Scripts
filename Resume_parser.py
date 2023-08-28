import nltk
import re
import subprocess
from pdfminer.high_level import extract_text
import requests

nltk.download('punkt')
nltk.download('average_perception_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('stopwords')

def extraxt_pdf(pdf_path):
    return extract_text(pdf_path)

def extract_names(txt):
    person_names = []

    for sent in nltk.sent_tokenize(txt):
        for chukn in nltk.ne_chunk(nltk.pos_tag(nltk.word_tokenize(sent))):
            if hasattr(chunk,'label') and chunk.label()=='PERSON':
                person_names.append(
                    ' '.join(chunk_leave[0] for chunk_leave in chunk.leaves())
                    )
    return person_names

PHONE_REG = re.compile(r'[\+\(]?[1-9][0-9.\-\(\)](8,)[0-9]')

def doc_to_text_catdoc(file_path):
    try:
        process = subprocess.Popen(
            ['catdoc','-w',file_path],
            stdout = subprocess.PIPE,
            stderr = subprocess.PIPE,
            universal_newlines = True,
        )
    except(
        FileNotFoundError,
        ValueError,
        subprocess.TimeoutExpired,
        subprocess.SubprocessError,
    ) as err:
        return (None,str(err))
    else:
        stdout,stderr = process.communicate()
    return (stdout.strip(),stderr.strip())


    
