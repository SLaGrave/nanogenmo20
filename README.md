# Whimsical Forest Field Guide
For [NaNoGenMo 2020](https://github.com/NaNoGenMo/2020), I plan on writing code to generate a field guide to help you survive a magical, whimsical forest.

---

The current data was pulled from [this Project Gutenberg entry](https://www.gutenberg.org/ebooks/49513). It has been split up by me.

---

The original plan. This might get changes as I go along
```
Sections on:
 - Author's notes
 - Table of Contents
 - Flora
 - Fauna

---
Entries will consist of 
 - a name
 - text describing the item
 - any warnings about it.

The name will most likely be generated based on a format with specific words pulled from corpuses. The text will likely be markov chain generated (unsure of source). The warnings will periodically added and will most likely be a format filled with specific based on the name and/or key words in the entry.

---
*Stretch goals*: If I complete what I have fast enough and don't want to start another project, I will possibly attempt these extra tasks:
 - NLP
 - Hook the gen script up to processing or blender or another similar software to generate a few plants for artwork throughout the text.
```

---

##### Requirements
[pycorpora](https://github.com/aparrish/pycorpora)

[markovify](https://github.com/jsvine/markovify)

markdown library

I use a style string that I pulled from [dillinger.io](dillinger.io)'s export as html.