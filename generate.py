"""
Author:         Sam LaGrave (github.com/SLaGrave)
Date:           11/01/2020
Last Updated:   11/03/2020
Purpose:        To generate 50k words of text for NaNoGenMo2020
"""

from utils import *
import markdown
from markdown.extensions.toc import TocExtension

TITLE = "Whimsical Forest Field Guide"
AUTHOR = "Sam LaGrave & his code."
DESCRIPTION = 'A field guide to help you identify the "local" flora and fauna. Written for NaNoGenMo 2020.'

NUM_ENTRIES = 20

desc_model = create_flora_markov("flora_texts/desc.txt")
notes_model = create_flora_markov("flora_texts/notes.txt")
place_model = create_flora_markov("flora_texts/place.txt")
time_model = create_flora_markov("flora_texts/time.txt")
virtues_model = create_flora_markov("flora_texts/virtues.txt")
postnotes_model = create_flora_markov("flora_texts/postnotes.txt")

text = "# " + TITLE + "\n - " + AUTHOR + "\n\n" + DESCRIPTION + "\n\n---\n\n[TOC]\n\n"
flora = "## Flora\n---\n"
for i in range(NUM_ENTRIES):
    flora += entry_for_flora(desc_model, notes_model, place_model, time_model, virtues_model, postnotes_model)
    if i != NUM_ENTRIES-1:
        flora += "\n\n---\n"

text += flora

# Style taken from the style used on dillinger.io html export
with open("style.txt", "r") as f:
    style = f.read()
with open("output.html", "w") as f:
    f.writelines(markdown.markdown(text, extensions=[TocExtension(title="Table of Contents")]))
    f.writelines(style)

# with open("output.md", "w", encoding="utf8") as f:
#     f.writelines(entries)

# markdown.markdownFromFile(
#     input='output.md',
#     output='output.html',
#     encoding='utf8',
# )

# with open("style.txt", "r") as s:
#     style = s.read()
# with open("output.html", "a") as f:
#     f.writelines(style)