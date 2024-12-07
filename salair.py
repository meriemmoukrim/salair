print("ce programme permet de compsée le salaire")
Salair_Base=float(input("donner le salair de base : "))
HS=float(input("donner le heure sut : "))
anciente=int(input("donner l'anciente : "))
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
Prime_anciente = (Salair_Base *  taux_anciente )/ 100
print(f"le prime anciente est : {Prime_anciente}")
Prime_HS = HS * 80
print(f"le prime heure sut est : {Prime_HS}")

SB = Salair_Base + Prime_HS  + Prime_anciente
print(f"le salair brut est : {SB}")

Mutuelle = (3 * SB ) / 100
print(f"la mutuelle est : {Mutuelle} ")

Retrait = (6 * SB ) / 100
print(f"la retraite  est : {Retrait} ")

if 0 < SB <= 2500:
       Deduction = Taux = 0
elif 2500 < SB <= 4166 :
       Deduction , Taux = 250 , 10
elif 4166 < SB <= 5000 :
       Deduction , Taux = 666.67 , 20
elif 5000 < SB <= 6666 :
       Deduction , Taux = 1166.67 , 30
elif 6666 < SB <= 15000 :
       Deduction , Taux = 1433.33 , 34
else :
       Deduction, Taux = 2033.33, 38
IR = (SB * Taux / 100 )- Deduction
print(f"le IR est : {IR}")
Salaire_net = SB - Mutuelle - Retrait - IR
print(f"le salaire net est : {Salaire_net}")


  



