my_dict = {'tuple': 1, 'list': '2', 'dict': 3, 'set': 4}
my_dict['tuple'] = (1, 2, 3, 4, 5)
my_dict['list'] = ['listval1', 'listval2', 'listval3', 'listval4', 'listval5']
my_dict['dict'] = {'dictkey1': 1, 'dictkey2': 2.2, 'dictkey3': False, 'dictkey4': 'value4', 'dictkey5': 'Five'}
my_dict['set'] = {'setval1', 123, 'setval3', True, 89.1}

print('My first dictionary:', my_dict)

last_tuple = my_dict['tuple'][-1]
print('Last element of the tuple is:', last_tuple)


my_dict['list'].append('addedlist')
my_dict['list'].pop(1)


my_dict[('I am a tuple',)] = 'addedvalue'
del my_dict['dict']


my_dict['set'].add(302)
my_dict['set'].remove(89.1)

print('My changed dictionary:', my_dict)
