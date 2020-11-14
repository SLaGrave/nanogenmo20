"""
Author:         Sam LaGrave (github.com/SLaGrave)
Date:           11/01/2020
Last Updated:   11/03/2020
Purpose:        To generate 50k words of text for NaNoGenMo2020
"""

from utils import *
import random
import markdown
from markdown.extensions.toc import TocExtension

TITLE = "Whimsical Forest Field Guide"
DESCRIPTION = 'A field guide to help you identify the "local" flora and fauna. Written for NaNoGenMo 2020.\n\n'

with open("intros.txt", encoding="utf8") as f:
        text = f.read()
intro_model = markovify.Text(text)
intro = ""
for _ in range(random.randint(5, 12)):
    try:
        intro += intro_model.make_sentence().capitalize() + " "
    except AttributeError:
        pass

DESCRIPTION += intro


NUM_ENTRIES_FAUNA = 100
NUM_ENTRIES_FLORA = 75

desc_model = create_flora_markov("flora_texts/desc.txt")
notes_model = create_flora_markov("flora_texts/notes.txt")
place_model = create_flora_markov("flora_texts/place.txt")
time_model = create_flora_markov("flora_texts/time.txt")
virtues_model = create_flora_markov("flora_texts/virtues.txt")
postnotes_model = create_flora_markov("flora_texts/postnotes.txt")

fauna_model = create_fauna_markov("fauna_texts/cleaned.txt")

text = "# " + TITLE + "\n\n" + DESCRIPTION + "\n\n---\n\n[TOC]\n\n"

fauna = "## Fauna\n---\n"
for i in range(NUM_ENTRIES_FAUNA):
    fauna += entry_for_fauna(fauna_model)
    if i != NUM_ENTRIES_FLORA-1:
        fauna += "\n\n---\n"

flora = "## Flora\n---\n"
for i in range(NUM_ENTRIES_FLORA):
    flora += entry_for_flora(desc_model, notes_model, place_model, time_model, virtues_model, postnotes_model)
    if i != NUM_ENTRIES_FLORA-1:
        flora += "\n\n---\n"

text += flora + "\n"
text += fauna

# Style taken from the style used on dillinger.io html export
with open("style.txt", "r") as f:
    style = f.read()
with open("output.html", "w") as f:
    f.writelines(markdown.markdown(text, extensions=[TocExtension(title="Table of Contents", toc_depth=3)]))
    f.writelines(style)

l = len(DESCRIPTION.split()) + len(fauna.split()) + len(flora.split())
print(f"Approx. word count: {l}\n*True word count is likely slightly less")