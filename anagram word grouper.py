with open("anagrammatic words.txt") as f:
  words = [line.strip() for line in f]
letters = []
alphabetized = []
results = []
length = 0
for word in words:
  letters = []
  for letter in word:
    letters.append(letter)
  letters.sort()
  string = "".join(letters)
  alphabetized.append(letters)
for length in range(max(len(word) for word in words) + 1):
  for word in range(len(words)):
    if len(words[word]) == length and words[word] not in results:
      print(words[word])
        results.append(words[word])
        for i in range(len(alphabetized)):
          if alphabetized[i] == alphabetized[word] and i != word:
            print(words[i])
            results.append(words[i])
