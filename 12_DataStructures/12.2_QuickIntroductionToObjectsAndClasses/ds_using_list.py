shoplist=['apple', 'mango', 'banana', 'blackberry']
print ('I must doing', len(shoplist), 'purchase')
print ('Purchase:', end=' ')

for item in shoplist:
    print(item, end= ' ')
print('\n also have to buy rice.')

shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
shoplist.sort()

print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)



