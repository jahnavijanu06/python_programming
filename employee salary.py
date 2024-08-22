#input the basic pay
basic_pay = float (input("enter the basic pay of the employee:"))

#calculate HRA as 20% of basic pay
hra=0.20*basic_pay
#calculate DA as 10% of basic pay
da=0.10*basic_pay
#calculate total salary
total_salary=basic_pay+hra+da
#display the results
print(f"basic pay:{basic_pay}")

print(f"HRA:{hra}")

print(f"DA:{da}")

print(f"total salary:{total_salary}")

