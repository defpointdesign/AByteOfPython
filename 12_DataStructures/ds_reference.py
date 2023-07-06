print('Simple Assignment')
shop_list = ['apple', 'mango', 'carrot', 'banana']
# my_list is a just another name pointing to the same object!
my_list = shop_list

# I purchased first item, so I remove it from my_list
del shop_list[0]

print('shop_list is:', shop_list)
print('my_list is:', my_list)
# Notice that both shop_list and my_list print both print the same list
# without the confirming that they point to the same object

print('\nCopy by making a full slice')
# Make colpy by doing a full slice
mylist = shop_list[:]
# remove first item
del mylist[0]
print('shop_list is:', shop_list)
print('mylist is:', mylist)
