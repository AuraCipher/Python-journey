menu = [
    "1.Pizza", "2.Pasta", "3.Burger", "4.Shawarma", "5.Nuggets", "6.Fries", "7.Drinks", "8.Coffee", "9.Sweets"
]
pizza_menu = [
    "1.Small Pizza: 5$","2.Medium Pizza: 10$","3.Large Pizza: 15$","4.Extra large Pizza: 20$"
]
pasta_menu = [
    "1.Chicken pasta: 10$", "2.Alfredo pasta: 15$", "3.Veg pasta: 20$"
]
Burger_menu = [
    "1.Chicken Burger: 10$", "2.Veg Burger: 7$", "3.Fries Burger: 5$", "4.Cheese Burger: 15$", "5.Zinger Burger: 20$"
]
Shawarma_menu = [
    "1.Chicken Shawarma: 15$", "2.Veg Shawarma: 10$", "3.Fries Shawarma: 15$", "4.Cheese Shawarma: 20$", "5.Beef Shawarma: 25$"
]
Nuggets_menu = [
    "1.Small Nuggets(6Pieces): 5$", "2.Medium Nuggets(12Pieces): 10$"
]
Fries_menu = [
    "1.Small Fries: 5$", "2.Medium Fries: 10$"
]
Drinks_menu = [
    "1.Coke: 5$", "2.Pepsi: 5$", "3.Water: 5$"
]
Coffee_menu = [
    "1.Cappuccino: 10$", "2.Latte: 15$", "3.Espresso: 20$"
]
Sweets_menu = [
     "1.Milkshake: 10$","2.Cake" ,"3.Ice Cream"
]
milkshake_menu = [
    "1.Chocolate Milkshake: 10$", "2.Cream Milkshake: 10$", "3.Pineapple Milkshake: 20$"
]
cakes_menu = [
    "1.Chocolate Cake: 15$", "2.Cream Cake: 15$", "3.Pineapple Cake: 20$"
]
ice_cream_menu = [
    "1.Vanilla Ice Cream: 10$", "2.Chocolate Ice Cream: 10$", "3.Strawberry Ice Cream: 10$"
]

def total_bill(total_payment):
    print("Thank you for your order! Have a great day!")
    print("Your total bill is", total_payment, "$")

print("Welcome to our restaurant!")
def main_menu():
    total_payment = 0
    while True:
        print("What would you like to order?\nHere is the menu.")
        for item in menu:
            print(item)
        order = input("Place your order(1,2,3,4,5,6,7,8,9):")
        if order == "1":
            print("List of Pizza")
            for pizza in pizza_menu:
                print(pizza)
            pizza_order = input("Which pizza would you like to order(1,2,3or4):")
            if pizza_order == "1":
                small_pizza_order = int(input("How much small pizza would you like to order(1,2,...,10):"))
                small_pizza_payment = small_pizza_order * 5
                total_payment += small_pizza_payment
                print("Cost of", small_pizza_order, "small pizza is", small_pizza_payment,"$")

            elif pizza_order == "2":
                medium_pizza_order = int(input("How much medium pizza would you like to order(1,2,...,10):"))
                medium_pizza_payment = medium_pizza_order * 10
                total_payment += medium_pizza_payment
                print("Cost of", medium_pizza_order, "medium pizza is", medium_pizza_payment,"$")

            elif pizza_order == "3":
                large_pizza_order = int(input("How much large pizza would you like to order(1,2,...,10):"))
                large_pizza_payment = large_pizza_order * 15
                total_payment += large_pizza_payment
                print("Cost of", large_pizza_order, "large pizza is", large_pizza_payment,"$")

            elif pizza_order == "4":
                extra_large_pizza_order = int(input("How much extra large pizza would you like to order(1,2,...,10):"))
                extra_large_pizza_payment = extra_large_pizza_order * 20
                total_payment += extra_large_pizza_payment
                print("Cost of", extra_large_pizza_order, "extra large pizza is", extra_large_pizza_payment,"$")
            else:
                print("Invalid pizza choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?(yes/no)")
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        elif order == "2":
            print("List of Pasta")
            for pasta in pasta_menu:
                print(pasta)
            pasta_order = input("Which pasta would you like to order(1,2,3):")
            if pasta_order == "1":
                chicken_pasta_order = int(input("How much chicken pasta would you like to order(1,2,...,10):"))
                chicken_pasta_payment = chicken_pasta_order * 10
                total_payment += chicken_pasta_payment
                print("Cost of", chicken_pasta_order, "chicken pasta is", chicken_pasta_payment,"$")

            elif pasta_order == "2":
                alfredo_pasta_order = int(input("How much alfredo pasta would you like to order(1,2,...,10):"))
                alfredo_pasta_payment = alfredo_pasta_order * 15
                total_payment += alfredo_pasta_payment
                print("Cost of", alfredo_pasta_order, "alfredo pasta is", alfredo_pasta_payment,"$")

            elif pasta_order == "3":
                veg_pasta_order = int(input("How much veg pasta would you like to order(1,2,...,10):"))
                veg_pasta_payment = veg_pasta_order * 20
                total_payment += veg_pasta_payment
                print("Cost of", veg_pasta_order, "veg pasta is", veg_pasta_payment,"$")
            else:
                print("Invalid pasta choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?(yes/no)").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        elif order == "3":
            print("List of Burger")
            for burger in Burger_menu:
                print(burger)
            burger_order = input("Which burger would you like to order(1,2,3,4,5):")
            if burger_order == "1":
                chicken_burger_order = int(input("How much chicken burger would you like to order(1,2,...,10):"))
                chicken_burger_payment = chicken_burger_order * 10
                total_payment += chicken_burger_payment
                print("Cost of", chicken_burger_order, "chicken burger is", chicken_burger_payment,"$")

            elif burger_order == "2":
                veg_burger_order = int(input("How much veg burger would you like to order(1,2,...,10):"))
                veg_burger_payment = veg_burger_order * 7
                total_payment += veg_burger_payment
                print("Cost of", veg_burger_order, "veg burger is", veg_burger_payment,"$")

            elif burger_order == "3":
                fries_burger_order = int(input("How much fries burger would you like to order(1,2,...,10):"))
                fries_burger_payment = fries_burger_order * 5
                total_payment += fries_burger_payment
                print("Cost of", fries_burger_order, "fries burger is", fries_burger_payment,"$")

            elif burger_order == "4":
                cheese_burger_order = int(input("How much cheese burger would you like to order(1,2,...,10):"))
                cheese_burger_payment = cheese_burger_order * 15
                total_payment += cheese_burger_payment
                print("Cost of", cheese_burger_order, "cheese burger is", cheese_burger_payment,"$")

            elif burger_order == "5":
                zinger_burger_order = int(input("How much zinger burger would you like to order(1,2,...,10):"))
                zinger_burger_payment = zinger_burger_order * 20
                total_payment += zinger_burger_payment
                print("Cost of", zinger_burger_order, "zinger burger is", zinger_burger_payment,"$")

            else:
                print("Invalid burger choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        if order == "4":
            print("List of Shawarma")
            for shawarma in Shawarma_menu:
                print(shawarma)
            shawarma_order = input("Which shawarma would you like to order(1,2,3,4,5):")
            if shawarma_order == "1":
                chicken_shawarma_order = int(input("How much chicken shawarma would you like to order(1,2,...,10):"))
                chicken_shawarma_payment = chicken_shawarma_order * 15
                total_payment += chicken_shawarma_payment
                print("Cost of", chicken_shawarma_order, "chicken shawarma is", chicken_shawarma_payment,"$")

            elif shawarma_order == "2":
                veg_shawarma_order = int(input("How much veg shawarma would you like to order(1,2,...,10):"))
                veg_shawarma_payment = veg_shawarma_order * 10
                total_payment += veg_shawarma_payment
                print("Cost of", veg_shawarma_order, "veg shawarma is", veg_shawarma_payment,"$")

            elif shawarma_order == "3":
                fries_shawarma_order = int(input("How much fries shawarma would you like to order(1,2,...,10):"))
                fries_shawarma_payment = fries_shawarma_order * 15
                total_payment += fries_shawarma_payment
                print("Cost of", fries_shawarma_order, "fries shawarma is", fries_shawarma_payment,"$")

            elif shawarma_order == "4":
                cheese_shawarma_order = int(input("How much cheese shawarma would you like to order(1,2,...,10):"))
                cheese_shawarma_payment = cheese_shawarma_order * 20
                total_payment += cheese_shawarma_payment
                print("Cost of", cheese_shawarma_order, "cheese shawarma is", cheese_shawarma_payment,"$")

            elif shawarma_order == "5":
                beef_shawarma_order = int(input("How much beef shawarma would you like to order(1,2,...,10):"))
                beef_shawarma_payment = beef_shawarma_order * 25
                total_payment += beef_shawarma_payment
                print("Cost of", beef_shawarma_order, "beef shawarma is", beef_shawarma_payment,"$")

            else:
                print("Invalid shawarma choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        elif order == "5":
            print("List of Nuggets")
            for nuggets in Nuggets_menu:
                print(nuggets)
            nuggets_order = input("Which nuggets would you like to order(1,2):")
            if nuggets_order == "1":
                small_nuggets_order = int(input("How much small nuggets would you like to order(1,2,...,10):"))
                small_nuggets_payment = small_nuggets_order * 5
                total_payment += small_nuggets_payment
                print("Cost of", small_nuggets_order, "small nuggets is", small_nuggets_payment,"$")

            elif nuggets_order == "2":
                medium_nuggets_order = int(input("How much medium nuggets would you like to order(1,2,...,10):"))
                medium_nuggets_payment = medium_nuggets_order * 10
                total_payment += medium_nuggets_payment
                print("Cost of", medium_nuggets_order, "medium nuggets is", medium_nuggets_payment,"$")

            else:
                print("Invalid nuggets choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        elif order == "6":
            print("List of Fries")
            for fries in Fries_menu:
                print(fries)
            fries_order = input("Which fries would you like to order(1,2):")
            if fries_order == "1":
                small_fries_order = int(input("How much small fries would you like to order(1,2,...,10):"))
                small_fries_payment = small_fries_order * 5
                total_payment += small_fries_payment
                print("Cost of", small_fries_order, "small fries is", small_fries_payment,"$")

            elif fries_order == "2":
                medium_fries_order = int(input("How much medium fries would you like to order(1,2,...,10):"))
                medium_fries_payment = medium_fries_order * 10
                total_payment += medium_fries_payment
                print("Cost of", medium_fries_order, "medium fries is", medium_fries_payment,"$")

            else:
                print("Invalid fries choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        elif order == "7":
            print("List of Drinks")
            for drinks in Drinks_menu:
                print(drinks)
            drinks_order = input("Which drinks would you like to order(1,2,3,4):")
            if drinks_order == "1":
                coke_order = int(input("How much coke would you like to order(1,2,...,10):"))
                coke_payment = coke_order * 5
                total_payment += coke_payment
                print("Cost of", coke_order, "coke is", coke_payment,"$")

            elif drinks_order == "2":
                pepsi_order = int(input("How much pepsi would you like to order(1,2,...,10):"))
                pepsi_payment = pepsi_order * 5
                total_payment += pepsi_payment
                print("Cost of", pepsi_order, "pepsi is", pepsi_payment,"$")

            elif drinks_order == "3":
                water_order = int(input("How much water would you like to order(1,2,...,10):"))
                water_payment = water_order * 5
                total_payment += water_payment
                print("Cost of", water_order, "water is", water_payment,"$")

            else:
                print("Invalid drinks choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        elif order == "8":
            print("List of Coffee")
            for coffee in Coffee_menu:
                print(coffee)
            coffee_order = input("Which coffee would you like to order(1,2,3):")
            if coffee_order == "1":
                cappuccino_order = int(input("How much cappuccino would you like to order(1,2,...,10):"))
                cappuccino_payment = cappuccino_order * 10
                total_payment += cappuccino_payment
                print("Cost of", cappuccino_order, "cappuccino is", cappuccino_payment,"$")

            elif coffee_order == "2":
                latte_order = int(input("How much latte would you like to order(1,2,...,10):"))
                latte_payment = latte_order * 15
                total_payment += latte_payment
                print("Cost of", latte_order, "latte is", latte_payment,"$")

            elif coffee_order == "3":
                espresso_order = int(input("How much espresso would you like to order(1,2,...,10):"))
                espresso_payment = espresso_order * 20
                total_payment += espresso_payment
                print("Cost of", espresso_order, "espresso is", espresso_payment,"$")

            else:
                print("Invalid coffee choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        elif order == "9":
            print("List of Sweets")
            for sweets in Sweets_menu:
                print(sweets)
            sweets_order = input("Which sweet dish would you like to order(1,2,3):")
            if sweets_order == "1":
                print("List of Milkshakes")
                for milkshakes in milkshake_menu:
                    print(milkshakes)
                    milkshakes_order = input("Which milkshake would you like to order(1,2,3,4,5):")
                    if milkshakes_order == "1":
                        chocolate_milkshake_order = int(input("How much Chocolate milkshake would you like to order(1,2,...,10):"))
                        chocolate_milkshake_payment = chocolate_milkshake_order * 10
                        total_payment += chocolate_milkshake_payment
                        print("Cost of", chocolate_milkshake_order, "chocolate milkshake is", chocolate_milkshake_payment,"$")
                    
                    elif milkshakes_order == "2":
                        strawberry_milkshake_order = int(input("How much Strawberry milkshake would you like to order(1,2,...,10):"))
                        strawberry_milkshake_payment = strawberry_milkshake_order * 15
                        total_payment += strawberry_milkshake_payment
                        print("Cost of", strawberry_milkshake_order, "strawberry milkshake is", strawberry_milkshake_payment,"$")
                        
                    elif milkshakes_order == "3":
                        pineapple_milkshake_order = int(input("How much Pineapple milkshake would you like to order(1,2,...,10):"))
                        pineapple_milkshake_payment = pineapple_milkshake_order * 20
                        total_payment += pineapple_milkshake_payment
                        print("Cost of", pineapple_milkshake_order, "pineapple milkshake is", pineapple_milkshake_payment,"$")
                        
                    else:
                        print("Invalid milkshake choice. Please try again.")
                        main_menu()
                    
                    route = input("Would you like to order anything else?").lower
                    if route == "yes":
                        main_menu()
                    else:
                        total_bill(total_payment)
                        break
            
            elif sweets_order == "2":
                print("List of Cakes")
                for cakes in cakes_menu:
                    print(cakes)
                    cakes_order = input("Which cake would you like to order(1,2,3,4,5):")
                    if cakes_order == "1":
                        chocolate_cake_order = int(input("How much Chocolate cake would you like to order(1,2,...,10):"))
                        chocolate_cake_payment = chocolate_cake_order * 10
                        total_payment += chocolate_cake_payment
                        print("Cost of", chocolate_cake_order, "chocolate cake is", chocolate_cake_payment,"$")
                    
                    elif cakes_order == "2":
                        cream_cake_order = int(input("How much Cream cake would you like to order(1,2,...,10):"))
                        cream_cake_payment = cream_cake_order * 15
                        total_payment += cream_cake_payment
                        print("Cost of", cream_cake_order, "cream cake is", cream_cake_payment,"$")
                    
                    elif cakes_order == "3":
                        pineapple_cake_order = int(input("How much Pineapple cake would you like to order(1,2,...,10):"))
                        pineapple_cake_payment = pineapple_cake_order * 20
                        total_payment += pineapple_cake_payment
                        print("Cost of", pineapple_cake_order, "pineapple cake is", pineapple_cake_payment,"$")
                        
                    else:
                        print("Invalid cake choice. Please try again.")
                        main_menu()
                    
                    route = input("Would you like to order anything else?").lower
                    if route == "yes":
                        main_menu()
                    else:
                        total_bill(total_payment)
                        break
                        
            elif sweets_order == "3":
                print("List of Ice creams")
                for ice_creams in ice_cream_menu:
                    print(ice_creams)
                    ice_creams_order = input("Which ice cream would you like to order(1,2,3,4,5):")
                    if ice_creams_order == "1":
                        vanilla_ice_cream_order = int(input("How much Vanilla ice cream would you like to order(1,2,...,10):"))
                        vanilla_ice_cream_payment = vanilla_ice_cream_order * 10
                        total_payment += vanilla_ice_cream_payment
                        print("Cost of", vanilla_ice_cream_order, "vanilla ice cream is", vanilla_ice_cream_payment,"$")

                    elif ice_creams_order == "2":
                        chocolate_ice_cream_order = int(input("How much Chocolate ice cream would you like to order(1,2,...,10):"))
                        chocolate_ice_cream_payment = chocolate_ice_cream_order * 15
                        total_payment += chocolate_ice_cream_payment
                        print("Cost of", chocolate_ice_cream_order, "chocolate ice cream is", chocolate_ice_cream_payment,"$")

                    elif ice_creams_order == "3":
                        strawberry_ice_cream_order = int(input("How much Strawberry ice cream would you like to order(1,2,...,10):"))
                        strawberry_ice_cream_payment = strawberry_ice_cream_order * 20
                        total_payment += strawberry_ice_cream_payment
                        print("Cost of", strawberry_ice_cream_order, "strawberry ice cream is", strawberry_ice_cream_payment,"$")

                    else:
                        print("Invalid ice cream choice. Please try again.")
                        main_menu()

                    route = input("Would you like to order anything else?").lower
                    if route == "yes":
                        main_menu()
                    else:
                        total_bill(total_payment)
                        break

            else:
                print("Invalid sweets choice. Please try again.")
                main_menu()

            route = input("Would you like to order anything else?").lower
            if route == "yes":
                main_menu()
            else:
                total_bill(total_payment)
                break

        else:
            print("Invalid menu selection. Please try again.")
            main_menu()

main_menu()
