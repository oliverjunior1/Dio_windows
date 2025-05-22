aquivo = open('lorem.txt', 'r')
print(aquivo.read())
print("******************************************")
aquivo = open('lorem.txt', 'r')
print(aquivo.readline())
print(aquivo.readline())
print(aquivo.readline())
print('*****************************************')
print(aquivo.readlines())
print('*****************************************')

aquivo = open('lorem.txt', 'r')
# tip
while len(linha := aquivo.readline()):
    print(linha)
aquivo.close()