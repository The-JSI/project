class Weapons:
    def __init__(self, name, dmg, agility):
        self.name = name
        self.dmg = dmg
        self.agility = agility

weapons_selection = {
    "sword": Weapons("Sword", 10, 5),
    "axe": Weapons("Axe", 15, 3),
    "bow": Weapons("Bow", 8, 12),
    "dagger": Weapons("Dagger", 5, 15)
}