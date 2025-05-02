class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus

    def __repr__(self):
        return self.address

    def avaliable_menus(self, time):
        avaliable_menu = []
        for menu in self.menus:
            if menu.start_time <= time <= menu.end_time:
                avaliable_menu.append(menu)
        return avaliable_menu

class Menu:
  def __init__(self, name, items, start_time, end_time):
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  def __repr__(self):
      return f"{self.name} menu avaliable from {self.start_time} to {self.end_time}"

  def calculate_bill(self, purchased_items):
      bill = 0
      for item in purchased_items:
          if item in self.items:
              bill += self.items[item]
      return bill

class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises

#menus
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50}

early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,}

dinner_items = {
  'crostini with eggplant caponata': 13.00, 'caesar salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,}

kids_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00}

arepas_items = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50}

# menu avaliability
brunch = Menu('brunch', brunch_items, 1100, 1600)
early_bird = Menu('early_bird', early_bird_items, 1500, 1800)
dinner = Menu('dinner', dinner_items, 1700, 2300)
kids = Menu('kids', kids_items, 1100, 2100)
arepas = Menu('Take a’ Arepa', arepas_items, 1000, 2000)

menu_list = [brunch, early_bird, dinner, kids]

flagship_store = Franchise("1232 West End Road", menu_list)
new_installment = Franchise("12 East Mulberry Street", menu_list)
arepas_place = Franchise("189 Fitzgerald Avenue", arepas)

basta = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])
arepa = Business('Take a’ Arepa', [arepas_place])