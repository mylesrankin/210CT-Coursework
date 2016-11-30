# Myles Rankin 2016 - Vowel removal recursively
def removeVowels(n,d=0): # n is string input, d=0 is stepper value which is left as default 0
    if d == (len(n)): # checks if stepper value is equal to list size
        return n
    elif n[0].lower() in ["a","e","i","o","u"]: # Check if current position in list is a vowel
        return removeVowels(n[1:],d) # return list apart from position 0
    else:
        return removeVowels((n[1:]+n[0]),d+1) # return list but with n[0] at end so i.e. input vowels = owelsv

# Example of removing vowels from a string
print(removeVowels("Ellie"))
