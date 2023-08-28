from itertools import permutations
actual_word = "HISTORY"
alphabet_list=[]
for x in actual_word:
    alphabet_list.append(x)
perm = permutations(alphabet_list)
word_list=[]
word=""
for ele in list(perm):
    for letter in ele:
        word= word + letter
    word_list.append(word)
    word=""
print(word_list)


