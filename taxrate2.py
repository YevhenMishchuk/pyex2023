income = float(input("Введіть річний дохід: "))

if income < 85528:
 tax = income * 0.18 - 556.02
elif income>85528:
    tax=14839.02+0.32*(85528-income)# тут записуємо ваш код.

tax = round(tax, 0)
print("Податок склав:", tax, "талера") 
 