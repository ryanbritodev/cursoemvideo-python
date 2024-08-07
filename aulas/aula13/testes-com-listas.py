# num = (2, 5, 9, 1)
# num[2] = 3
# print(num)
# Não é possível, tuplas são IMUTÁVEIS

num = [2, 5, 9, 1]
num[2] = 3
print(num)
num.append(7)
num.sort()
print(num)
print(num[::-1])
num.sort(reverse=True)
num.insert(2, 2)
num.remove(2)
if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4!")
num.pop()
print(num)
print(f"Essa lista tem {len(num)} elementos")
