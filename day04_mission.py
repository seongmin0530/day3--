# 8-6, 8-7, 8-8, 8-9
life = {'animal':dict(cats='Henri', octopi='Grumpy', emus='Lucy'), 'plants': dict(), 'other': dict()}  #8-6

first_key_list = [key for key in life.keys()]  # 8-7
print('#8-7: ', first_key_list)

animals_key_list = [key for key in life['animal'].keys()]  # 8-8
print('#8-8: ', animals_key_list)

print('#8-9: ',life['animal']['cats'])  # 8-9


