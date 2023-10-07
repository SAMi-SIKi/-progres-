inventory_player= ['sword', 'shield', 'tunic', 'gun']
inventory_chest= ['banana', 'diamond', 'ammo']

is_pickedup= True

if is_pickedup:
    print("You picked up the items")
    inventory_player += inventory_chest
print(inventory_player)