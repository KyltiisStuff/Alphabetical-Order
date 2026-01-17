with open("word list.txt") as f:
  words = [line.strip() for line in f]
letters = []
results = []
string = ""
for word in words:
  letters = []
  for letter in word:
    letters.append(letter)
  letters.sort()
  string = "".join(letters)
  results.append(string)
for word in range(len(results)):
  if results.count(results[word]) > 1:
    print(words[word])
