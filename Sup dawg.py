import time
text = 'hello world'
print(text)
response = input() 
print(response + ' is what a normie would say')
response2 = input()
print('im sorry that was uncalled for, ill just go home now')
time.sleep(3)

text2 = """how many feet are in a mile?
is it:
A)5638
B)5219
C)5280
D)4976"""
answer = 'C'
while True:
    print(text2)
    response3 = input().upper()

    if response3 == answer:
        print('Yay! you did it!')
        break
    else:
        print('Try again')

text3 = 'that was impressive!'
print(text3)