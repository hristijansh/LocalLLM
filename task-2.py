def isPalindrome(word):
    for letter in word:
        print(letter)
        
    for i in range(0, len(word) // 2):
        j = len(word) - i - 1
        if word[i] != word[j]:
            print(False)
            return
    print(True)
isPalindrome("racecar")
