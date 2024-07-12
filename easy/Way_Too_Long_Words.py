list_num = int(input().strip())
words = [input().strip() for i in range(list_num)]

for word in words:
    if len(word) < 1 and len(word) > 100:
        print("Word Length must be between 1 and 100")
    elif len(word) > 10:
        abb = word[0] + str(len(word) - 2) + word[-1]
        print(abb)
    else:
        print(word)
