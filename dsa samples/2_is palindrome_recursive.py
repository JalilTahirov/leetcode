my_word = "aawbbaea"

def isPalindrome(word):
    if len(word) <=1:
        return True
    elif word[0] != word[-1]:
        return False
    else:
        return isPalindrome(word[1:-1])
    

print(isPalindrome(my_word))

