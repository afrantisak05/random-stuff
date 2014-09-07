name = raw_input("what is your name: ")
health = raw_input("what is your health: ")
health = int(health)
while True:
    damage = raw_input("damage ")
    damage = int(damage)
    weakness = raw_input("weakness ")
    weakness = int(weakness)
    real_damage = weakness * damage
    resistance = raw_input("resistance ")
    resistance = int(resistance)
    correct_damage = real_damage + resistance
    health = health - correct_damage 
    print "{name}, health left {difference}".format(name=name, difference = health)
