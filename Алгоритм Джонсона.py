n = int(input("Введите количество заданий:"))

vremya1, vremya2 = [], []

print("Введите время выполнения операции для каждой машины:")
for i in range(n):
    a = list(map(int, input().split()))
    if len(a) == 2:
        for num in range(2):
            if num == 0:
                vremya1.append(a[num])
            elif num == 1:
                vremya2.append(a[num])
    else:
        print("Алгоритм Джонсона работает лишь для 2 машин.")

machine1, machine2 = [], []

for i in range(n):
    mn1 = min(vremya1)
    mn2 = min(vremya2)
    if mn1 <= mn2:
        ind = vremya1.index(mn1)
        if vremya1[ind] < vremya2[ind]:
            machine1.append(vremya1[ind])
        else:
            machine2 = [vremya2[ind]] + machine2
        vremya1.pop(ind)
        vremya2.pop(ind)
    else:
        ind = vremya2.index(mn2)
        if vremya1[ind] < vremya2[ind]:
            machine1.append(vremya1[ind])
        else:
            machine2 = [vremya2[ind]] + machine2
        vremya1.pop(ind)
        vremya2.pop(ind)
print(machine1)
print(machine2)
print(machine1 + machine2)
print("Оптимальное время:", sum(machine1 + machine2))
