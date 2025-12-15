import random

def evolutie_diferentiala(functie_fitness,limite):
    nr_cromozomi=20
    factor_f=0.8
    cr=0.9
    nr_generatii=100
    dim=len(limite)
    populatie=[]
    for i in range(nr_cromozomi):
        individ=[]
        for j in range(dim):
            val=random.uniform(limite[j][0],limite[j][1])
            individ.append(val)
        populatie.append(individ)

    fitness=[]
    for individ in populatie:
        fitness.append(functie_fitness(individ))
    for generatie in range(nr_generatii):
        pop_noua=[]
        for i in range(nr_cromozomi):
            indici=list(range(nr_cromozomi))
            indici.remove(i)
            r1=random.choice(indici)
            indici.remove(r1)
            r2=random.choice(indici)
            indici.remove(r2)
            r3=random.choice(indici)
            x1=populatie[r1]
            x2=populatie[r2]
            x3=populatie[r3]
            vector_mutant=[]
            for j in range(dim):
                val=x1[j]+factor_f*(x2[j]-x3[j])
                vector_mutant.append(val)
            individ_nou=[]
            poz_oblig=random.randint(0,dim-1)
            for j in range(dim):
                if random.random()<cr or j==poz_oblig:
                    individ_nou.append(vector_mutant[j])
                else:
                    individ_nou.append(populatie[i][j])
            for j in range(dim):
                if individ_nou[j]<limite[j][0]:
                    individ_nou[j]=limite[j][0]
                if individ_nou[j]>limite[j][1]:
                    individ_nou[j]=limite[j][1]
            fitness_nou=functie_fitness(individ_nou)
            if fitness_nou<=fitness[i]:
                pop_noua.append(individ_nou)
            else:
                pop_noua.append(populatie[i])
        populatie=pop_noua
        fitness=[]
        for individ in populatie:
            fitness.append(functie_fitness(individ))
    cel_mai_bun=populatie[0]
    cel_mai_bun_fitness=fitness[0]
    for i in range(nr_cromozomi):
        if fitness[i]<cel_mai_bun_fitness:
            cel_mai_bun=populatie[i]
            cel_mai_bun_fitness=fitness[i]
    return cel_mai_bun,cel_mai_bun_fitness
