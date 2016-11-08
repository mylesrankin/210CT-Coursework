date = "25 09 2016"
d = int(date[0:2])
m = int(date[3:5])
y = int(date[6:10])

def daysLeft(d,m,y):
    months = [31,28,31,30,31,30,31,31,30,31,30,31]
    soFar = d-months[m]
    
    for i in range(0,(m)):
        soFar +=months[i]
    daysLeft = sum(months)-soFar
    if y%4 == 0:
        if m>2:
            soFar  +=1
    
    print("Days so far:")     
    print(soFar)
    print("Days left: ")
    print(daysLeft)
    
        
    
    
