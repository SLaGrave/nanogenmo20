# Modifies the text in a file to be more generic

with open("base.txt", "r", encoding="utf8") as f:
    data = f.readlines()

desc = list()

for line in data:
    if not ("[Illustration" in line) and not line.startswith("=") and not line.startswith("_") and not line.startswith("("):
        desc.append(line)

desc = [line.replace("\n", " ").replace("_", "") for line in desc]

with open("cleaned.txt", "w", encoding="utf8") as f:
    f.writelines(desc)