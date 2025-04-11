def is_palindrome(text):
    cleaned =''.join(text.lower().split())

    return cleaned == cleaned[::-1]

word =input('Enter a word : ')

if is_palindrome(word):
    print("It's a palindrome!")
else:
    print(" Not a palindrome.")