"""
Author:         Sam LaGrave (github.com/SLaGrave)
Date:           11/01/2020
Last Updated:   11/03/2020
Purpose:        To generate 50k words of text for NaNoGenMo2020
"""

from utils import *

import random

from pycorpora import plants, colors, animals


# I want the output to be in a nice format. In the future I will likely try
# to use a pdf library, or possibly output LaTeX that can generate nice
# documents.

# Document constants
HEADER = """Whimsical Forest Field Guide
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

random_animals = random.sample(animals.common["animals"], 10)
random_colors = random.sample([item['color'] for item in colors.crayola["colors"]], 10)
fauna_test = list()
for p in zip(random_colors, random_animals):
    pair = p[0] + " " + p[1]
    fauna_test.append(pair)

Flora_TOC = [f"\t\t{pair}\n" for pair in flora_test]
Fauna_TOC = [f"\t\t{pair}\n" for pair in fauna_test]

# Writes the actual html document
with open("output.txt", "w") as f:
    f.writelines(HEADER)

    f.writelines("Table of Contents:\n")
    f.writelines("\tFlora\n")
    for line in Flora_TOC:
        f.writelines(line)
    f.writelines("\tFauna\n")
    for line in Fauna_TOC:
        f.writelines(line)

with open("output.txt", "r") as f:
    data = f.read()
print(f"Word Count: {len(data.split())}")