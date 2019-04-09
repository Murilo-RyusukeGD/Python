num = int(input("Digite um número: "))

print("=" * 18)
for index in range(0,11):
    print ("| {} x {:>2} = {:<5}|".format(num, index, num*index))
print("=" * 18)