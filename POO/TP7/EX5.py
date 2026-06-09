"""
Vérifier si &quot;radar&quot; est un palindrome en utilisant uniquement un deque.
"""

from collections import deque

def is_palindrome(word):
    d = deque(word)
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True
print(is_palindrome("radar"))