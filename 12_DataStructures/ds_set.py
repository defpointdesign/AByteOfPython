# >>> bri = set(['brazil', 'russia', 'india'])
# >>> 'india' in bri
# True
# >>> 'usa' in bri
# False
# >>> bric = bri.copy()
# >>> bric.add('china')
# >>> bric.issuperset(bri)
# True
# >>> bri.remove('russia')
# >>> bri & bric # OR bri.intersection(bric)
# {'brazil', 'india'}