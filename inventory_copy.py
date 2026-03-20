

#========The beginning of the class==========
class Shoe:


    def __init__(self, country, code, product, cost, quantity):
        self.country  = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
        '''
        In this function, you must initialise the following attributes:
            ● country,
            ● code,
            ● product,
            ● cost, and
            ● quantity.
        '''
    def get_cost(self):
        try:
            return int(self.cost)
        except:
            print (f"{self.cost} is not an integer")
        '''
        Add the code to return the cost of the shoe in this method.
        '''


    def get_quantity(self):
        try:
            return int(self.quantity)
        except:
            print (f"{self.quantity} is not an integer")
        '''
        Add the code to return the quantity of the shoes.
        '''


    def __str__(self):
        return (f'{self.country} | {self.code} | {self.product} | ${self.cost} | #{self.quantity}')
        '''
        Add a code to returns a string representation of a class.
        '''


#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []

#==========Functions outside the class==============

def read_shoes_data():
    with open("inventory.txt", "r+") as file:
        for line, data in enumerate(file):
            if data == 0:
                continue    
            else:
                for line in file:
                    remove = line.rstrip('\n') #remove \n at the end of each nested list
                    split = remove.split(",") #split each string by category
                    shoe_list.append(split)
                    display.append(split)
    for col in shoe_list:
        try: 
            col[3] = int(col[3])
            col[4] = int(col[4])
#Convert columns on index 3 and 4 into integers
        except: 
            pass  #ignoring strings/non-integers

'''
    This function will open the file inventory.txt
    and read the data from this file, then create a shoes object with this data
    and append this object into the shoes list. One line in this file represents
    data to create one object of shoes. You must use the try-except in this function
    for error handling. Remember to skip the first line using your code.
    '''
def capture_shoes():
    try: 
        new_shoe = [] #create new list for new shoe
        country = input("Country: ")
        c = country.upper() #to match the rest of the products as uppercase
        new_shoe.append(c) #add to new list
        #product country
        code = input("Code: ")
        d = code.upper()
        new_shoe.append(d)
        #product code
        product = input("Product: ")
        p = product.upper()
        new_shoe.append(p)
        #product name
        cost = int(input("Cost: "))
        new_shoe.append(cost)
        #product cost
        quantity = int(input("Quantity: "))
        new_shoe.append(quantity)
        #product quantity
        shoe_list.append(new_shoe) #add new product to shoe_list
        print ("\nUpdated list below:")
        view_all()
    except: 
        print ("Unable to add shoe") 
    
    '''
    This function will allow a user to capture data
    about a shoe and use this data to create a shoe object
    and append this object inside the shoe list.
    '''


def view_all():
    print ("Country |", "Code |", "Product |", "Cost |", "Quantity \n")
    for sublist in display:
        sublist = Shoe(*sublist)
        print (sublist)
    print ("\n")
    '''
    This function will iterate over the shoes list and
    print the details of the shoes returned from the __str__
    function. Optional: you can organise your data in a table format
    by using Python’s tabulate module.
    '''

def re_stock():
    shoe_list.sort(key=lambda x:x[4])
    #sorted from smallest to greatest quantity
    print (shoe_list[0])
    stock = input("Would you like to restock this product? Y/N? ")
    stock.lower()
    if stock == 'y':
        plus = int(input("How many is being added? ")) #request amount to add
        shoe_list[0][4] += plus #replace with combined value 
    else:
        print ("Goodbye")
    print("Product has been updated to:")
    print (f'{shoe_list[0]} + \n') #display updated quantity

    '''
    This function will find the shoe object with the lowest quantity,
    which is the shoes that need to be re-stocked. Ask the user if they
    want to add this quantity of shoes and then update it.
    This quantity should be updated on the file for this shoe.
    '''


def search_shoe():
    code = input("\nWhat is the code of the product? ")
    #code.upper()
    found = False
    for sublist in shoe_list:
        if code in sublist: #search in nested list
            found = True
            print (f"{sublist}")
    if not found: #if not found
        print ("Unable to find code")    
    again = input("Try again? Y/N? ") #search again? or return to main menu
    again.lower()
    if again =='y':
        search_shoe()
    else:
        print ("\n")
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    for sublist in shoe_list:
        value = sublist[3] * sublist[4] #multiply cost and quantity
        print (f"{sublist[2]}'s value is ${value}")
    print ("\n")

    '''
    This function will calculate the total value for each item.
    Please keep the formula for value in mind: value = cost * quantity.
    Print this information on the console for all the shoes.
    '''


def highest_qty():
    shoe_list.sort(key=lambda x:x[4], reverse=True)
    #sort from greatest to smallest quantity
    print (f"\n{shoe_list[0][2]} is on sale.\n")
    '''
    Write code to determine the product with the highest quantity and
    print this shoe as being for sale.
    '''

#==========Main Menu=============
'''
Create a menu that executes each function above.
This menu should be inside the while loop. Be creative!
'''
def inventory():
    while True:
        check = input("Would you like to check inventory? \nYes/No? ")
        check.lower()
        if check == 'yes':
            print ("\nWhat would you like to do?")
            type = int(input("1-See all product, 2-Other, 3-End \n"))
            try:
                if type == 1:
                    view_all()  
                elif type == 2:
                    print ("\nChoose a category by number:")
                    print ("1-Add Shoe, 2-Re-stock, 3-Search by code, 4-Product value, 5-Sale Item")
                    category = int(input("Enter your selection: "))
                    try:
                        if category == 1:
                            capture_shoes()
                        elif category == 2:
                            re_stock()
                        elif category == 3:
                            search_shoe()
                        elif category == 4:
                            value_per_item()
                        elif category == 5:
                            highest_qty()
                    except:
                        print ("Unable to verify selection: Try again. \n")    
                        inventory() 
                else:
                    print("Goodbye! ")
            except():
                print("That is not an option. Try again")
                inventory()
        elif check == 'no':
            print ("Goodbye!")
            exit()
        else: 
            print ("Invalid input. Please try again")
            inventory()

display = []

read_shoes_data()
inventory()