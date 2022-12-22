from time import sleep
import math
import random


def print_loading():
    print('█▒▒▒▒▒▒▒▒▒')
    sleep(1)
    print('███▒▒▒▒▒▒▒')
    sleep(2)
    print('█████▒▒▒▒▒')
    sleep(3)
    print('███████▒▒▒')
    sleep(4)
    print('█████████▒')
    sleep(5)
    print('██████████')


def prim_roots(modulo: int) -> list:
    coprime_set = set()
    for num in range(1, modulo):
        if math.gcd(num, modulo) == 1:
            coprime_set.add(num)
    result = []
    for g in range(1, modulo):
        temp_set = set()
        for powers in range(1, modulo):
            temp_set.add(pow(g, powers, modulo))
        if coprime_set == temp_set:
            result.append(g)
    return result


def is_prime(n: int) -> bool:
    for i in range(2, int(math.sqrt(n))+1):
        if (n % i) == 0:
            return False
    return True


def generate_keys() -> list:
    prime_ints = [i for i in range(500, 2000) if is_prime(i)]
    p = random.choice(prime_ints)
    g = random.choice(prim_roots(p))
    x = random.randint(2, p - 2)
    y = (g**x) % p
    return [p, g, y, x]


def encrypt():
    keys = generate_keys()
    print('                 ___  _    ___  ')
    print('\_/  _      ._    |  |_ \/  |  o')
    print(' |  (_) |_| |     |  |_ /\  |  o\n')
    text = input('▬▬ι═══════>   ').strip()
    print()
    print_loading()
    with open('encrypted.txt', 'w', encoding='utf-8') as en:
        for alpha in text:
            k = 0
            while k == 0:
                temp = random.randint(2, keys[0] - 2)
                k = temp if math.gcd(keys[0], temp) == 1 else 0
            a = (keys[1]**k) % keys[0]
            b = ((keys[2]**k) * ord(alpha)) % keys[0]
            en.write(f'{a} {b}\n')
    print(' _                                   ')
    print('|_) ._ o     _. _|_  _    |/  _     o')
    print('|   |  | \/ (_|  |_ (/_   |\ (/_ \/ o')
    print('                                 /   ')
    print(f'(̅_̅_̅_̅(̅_̅_̅_̅_̅_̅_̅_̅_̅̅_̅()ڪے   °·.¸.·°¯°·.¸.-<{keys[3]}>-.¸.·°¯°·.¸.·°')
    print(' _                              ')
    print('|_)     |_  | o  _   |/  _     o')
    print('|   |_| |_) | | (_   |\ (/_ \/ o')
    print('                            /   ')
    print(f'()___)____________)   𓂀 p = {keys[0]} 𓂀 g = {keys[1]} 𓂀 y = {keys[2]} 𓂀\n')
    print(' _             ')
    print('| \  _  ._   _ ')
    print('|_/ (_) | | (/_')
    print('\n')


def decrypt():
    print(' _                                   ')
    print('|_) ._ o     _. _|_  _    |/  _     o')
    print('|   |  | \/ (_|  |_ (/_   |\ (/_ \/ o')
    print('                                 /   ')
    x, p = '', ''
    while not x.isdigit():
        x = input('X   ▬▬ι═══════>   ')
    while not p.isdigit():
        p = input('P   ▬▬ι═══════>   ')
    x, p = int(x), int(p)
    print()
    print_loading()
    with open('encrypted.txt', 'r', encoding='utf-8') as en, open('decrypted.txt', 'w', encoding='utf-8') as dec:
        while True:
            str_lst = en.readline().strip().split(' ')
            if len(str_lst) == 1: break
            a, b = int(str_lst[0]), int(str_lst[1])
            res = (b * (a**(p-1-x))) % p
            dec.write(chr(res))
    print(' _             ')
    print('| \  _  ._   _ ')
    print('|_/ (_) | | (/_')
    print('\n')


def set_choice() -> int:
    choice_dict = {1: 'encrypt', 2: 'decrypt', 3: 'exit'}
    choice = input('(num|word) ▬▬ι═══════>   ')
    if choice.isdigit() and int(choice) in choice_dict.keys():
        return int(choice)
    elif choice.lower().strip() in choice_dict.values():
        for k, v in choice_dict.items():
            if v == choice.lower().strip():
                return k
    else:
        return set_choice()


def main():
    with open('el-gamal.txt', 'r', encoding='utf-8') as el:
        print(*el, '\n')
    match set_choice():
        case 1:
            encrypt()
        case 2:
            decrypt()
        case 3:
            exit(0)


if __name__ == "__main__":
    main()
