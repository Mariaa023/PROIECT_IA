from probleme.problema_somn import fitness_somn,limite_somn


def testeaza_somn_manual():
    print("Test manual program somn")
    ora_culcare=float(input("Introdu ora de culcare:"))
    ora_trezire=float(input("Introdu ora de trezire:"))

    individ=[ora_culcare,ora_trezire]

    fitness= fitness_somn(individ)

    print("Ora culcare:", afiseaza_ora(ora_culcare))
    print("Ora trezire:", afiseaza_ora(ora_trezire))
    print("Fitness (penalizare):", fitness)
    print()

def afiseaza_ora(ora_reala):
    ora=int(ora_reala)
    minute=int((ora_reala-ora)*60)

    if minute<0:
        minute=0
    if minute>=60:
        minute=59
    return f"{ora:02d}:{minute:02d}"

def ruleaza_problema_somn():
    solutie,fitness=evolutie_diferentiala(
        fitness_somn,
        limite_somn
    )
    print("Problema somn:")
    print("Ora culcare:", afiseaza_ora(solutie[0]))
    print("Ora trezire:", afiseaza_ora(solutie[1]))
    print("Fitness:", fitness)
    print()

if __name__ =="__main__":
    ruleaza_problema_somn()
    testeaza_somn_manual()