with open("word list.txt") as f:
  words = [line.strip() for line in f]
letters = []
string = ""
for word in words:
  letters = []
  for letter in word:
    letters.append(letter)
  letters.sort() # if you want it to be in reverse alphabetical order, you can put "reverse=True" in the parentheses
  string = "".join(letters)
  if string == word:
    print(word)
