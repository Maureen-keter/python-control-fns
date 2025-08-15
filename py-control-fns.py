def calculate_discount(price, discount_percent):
    if discount_percent < 20:
        return price
    else:
        discounted_price=price- price*discount_percent/100
        return discounted_price
    
try:        
        price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage: "))
        discounted_price = calculate_discount(price, discount_percent)
        if discount_percent < 20:             
            print(f"No discount applied. The price remains: {discounted_price}")
        else:
            print(f"The price after discount is: {discounted_price}")
except ValueError:
    print("Invalid input! Please enter numeric values.")
     


    