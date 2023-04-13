"""
You are given a string s, which contains stars *.

In one operation, you can:

Choose a star in s.
Remove the closest non-star character to its left, as well as remove the star itself.
Return the string after all stars have been removed.

Note:

The input will be generated such that the operation is always possible.
It can be shown that the resulting string will always be unique.
"""

def RemoveStars():
    string = 'leet**cod*e'
    solution = list()
   
    for character in string:
        if '*' in character:
            solution.pop() # Removes the last element appended to the list
        else:
            solution+=[character]

    print(''.join(solution))
   
RemoveStars()