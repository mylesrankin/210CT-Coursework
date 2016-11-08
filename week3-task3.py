# Vowel removal#
def removeVowels(n,d=0):
    if d > (len(n)-1):
        return n
    elif n[d] in ["a","e"]:
        print("vowel")
        print(n)
        return removeVowels(n[1:],d+1)
    else:
        print(n)
        print("CCC")
        return removeVowels((n[1:]+n[d]),d+1)
