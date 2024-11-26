print("ce programme permet de composée le salaire")
salair_base=float(input("donner le salair de base : "))
HS=float(input("donner heure sut  : "))
anciente=float(input("donner l'anciente: "))
if 0 <  anciente < 2 :
    taux_anciente = 0
elif 2 <= anciente < 5 :
    taux_anciente = 5
elif 5 <= anciente <  10 :
    taux_anciente = 10
elif 10 <= anciente < 15 :
    taux_anciente = 15
elif 15 <= anciente < 20 :
    taux_anciente = 20
else :
    taux_anciente = 25
prime_anciente = salair_base * taux_anciente / 100
print(f"le prime anciente est : {prime_anciente}")
prime_HS = 80 * HS
print(f"le prime HS est : {prime_HS}")
SB = salair_base + prime_HS + prime_anciente
print(f"le salaire brut est : {SB} ")
mutuelle = (3 * SB) / 100
print("la mutuelle est :", mutuelle)
retraite = (6 *  SB) / 100
print("la retraite est :", retraite )
if 0 < SB <= 2500 :
    taux = 0
    deduction = 0
elif 2500 < SB <= 4166 :
    taux = 10
    deduction = 250
elif 4166 < SB <= 5000 :
    taux = 20
    deduction = 666.67
elif 5000< SB <= 6666 :
    taux = 30
    deduction = 1166.67
elif 6666 < SB <= 15000 :
    taux = 34
    deduction = 1433.33
else :
    taux = 38
    deduction = 2033.33
IR = SB * taux / 100  - deduction
print(f"IR est :{IR}")
salair_net = SB - mutuelle - retraite - IR
print("le salair net est :", salair_net )




