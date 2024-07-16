
class Rifles():
    def __init__(self, ammomax, damage, price):
        self.ammomax = ammomax
        self.damage = damage
        self.price = price
        #Создание информации о оружии  - Creating a info of gun
    def info(self):
        print(f"МаксимумПатронов - {self.ammomax}")
        print(f"УронОтОружия - {self.damage}")
        print(f"ЦенаРужья - {self.price}")
        #Параметры оружия - Setting of gun
gun1 = Rifles(5, 50, 2500)
gun2 = Rifles(10, 150, 5000)



def choosingrifle():
  
    money = int(input("Выдай себе деньги, от одного до 5000"))
    if money > 5000:
        print("ТАК НЕЛЬЗЯ!")
    
    print("Выбери оружие")
    choice = int(input("1 или 2:"))
    if choice == 1 and money >= 2500:
        gun1.info()
    elif choice == 2 and money == 5000:
        gun2.info()
    else:
        print("Нужны деньги.")

choosingrifle()
