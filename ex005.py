print("Vote em um dos consoles \n"
      "Playstation - P \n"
      "XBOX        - X \n"
      "NINTENDO    - N \n")

p = 0
x = 0
n = 0

Usuário = input("Voto do usuário 1: ").lower()
if Usuário == "p":
    p += 1
elif Usuário == "x":
    x += 1
elif Usuário == "n":
    n += 1
Usuário = input("Voto do usuário 2: ").lower()
if Usuário == "p":
    p += 1
elif Usuário == "x":
    x += 1
elif Usuário == "n":
    n += 1
Usuário = input("Voto do usuário 3: ").lower()
if Usuário == "p":
    p += 1
elif Usuário == "x":
    x += 1
elif Usuário == "n":
    n += 1
Usuário = input("Voto do usuário 4: ").lower()
if Usuário == "p":
    p += 1
elif Usuário == "x":
    x += 1
elif Usuário == "n":
    n += 1
Usuário = input("Voto do usuário 5: ").lower()
if Usuário == "p":
    p += 1
elif Usuário == "x":
    x += 1
elif Usuário == "n":
    n += 1

#se o Playstaion ganhar
if p > x > n:
    print("O console mais votado foi o Playstation com {} votos.".format(p))
elif p > n > x:
    print("O console mais votado foi o Playstation com {} votos.".format(p))
elif p > n == x:
    print("O console mais votado foi o Playstation com {} votos.".format(p))
#Se o Xbox ganhar
if x > n > p:
    print("O console mais votado foi o Xbox com {} votos.".format(x))
elif x > p > n:
    print("O console mais votado foi o Xbox com {} votos.".format(x))
elif x > p == n:
    print("O console mais votado foi o Xbox com {} votos.".format(x))
#Se o Nintendo ganhar
if n > p > x:
    print("O console mais votado foi o Nintendo com {} votos.".format(n))
elif n > x > p:
    print("O console mais votado foi o Nintendo com {} votos.".format(n))
elif n > x == p:
    print("O console mais votado foi o Nintendo com {} votos.".format(n))
#Se houver empate
else:
    if p == x > n:
       print("Houve empate entre Playstation e Xbox, ambos com {} pontos.".format(p))
    elif p == n > x:
       print("Houve empate entre Playstation e Nintendo, ambos com {} pontos.".format(p))
    elif n == x > p:
       print("Houve empate entre Nintendo e Xbox, ambos com {} pontos.".format(n))
