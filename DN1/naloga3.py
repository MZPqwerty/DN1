n1 = int(input("Vnesite poljubno celo število: "))
n2 = int(input("Vnesite poljubno celo število: "))
n3 = int(input("Vnesite poljubno celo število: "))

print("Prvo število: " + str(n1) + ", Tip števila: " + str(type(n1)))
print("Drugo število: " + str(n2) + ", Tip števila: " + str(type(n2)))
print("Tretje število: " + str(n3) + ", Tip števila: " + str(type(n3)))

if n2 == n1 and n3 <= n1:
    print("Drugo število je enako prvemu in tretja je manjša ali enaka prvi.")
else:
    print("Drugo število ni enako prvemu ali pa je tretja vrednost večja od prve.")