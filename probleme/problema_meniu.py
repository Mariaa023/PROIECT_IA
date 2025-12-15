def fitness_meniu(individ):
    proteine=individ[0]
    carbohidrati=individ[1]
    grasimi=individ[2]

    calorii=proteine*4+carbohidrati*4+grasimi*9

    penalizare_calorii=abs(calorii-2000)/100
    penalizare_proteine=abs(proteine-150)/50
    penalizare_carbohidrati=abs(carbohidrati-250)/50
    penalizare_grasimi=abs(grasimi-70)/20

    return(
        penalizare_calorii+
        penalizare_proteine+
        penalizare_carbohidrati+
        penalizare_grasimi
    )

limite_meniu=[
    (50,250),
    (100,400),
    (30,120)
  ]