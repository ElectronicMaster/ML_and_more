import re
from pathlib import Path

path = Path("D:\\GitHub\\Natural_Language_Processing\\Regular_Expression\\text.txt")
with path.open(encoding="utf-8") as file:
    text = file.read()

# pattern = '\(\d{3}\) \d{3}-\d{4}'
# pattern = 'E.o.'
# pattern = 'E.o\w'

pattern = 'Note \d – ([^\n]+)'

# + -> capture everything one or more preceding character
# [^] -> do not capture the match
# (...) -> capture elements withing brackets 

matches = re.findall(pattern,text)
print("text 1")
for match in matches:
    print(match)

print("text 2")
text = "FY2020 Q4 fy2024 sadsada dsada asdas das $41313.23232 FY2024 Q4 fy2024 sadsada dsada asdas das $1232123.23232"
pattern = 'FY(\d{4})'
matches = re.findall(pattern,text,flags=re.IGNORECASE)
for match in matches:
    print(match)

pattern = '\$[\d.]+'
matches = re.findall(pattern,text)
print(matches)

pattern = '(FY\d{4})[^\$]+(\$[\d.]+)'
matches = re.findall(pattern,text)
print(matches)

# re.search() finds first occurence 

# Exercise https://github.com/codebasics/py/blob/master/Advanced/regex/regex_tutorial_exercise_questions.ipynb