import random as r

def generate_population(size):
    population = []
    genes = [0, 1]	
    for i in range(size):
        chromosome = []
        for i in range(n):
            chromosome.append(r.choice(genes))
        population.append(chromosome)
    return population


    
def fitness(l):
    risk_sum=0
    gain_sum=0
    investment_count=0
    for i in range(n): 
        risk_sum+= l[i]*risk[i]
        gain_sum+= l[i]*gain[i]
        investment_count+=l[i]

    if investment_count>3:
        return 0
    else:
        f =  wg*gain_sum - wr*risk_sum
        return f 


def selection(p):
    fitness_values = []
    for chromosome in p:
        fitness_values.append(fitness(chromosome))
	
    fitness_values = [float(i)/sum(fitness_values) for i in fitness_values]

    selected=r.choices(p, weights=fitness_values, k=2)	
    parent1 = selected[0]
    parent2 = selected[1]
	
    return parent1, parent2
    


def crossover(parent1,parent2):
    point=r.randint(0,n-1)
    child1=parent1[0:point]+parent2[point:]
    child2=parent2[0:point]+parent1[point:]
    return child1,child2


def mutate(l):
    point=r.randint(0,n-1)
    if l[point]==0:
        l[point]=1
    else:
        l[point]=0

    return l



def solution(p):
    fitness_values = []
    for chromosome in p:
        fitness_values.append(fitness(chromosome))

    max_value = max(fitness_values)
    max_index = fitness_values.index(max_value)
    sol=p[max_index]
    
    sol_risk=0
    sol_gain=0
    for i in range(n):
        sol_risk+= sol[i]*risk[i]
        sol_gain+= sol[i]*gain[i]

    return sol,sol_risk,sol_gain
    
    


n=int(input("Enter Number of items "))
risk=list()
gain=list()


print("Enter the gains : ")
for i in range(n):
    x=int(input())
    gain.append(x)


print("Enter the risks : ")
for i in range(n):
    x=int(input())
    risk.append(x)



    
wg=float(input("Enter weight of gain : "))
wr=float(input("Enter weight of risk : "))
    






x=50    #Generations
uc=1    #Crossover Prob
um=0.01 #Mutation Prob
size=100#Pop Size
    



population=generate_population(size)

for i in range(x):
    parent1,parent2=selection(population)
    
    if r.uniform(0,1)<uc:
        child1,child2=crossover(parent1,parent2)
    else:
        child1,child2=parent1,parent2
    
    if r.uniform(0,1)<um:
        child1=mutate(child1)
        child2=mutate(child2)

    print("Pass number ",i,"Children:",child1,child2)    
        
    population=[child1,child2] + population[2:]


ans=solution(population)

print("The solution is: ")
print(ans[0])
print("The Total Risk is:",ans[1], "and the total gain is ", ans[2] )

    
    


    

