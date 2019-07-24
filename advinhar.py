from random import randint
from time import sleep
computer = randint(0, 5)
print('\033[1;35m=§='*20)
print('\033[0;34mVou pensar em um numero de 0 a 5! Tente adivinhar!')
print('\033[1;35m=§='*20)
player = int(input('\033[1mQual é o numero que você pensou?\033[m'))
print('\033[1;32mPROCESSANDO...')
sleep(2)
if player == computer:
    print('\033[1;33mParabéns!!! Você ganhou!!!')
else:
    print(f'\033[1;31mOps! Tente outra vez você perdeu eu pensei no {computer}!!')