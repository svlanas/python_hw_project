sentence = input("введіть речення з двох або більше слів ")
while sentence.strip().find(" ") == -1 or sentence.strip().count(" ") < 1:
    print("ви ввели некоректне значення")
    sentence = input("введіть речення з двох або більше слів ")
sentence = sentence.expandtabs()
sentence_lst = sentence.split(" ")
n = sentence_lst.count("")
for i in range(1, n+1):
    sentence_lst.remove("")
sentence_lst.sort()
print("{:<7} {:<15}".format("Index", "List\'s element"))
for j in range(len(sentence_lst)):
    print(f"{j:<7} {sentence_lst[j]:<15}")
print("Number of elements =", len(sentence_lst))