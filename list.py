carNames = []
while True:
    print('please enter the name of car ' + str(len(carNames) + 1) + '(Or enter nothing to stop)')
    name = input()
    if name == '':
        break
    # carNames = carNames + [name]
    if name in carNames:
        print('the name : ' + name + ' already exits')
    else:
        carNames.append(name)
print('the car names are:')
for name in carNames:
    print(name)
