import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown

def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

import os
os.environ['GOOGLE_API_KEY']="AIzaSyAmkjiWkiTRY0QBJwsNvCscd3-HAqtXZF4"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

for m in genai.list_models():
  if 'generateContent' in m.supported_generation_methods:
    pass
def model(text):
   model = genai.GenerativeModel('gemini-pro')
   response = model.generate_content(text)
   return response.text