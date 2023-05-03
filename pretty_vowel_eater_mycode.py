user_word=input("Enter word: ")
user_word=user_word.upper()
word=[]
for letter in user_word:
    if letter=="A":
        continue
    if letter=="E":
        continue
    if letter=="O":
        continue
    if letter=="U":
        continue
    if letter=="I":
        continue
    if letter=="Y":
        continue
    word.append(letter)
    #print(word)
word_without_vowels=''.join(word)
print(word_without_vowels)
    #word_without_vowels=''.join(letter)
    #print(word_without_vowels)
    
# Запропонувати користувачу ввести слово
# та присвоїти його змінній user_word.


#for letter in user_word:
   # Завершити тіло циклу.

# Вивести слово, призначене word_without_vowels.

