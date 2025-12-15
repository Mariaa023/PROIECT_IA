def fitness_somn(individ):
    ora_culcare=individ[0]
    ora_trezire=individ[1]

    if ora_culcare>ora_trezire:
        durata_somn=ora_trezire+24-ora_culcare
    else:
        durata_somn=ora_trezire-ora_culcare

    penalizare_durata=abs(durata_somn-8)
    penalizare_trezire=abs(ora_trezire-8)

    penalizare_culcare_tarzie=0
    if ora_culcare>24:
        penalizare_culcare_tarzie=ora_culcare-24
    return  penalizare_durata+penalizare_trezire+penalizare_culcare_tarzie

limite_somn=[
    (22,26),
    (6,10)
]
