"""Palindrome"""
def palindrome(me):
    mo = me.casefold()
    you = reversed(mo)
    if list(mo) == list(you):
        return ('yes')
    else:
        return ("no")

print(palindrome('bhihB'))


def pal(me):
    mo = me.casefold()
    you = mo[::-1]
    if list(mo) == list(you):
        return ('yes')
    else:
        return ("no")
print(pal('Mom'))