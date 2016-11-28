
def alienInvasion(n):
    x = 3
    y = 5
    population = []
    for i in range(n):
        population.append(1)
    print(population)
    for j in population:
        population.insert(j+3,(population[j+3]+3))
        print(population)
    print(population)

def ai(n):
    population = [1]
    for i in range(0,n-1):
        if i%3 == 0:
            population[i] = (population[i-2]*3)
    print(population)
        
            
            
            
            
        
    
        
        
    
