import calc_bmi

a = float(input("身長(m):"))
b = float(input("体重(kg):"))

for i in range(2):
    print(f"BMI値:{calc_bmi.get_bmi(a,b)}")
