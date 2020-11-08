"""
Author:         Sam LaGrave (github.com/SLaGrave)
Date:           11/03/2020
Last Updated:   ---
Purpose:        Helper functions used in generate.py
"""
import random
import markovify
from pycorpora import plants, colors

def create_flora_markov(filename):
    with open(filename, encoding="utf8") as f:
        text = f.read()
    return markovify.Text(text)

def entry_for_flora(desc_model, notes_model, place_model, time_model, virtues_model, postnotes_model):
    name = "### " + random.sample([item['color'] for item in colors.crayola["colors"]], 1)[0] + " " + \
        random.sample(plants.flowers["flowers"], 1)[0]
    
    notes = ""
    if random.random() > 0.75:
        for _ in range(random.randint(1, 4)):
            notes += notes_model.make_sentence().capitalize() + " "
    
    desc = ""
    for i in range(random.randint(1, 6)):
        desc += desc_model.make_sentence().capitalize() + " "
    
    place = ""
    for i in range(random.randint(1, 6)):
        place += place_model.make_sentence().capitalize() + " "
    
    time = ""
    for i in range(random.randint(1, 6)):
        time += time_model.make_sentence().capitalize() + " "
    
    virtues = ""
    for i in range(random.randint(1, 6)):
        virtues += virtues_model.make_sentence().capitalize() + " "

    postnotes = ""
    if random.random() > 0.80:
        for _ in range(random.randint(1, 4)):
            postnotes += postnotes_model.make_sentence().capitalize() + " "

    entry = name + "\n\n"
    if notes != "":
        entry += notes + "\n\n"
    entry += "##### Description\n" + desc + "\n\n" + \
        "##### Location\n" + place + "\n\n" + \
        "##### Time\n" + time + "\n\n" + \
        "##### Uses, Behavior, and Traits\n" + virtues
    if postnotes != "":
        entry += "\n\n" + postnotes

    return entry


def entry_for_fauna(name):
    # TODO: Add logic
    return