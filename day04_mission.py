# 8-1, 8-2, 8-3, 8-4, 8-5
e2f = dict(dog='chien', cat='chat', walrus='morse')  # 8-1

print('#8-2: ',e2f['walrus'])  # 8-2

f2e = dict()  # 8-3
for key, value in e2f.items():
    f2e[value] = key
print('#8-3: ',f2e)

for key, value in e2f.items():  # 8-4
    if value == 'chien':
        print('#8-4: ',key)

print('#8-5: ',end=' ')  # 8-5
for key in e2f.keys():
    print(key, end=' ')


