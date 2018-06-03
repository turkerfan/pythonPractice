import re
import urllib.request
with urllib.request.urlopen('https://en.wikipedia.org/wiki/Spain') as response:
  html = response.read()
html=str(html)

#  html
pattern = re.compile( "[a-zA-Z]+" ) #regular exp for word
answers = pattern.findall(html) #list
print(answers)
print(len(answers))

listLindsay = re.compile( "[A-Z][a-z]*")
answersLindsay = listLindsay.findall(html)
print(answersLindsay)
print(len(answersLindsay))
print(len(answersLindsay)/len(answers))

if len(answersLindsay)>len(answers):
  print("Spanish is more frequent! Wohoo!")
else:
  print("Spain is more frequent! Long live the king!")

