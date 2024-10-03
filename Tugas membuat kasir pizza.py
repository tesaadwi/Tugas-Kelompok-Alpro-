#welcoming sentence for user
print("===Welcome to pizza king===")
print("let me help you to order pizza here")

total_price = 0;

#showing the user a pricelist topping in pizza king
print("===first, choose the topping !===")
print("""===Topping pricelist in pizza king===
      1. Pepperoni  = Rp 12.000
      2. Sausage    = Rp 10.000
      3. Mushroom   = Rp 9.000
      4. Sweet Corn = Rp 8.000
      ======================================""")

#let the user choose the topping
topping_number = float(input("So, input the number of toppings you want to order:"))

#this line of code's for process the user input about topping
#user input will showed in final bill
if topping_number == 1:
  topping = "Pepperoni"
  topping_price = "Rp 12.000"
  total_price += 12000

elif topping_number == 2:
  topping = "Sausage"
  topping_price = "Rp 10.000"
  total_price += 10000

elif topping_number == 3:
  topping = "Mushroom"
  topping_price = "Rp 9.000"
  total_price += 9000

elif topping_number == 4:
  topping = "Sweet corn"
  topping_price = "Rp 8.000"
  total_price += 8000

else: "please, add the toppings according to the instructions"
print("topping choosed")

#showing the user a pricelist of crust
print("===now choose the Crust===")
print("""===Crust pricelist in pizza king===
      1. Pan Crust    = Rp 9.000
      2. Cheesy Crust = Rp 15.000
      3. Chilli Cheesy Stuffed Crust = Rp 20.000
      4. Crown Crust Carnival= Rp 23.000
      ======================================""")

#user input after they look at the pricelist
crust_number = float(input("So, input the number of Crust you want to order:"))

#this line of code's for process the user input about crust
#user input will showed in final bill
if crust_number == 1:
  crust = "Pan Crust"
  crust_price = "Rp 9.000"
  total_price += 9000

elif crust_number == 2:
  crust = "Cheesy Crust"
  crust_price = "Rp 15.000"
  total_price += 15000

elif crust_number == 3:
  crust = "Chilli Cheesy Stuffed Crust"
  crust_price = "Rp 20.000"
  total_price += 20000

elif crust_number == 4:
  crust = "Crown Crust Carnival"
  crust_price = "Rp 23.000"
  total_price += 23000

else: "please, add the crust according to the instructions"

#pricelist of Size
print("===now choose the Size===")
print("""===Size pricelist in pizza king===
      1. Personal (for 1 person) = Rp 30.000
      2. Regular (for 2 persons)  = Rp 50.000
      3. Jumbo (for 4 persons )    = Rp 65.000
      ======================================""")

#user input for Size of pizza
size_number = float(input("So, input the number of Size you want to order:"))

#this line of code's for process the user input about Size
#user input will showed in final bill
if size_number == 1:
  size = "Personal"
  size_price = "Rp30.000"
  total_price += 30000

elif size_number == 2:
  size = "Regular"
  size_price = "Rp50.000"
  total_price += 50000

elif size_number == 3:
  size = "Jumbo"
  size_price = "Rp65.000"
  total_price +=65000

#offering some extra topping
print(" do you want to add some cheese only for Rp 8.000 ?")
cheese = input("input (yes) or (no) for aggre or disagree: ")

if cheese == "yes":
 cheese_price = "Rp 8.000"
 total_price += 8000

elif cheese == "no":
  cheese_price = "0"
  total_price += 0



#showing the final bill 

print(f"""======================================
Topping     : {topping} {topping_price}
Crust       : {crust}   {crust_price}
Size        : {size}    {size_price}
extra cheese: {cheese}  {cheese_price}
------------------------------------------
your Final Bill :       Rp{total_price}
""")


            
 






