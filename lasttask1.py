x=int(input('Введите число от 1 до 9: '))

if x<=3 and x>=0:
    s=input('Введите строку: ')
    n=int(input('Введите число повторов строки: '))
    i=0
    while i<n:
        print(s)
        i=i+1

elif x<=6 and x>=4:
    m=int(input('Введите степень, в которую следует возвести число: '))
    x=x**m
    print(x)

elif x<=9 and x>=7:
    n=10
    i=0
    while i<n:
        x=x+1
        print(x)
        i=i+1

else:
    print('Ошибка ввода')
