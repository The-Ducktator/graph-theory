print("Hello there user")
word = ''

path = input("Enter the directory you would like to use ")

word = input("Enter the regular expertion you would like to found ")
checker = word
endsWithMatch = checker.endswith('$')
startsWithMatch = checker.startswith('^')
digitMatch = ("/d" == checker)
notDigitMatch = ("/D" == checker)
if digitMatch or notDigitMatch:
  checker = "0|1|2|3|4|5|6|7|8|9"
characterMatch = ("/w" == checker)
notCharacterMatch = ("/W" == checker)
if characterMatch or notCharacterMatch:
  lowerChecker = "a|b|c|d|e|f|g|h|i|j|k|l|m|n|o|p|q|r|s|t|u|v|w|x|y|z|"
  capChecker = "|A|B|C|D|E|F|G|H|I|J|K|L|M|N|O|P|Q|R|S|T|U|V|W|X|Y|Z|"
  otherChecker = "|_|0|1|2|3|4|5|6|7|8|9"
  alphaChecker = lowerChecker + capChecker
  checker = alphaChecker + otherChecker
  print(checker)
alternatives = "|" in checker
trueWords = checker.split("|")
exactMatch = startsWithMatch and endsWithMatch
print(exactMatch)
trueWord = word
if '.' in word:
  print("query found")
if startsWithMatch == True:
  trueWord = trueWord.replace('^', '')
if endsWithMatch == True:
  trueWord = trueWord.replace('$', '')
f = open(path, 'r')
line = f.readline()
while line:
  if exactMatch:
    if trueWord == line:
      print(line)
  elif startsWithMatch:
    if line.startswith(trueWord):
      print(line)
  elif endsWithMatch:
    if line.endswith(trueWord):
      print(line)
  elif notDigitMatch:
    if not any(substring in line for substring in trueWords):
      print(line)
  elif notCharacterMatch:
    if not any(substring in line for substring in trueWords):
      print(line)
  elif alternatives:
    if any(substring in line for substring in trueWords):
      print(line)
  else:
    if trueWord in line:
      print(line)
     
  line = f.readline()
f.close()

print("Thank you for using this code:)")
print("Have a wondefulday")
