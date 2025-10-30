is_raining = False
is_cold = False
print("Good morning")
if is_raining and is_cold:
    print("Bring an umbrella, and jacket")
elif is_raining and not(is_cold):
    print("Bring an umbrella")
elif not(is_raining) and is_cold:
    print("Bring a jacket")
else:
    print("shirt is fine")


amount = 50
if amount <= 50:
    print("Purchase approved")
else:
    print("Pin required")
