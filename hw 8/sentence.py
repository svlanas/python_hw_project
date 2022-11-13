sentence = input("введіть речення з двох або більше слів ")
while sentence.find(" ") == -1 or sentence.count(" ") < 1:
    print("ви ввели некоректне значення")
    two_words = input("введіть речення з двох або більше слів ")
sentence = sentence.expandtabs()
# sentence = sentence.lower()
sentence_lst = sentence.split(" ")
n = sentence_lst.count("")
for i in range(1, n+1):
    sentence_lst.remove("")
sentence_lst.sort()
print("{:<7} {:<15}".format("Index", "List\'s element"))
for j in range(len(sentence_lst)):
    print(f"{j:<7} {sentence_lst[j]:<15}")
print("Number of elements =", len(sentence_lst))