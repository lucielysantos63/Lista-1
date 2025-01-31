lista = [20, 76, 94, 60, 28, 65, 4, 69, 71, 22]

a = lista[3:8]
b = lista[3:-3]
c = lista[2::2]
d = lista[2:-2:2]
e = lista[-1:0]
f = lista[-1:0:-1]
g = lista[-1::-1]
h = lista[::-1]
i = lista[6::-2]


print(f"Lista[3:8] = {a}")
print(f"Lista[3:-3] = {b}")
print(f"Lista[2::2] = {c}")
print(f"Lista[2:-2:2] = {d}")
print(f"Lista[-1:0] = {e}")
print(f"Lista[-1:0:-1] = {f}")
print(f"Lista[-1::-1] = {g}")
print(f"Lista[::-1] = {h}")
print(f"Lista[6::-2] = {i}")