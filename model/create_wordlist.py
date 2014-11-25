import re

word_file = open("aammango_dic", "r") 
wlist = open("wlist", "w")

wordArr = word_file.readlines()
word_file.close()

wlist.write("var wordList = [")
gram = "var grammar = {numStates: 1, start: 0, end: 0, transitions: ["
words = ""

for word in wordArr:
  word = word.strip('\n')
  splitWord = word.split(' ')
  print(splitWord)
  words += "[\"" + splitWord[0] + "\", \"" + ' '.join(splitWord[1:]) + "\"], "
  gram += "{from: 0, to: 0, word: \"" + splitWord[0] + "\"}, "

wlist.write(words[:-2] + "];\n" + gram[:-2] + "]};")
wlist.close()