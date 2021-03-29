import calc_bmi

a = float(input("身長(m):"))
b = float(input("体重(kg):"))

print(f"BMI値:{calc_bmi.get_bmi(a,b)}")
