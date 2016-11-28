a = float(input("enter a: "))
b = float(input("enter b: "))
c = float(input("enter c: "))
d = float(input("enter d: "))

divAb = a/b
divCd = c/d

if divAb > divCd:
    print(round(divAb,3))
else:
    print(round(divCd,3))
