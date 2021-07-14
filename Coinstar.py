quarters = float(input('How many quarters do you have?\n'))
dimes = float(input('How many dimes do you have?\n'))
nickels = float(input('How many nickels do you have?\n'))
pennies = float(input('How many pennies do you have?\n'))

q_price = float(0.25)
d_price = float(0.10)
n_price = float(0.05)
p_price = float(0.01)

q = q_price * quarters
d = d_price * dimes
n = n_price * nickels
p = p_price * pennies

total = q + d + n + p

rate = float(1130.81)

conversion = total * rate

print(f'Your total amount of {quarters:.0f} quarters, {dimes:.0f} dimes, {nickels:.0f} nickels, and {pennies:.0f} pennies equals to ${total}')

print(f'Converted to Korean won, you have ₩{conversion:.2f}')


