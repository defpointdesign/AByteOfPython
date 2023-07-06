ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-land.org',
    'Spammer': 'spammer@hotmail.com'
}
print ("Swarrop's adress is", ab['Swaroop'])

# Deleting a key-value pair
del ab['Spammer']
print('\nThere are {} contact in the address-book\n'.format(len(ab)))

for name, address in ab.items():
    print('Contact {} at {}'.format(name, address))

# Adding a key-value pair
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuidos address is", ab['Guido'])
