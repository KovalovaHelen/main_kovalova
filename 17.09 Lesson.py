#"""
#1. Пользователь вводит два числа А и В, нужно вывести сумму чисел в диапазоне от А до В.
#"""
#
#a = int(input('Enter the minimum value : '))
#b = int(input('Enter the maximum value : '))
#
#s = 0
#i = a
#
#while a<=i<=b:
#    s+=i
#    i+=1
#
#print (s)
#
"""
2. Пользователь вводит два числа А и В, нужно вывести сумму всех четных чисел в диапазоне от А до В.
"""
#a = int(input('Enter the minimum value : '))
#b = int(input('Enter the maximum value : '))
#
#s = 0
#i = a
#
#while a<=i<=b:
#    if i % 2 == 0:
#        s+=i
#        i+=2
#    else:
#        i=a+1
#        s += i
#        i += 2
#
#print (s)
#
"""
3. Пользователь вводит два числа А и В, нужно вывести прямоугольник со сторонами А и В с помощью символа "*", используя цикл.
"""
#
#a = int(input('Enter the width of the rectangle : '))
#b = int(input('Enter the height of the rectangle : '))
#i=1
#
#while i<b+1:
#    print ("*"*a)
#    i=i+1
#
"""
4.Запросить у пользователя число N, вывести треугольник шириной N, используя символ "*".
"""
#N = int(input('Enter number N : '))
#i=1
#
#while i<N+1:
#    print ("*"*N)
#    N=N-1
