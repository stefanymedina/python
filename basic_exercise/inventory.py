inventory = {'croissant': 19, 'bagel': 4, 'muffin': 8, 'cake': 1}
stock_list ={}
stock_list.update(inventory)

stock_list.update({'cookie': 18})
stock_list.pop('cake')

print(stock_list)