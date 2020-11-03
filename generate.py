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
# documents.

# Document constants
HEADER = """
Whimsical Forest Field Guide
SLaGrave (and his code)

A field guide to help you survive a magical, whimsical forest.\n\n
"""

# Modified a demo from the demo of pycorpora
random_flowers = random.sample(plants.flowers["flowers"], 10)
random_colors = random.sample([item['color'] for item in colors.crayola["colors"]], 10)
flora_test = list()
for p in zip(random_colors, random_flowers):
    pair = p[0] + " " + p[1]
    flora_test.append(pair)

# Writes the actual html document
with open("output.txt", "w") as f:
    f.writelines(HEADER)

word_count = len(HEADER.split())
print(f"Word Count: {word_count}")