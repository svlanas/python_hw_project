two_words = input("введіть 2 слова через пробіл ")
while two_words.find(" ") == -1 or two_words.count(" ") != 1:
    print("ви ввели некоректне значення")
    two_words = input("введіть 2 слова через пробіл ")
i = two_words.find(" ")
reverse_1 = two_words[i-1::-1]
reverse_2 = two_words[:i:-1]
reverse = reverse_1 + " " + reverse_2
print(reverse.title())
