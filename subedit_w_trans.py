import re
#You need to install googletrans to use Google Translate API (pypi.org/project/googletrans/)
from googletrans import Translator

#This is your files name without extension (without .srt).
file_name = "1"
#This is the language you want to translate the subtitle file.
destination_language = "tr"
#This is the original language of the subtitle file.
source_language = "en"

def time_to_sec(boolean: bool, time: str):
    if not boolean:
        hrs = int(time[0:2])
        mins = int(time[3:5])
        secs = float(time[6:12].replace(",", "."))
        return hrs*3600 + mins*60 + secs
    elif boolean:
        hrs = int(time[17:19])
        mins = int(time[20:22])
        secs = float(time[23:29].replace(",", "."))
        return hrs*3600 + mins*60 + secs

def sec_to_time(time: float):
    hrs = int(time/3600)
    time = time - hrs*3600
    mins = int(time/60)
    secs = time - mins*60
    previous = "{:02d}".format(hrs) + ":" + "{:02d}".format(mins) + ":" + "{:06.3f}".format(secs)
    return previous.replace(".", ",")

def splitter():
    del_list.clear()
    for x in range(len(texts)):
        punctuation = texts[x].find(".") or texts[x].find("?")
        if punctuation != -1:
            split_lines = re.split(r"(?<=[.?])\s+", texts[x])
            if len(split_lines) == 2:
                part1 = split_lines[0].count(".") + split_lines[0].count("?")
                part2 = split_lines[1].count(".") + split_lines[1].count("?")
                if part1 + part2 < 2:
                    texts[x-1] = texts[x-1] + " " + split_lines[0]
                    texts[x+1] = split_lines[1] + " " + texts[x+1]
                    del_list.append(x)
    for x in sorted(del_list, reverse=True):
        del texts[x]
    splitter_timer()
        
def splitter_timer():
    for x in range(len(del_list)):
        start = time_to_sec(0, times[del_list[x]])
        end = time_to_sec(1, times[del_list[x]])
        previous_end = time_to_sec(1, times[del_list[x]-1])
        next_start = time_to_sec(0, times[del_list[x]+1])
        
        average = ((start - previous_end) + (next_start - end)) / 2
        result = ((end - start) + average) / 2
        times[del_list[x]-1] = times[del_list[x]-1][0:17] + sec_to_time(previous_end + result)
        times[del_list[x]+1] = sec_to_time(next_start - result) + times[del_list[x]+1][12:29]
    for x in sorted(del_list, reverse=True):
        del times[x]
        
def joiner():
    del_list.clear()
    for x in range(len(texts), 0, -1):
        punctuation = texts[x-1].find(".") or texts[x-1].find("?")
        if punctuation == -1:
            texts[x-1] = texts[x-1] + " " + texts[x]
            del_list.append(x)
    for x in del_list:
        del texts[x]
    joiner_timer()

def joiner_timer():
    for x in range(len(del_list)):
        times[del_list[x]-1] = times[del_list[x]-1][0:17] + times[del_list[x]][17:29]
    for x in del_list:
        del times[x]

with open(file_name + ".srt", "r") as f:
    lines = [line.rstrip() for line in f]
    c = 0
    times, texts, del_list = [], [], []
    for line in lines:
        c = c + 1
        if c % 4 == 2:
            times.append(line)
        elif c % 4 == 3:
            texts.append(line)

splitter()
joiner()

file_name = file_name + "_edited"

translator = Translator()

for x in range(len(texts)):
    translated_line = translator.translate(texts[x], dest = destination_language, src = source_language)
    texts[x] = translated_line.text

with open(file_name + ".srt", "w", encoding = "utf-8") as f:
    sub = ""
    for x in range(len(texts)):
        sub = sub + str(x+1) + "\n" + times[x] + "\n" + texts[x] + "\n\n"
    f.write(sub)

print("Done!")
