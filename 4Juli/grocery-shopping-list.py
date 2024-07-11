items = [
    ('diapers', 10.00),
    ('peanuts', 5.00),
    ('butter', 6.25),
    ('cheese', 3.00),
    ('milk', 3.5),
    ('yogurt', 1.99),
    ('eggs', 4.5),
    ('bread', 4), 
    ('shrimp', 2.5),
    ('coffee', 1.5)
]

money = 65
menu = ('buy', 'return', 'quit')
cartList = [] # empty list

def buyProduct(item,price):
    global money
    money = money - price
    cartList.append(item)

def returnProduct(item,price):
    global money
    money = money + price
    cartList.remove(item)

while menu != "quit":
    print("""
            Diapers ....10.00
            Peanuts ....5.00
            Butter .....6.25
            Cheese .....3.00
            Milk .......3.50
            Yogurt .....1.99
            Eggs .......4.50
            Bread ......4.00
            Shrimp .....2.50
            Coffee .....1.50
            """)
    menu = input("Welcome! What do you want to do?\nbuy / return / quit : ").lower()

    if menu == "buy":
        product = input("What do you want to buy? ")
        for i in items:
            if i[0] == product:
                confirm = input(f"Do you want to buy {i[0]} for {i[1]}? y/n ")
                if confirm == 'y':
                    buyProduct(i,i[1])
                    print(f"Your current money is {money}")
                    print(f"Your have just bought {cartList}")
                else:
                    print("You can buy another product!")
    elif menu == "return":
        product = input("What product do you want to return? ")
        for i in items:
            if i[0] == product:
                confirm = input(f"Do you want to return {i[0]} for {i[1]}? y/n ")
                if confirm == 'y':
                    returnProduct(i,i[1])
                    print(f"Your current money is {money}")
                    print(f"Your have just bought {cartList}")
                else:
                    print("You can buy another product!")
    else:
        print("Thank You")