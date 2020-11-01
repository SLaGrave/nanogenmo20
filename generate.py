"""
Author:         Sam LaGrave (github.com/SLaGrave)
Date:           11/01/2020
Last Updated:   ---
Purpose:        To generate 50k words of text for NaNoGenMo2020
"""
import random
from pycorpora import plants, colors

# I want the output to be in a nice format. In the future I will likely try
# to use a pdf library, or possibly output LaTeX that can generate nice
# documents. But for now I will just write some html to a file.

# Document constants
TITLE = "Whimsical Forest Field Guide"
AUTHOR = "SLaGrave (and his code)"
DESC = "A field guide to help you survive a magical, whimsical forest."

# Modified a demo from the demo of pycorpora
random_flowers = random.sample(plants.flowers["flowers"], 10)
random_colors = random.sample([item['color'] for item in colors.crayola["colors"]], 10)
flora_test = ""
for p in zip(random_colors, random_flowers):
    pair = p[0] + " " + p[1]
    flora_test += f"{pair}</br>"

# Helper function for the html document
def htmlhelper(tag, data):
    return "<" + tag + ">\n" + data + "\n</" + tag + ">"

# Writes the actual html document
with open("output.html", "w") as f:
    head_title = htmlhelper("title", TITLE)
    head = htmlhelper("head", head_title)

    body_title = htmlhelper("h1", TITLE)
    body_author = htmlhelper("h4", AUTHOR)
    body_desc = htmlhelper("a", DESC)
    body_text = htmlhelper("a", "<br><br><hr><h3>Table of Content:</h3></br>" + flora_test)
    body = htmlhelper("body", body_title + body_author + body_desc + body_text)

    html = htmlhelper("html", head + body)
    f.writelines(html)

word_count = len(TITLE.split(" ")) + len(AUTHOR.split(" ")) + len(DESC.split(" ")) + len(flora_test.split(" "))
print(f"Word Count: {word_count}")