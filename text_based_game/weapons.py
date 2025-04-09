class Weapons:
    def __init__(self, name, dmg, agility, max_upgradable_dmg):
        self.name = name
        self.dmg = dmg
        self.agility = agility
        self.max_upgradable_dmg = max_upgradable_dmg

weapons_selection = {
    "sword": Weapons("Sword", 10, 5, 20),
    "axe": Weapons("Axe", 15, 3, 25),
    "bow": Weapons("Bow", 8, 12, 18),
    "dagger": Weapons("Dagger", 5, 15, 12),
    "railgun": Weapons("Railgun", 20, 2, 35),
    "rocket launcher": Weapons("Rocket Launcher", 25, 1, 40)}