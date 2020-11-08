# Modifies the text in a file to be more generic

def extra(line):
    if "." in line and not ". " in line:
        line.replace(".", ". ")
    return line

with open("base.txt", "r", encoding="utf8") as f:
    data = f.read()

data = data.split("\n\n")
data = [extra(d.replace("\n", " ")) for d in data]

TITLES = list()
NOTES = list()
DESC = list()
PLACE = list()
TIME = list()
VIRTUES = list()
POSTNOTES = list()

last = ""
for i in range(len(data)):
    s = data[i]
    if "[TITLE]" in s:
        TITLES.append(s)
    elif "[TITLE]" in last and not "[DESC]" in s:
        NOTES.append(s)
    elif "[DESC]" in s:
        DESC.append(s)
    elif "[PLACE]" in s:
        PLACE.append(s)
    elif "[TIME]" in s:
        TIME.append(s)
    elif "[VIRTUES]" in s:
        VIRTUES.append(s)
    elif "[VIRTUES]" in last and not "[TITLE]" in s:
        POSTNOTES.append(s)
    else:
        pass
        # print("oh no")

    last = s


def r(line, text):
    return line.replace(text, "")


with open("notes.txt", "w", encoding="utf8") as f:
    f.writelines([r(l, "") for l in NOTES])

with open("desc.txt", "w", encoding="utf8") as f:
    f.writelines([r(l, "[DESC]") for l in DESC])

with open("place.txt", "w", encoding="utf8") as f:
    f.writelines([r(l, "[PLACE]") for l in PLACE])

with open("time.txt", "w", encoding="utf8") as f:
    f.writelines([r(l, "[TIME]") for l in TIME])

with open("virtues.txt", "w", encoding="utf8") as f:
    f.writelines([r(l, "[VIRTUES]") for l in VIRTUES])

with open("postnotes.txt", "w", encoding="utf8") as f:
    f.writelines([r(l, "") for l in POSTNOTES])