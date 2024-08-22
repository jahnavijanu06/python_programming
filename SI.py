P=float(input("enter principle: "))
T=float(input("enter Time: "))
R=float(input("enter rate: "))
SI=(P*T*R)/100
CI=P*(pow((1+R/100),T))
print("Simple interest is:",SI)
print("compund interest is:",CI)
