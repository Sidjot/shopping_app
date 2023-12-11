import uuid
session_id=0
user_type = None
granted = False
cart=[]
newlist2=[]
def grant():
    global granted
    granted = True

def login (name,password):
    global session_id
    global user_type
    success=False
    reg=[]
    with open("Register.txt","r") as Register:
        for i in Register:
            reg.append(i[:-1])
        reg2=[(i.split(","))for i in reg]
        for item in reg2:
            if item[0]==name and item[1]==password:
                user_type=item[2]
                session_id= uuid.uuid4()
                success=True
                create_items()
                break
        if success:
            print("Login Successful!!!")
            grant()
        else:
            print("Wrong username or password")
            access(option)       
        
def register(name, password,flag):
    with open("Register.txt","a")as Register:
        Register.write(name+","+password+","+str(flag)+"\n")
        grant()
        
def access(option):
    global name
    if option.lower() == "login":
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        login(name,password)
    else:
        print("Enter your name and password to register")
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        admin_flag = input("Is this admin registration?(Yes/No)")
        if admin_flag.lower()=="yes":
            register(name,password,1)  #1 for admin
        else:
            register(name,password,0)  #0 for customer
            
        
        print("Registration succesfull!!")
    
def begin():
    global option
    print("Welcome to JohnJeremy Shoppee","\n","Please choose one of the 2 options")
    option = input("Login or Register (Login, Reg): ")
    if option.lower()!= "login" and option.lower()!="reg":
        begin()
    
def show_options():
    if user_type==str(1):
        while True:
            option=input("Please select option\n 1. Add/Remove Category \n 2. Add/Modify/Remove item in category \n 3. Display all items\n 4. Logout:(1/2/3/4) ")
            if option==str(1):
                catg_option=input("Please select option \n 1. Add Category \n 2. Remove Category: (1/2)")
                if catg_option==str(1):
                    pass
                    #add_category()
                elif catg_option==str(2):
                    pass
                    #remove_category()
            elif option==str(2):
                pass
                #add_modify_item
            elif option== str(3):
                show_all_items()
            elif option==str(4):
                logout()
                break
            else:
                print("Please select input from list","\n")
                show_options()
    else:
        while True:            
            option = input("Please select option: 1. See all available items \n 2. Add item to cart \n 3. Remove item from cart \n 4. Bill generation and checkout \n 5. Logout")
            if option == str(1):
                show_all_items()
            elif option == str(2):
                add_item_cart()
            elif option == str(3):
                remove_item_cart()
            elif option == str(4):
                checkOut()
                
            elif option == str(5):
                logout()
                break
            else:
                print("Please select input from list","\n")
                show_options()
            
def logout():
    global session_id
    global user_type
    global granted
    global cart
    session_id=0
    user_type = None
    granted = False
    cart=[]
    print("You have been successfully logged out")
        
def create_items():
    global newlist2
    with open("MyFile.txt","r") as MyFile:
        f=MyFile.readlines()
        newlist=[]
        for line in f:
            if line[-2]== '-':
                #newlist.append(line[:-27])
                pass
            else:
                newlist.append(line[:-1])
        newlist2=[str(catg).split(",") for catg in newlist]
        
def show_all_items():        
        for item in newlist2:
            print(item[2],"Available Qty: ",item[5]," ", item[3]," ",item[4],"\n")
 
def add_item_cart():
    for item in newlist2:
            print(item[2],"Available Qty: ",item[5]," ", item[3]," ",item[4],"\n")
    while True:
        option = input("Please select item(Press 'q' to quit)")
        flag=0
        for item in newlist2:
            if option.lower()== item[2].lower():
                flag=1
                quantity = int(input ("Please enter qty of items: "))
                add_to_cart(option,quantity)
                break
        if flag==0:
            print("Please select valid item")
        if option.lower() == "q":
            break
            
    print("Items in cart: ",cart)

def add_to_cart(option,quantity):
    global cart
    flag=0
    for i in cart:
        if i[0].lower() == option.lower():
            for item in newlist2:
                if item[2].lower()==option.lower():
                    if int(item[5]) > (int(i[1]) + int(quantity)):
                        i[1] = int(i[1]) + int(quantity)
                        flag=1
                        return cart
                    else:
                        print("Quantity exceeds available stock")
                        flag = 1
                        break             
            
    if flag ==0:
        cart.append([option,quantity])
    print("Items in cart: ",cart)

def remove_item_cart():
    flag=0
    global cart
    while True:
        for i in cart:
            print(i[0], i[1])
        option = input("Please slect item you want to remove(Press 'q' to quit)")
        if option.lower() == "q":
            break
        for i in cart:
            if option.lower() == i[0].lower():
                flag = 1
                qty = input("How much quantity you want to remove")
                if int(qty)<0 or int(qty) > int(i[1]):
                    print("Please enter valid quantity")
                else:
                    i[1] = int(i[1])-int(qty)
        if flag ==0:
            print("Please select valid item")
    print(cart)
def get_sum(numbers,n=3):
    if len(numbers)<n:
        return 0
    return numbers[n-1]+get_sum(numbers[n:])

def checkOut():
    #print (newlist2)
    checkout =[]
    for item in cart:
        print (item)
        for art in newlist2:
            if item[0].lower()==art[2].lower():
                pr=[]
                pr.append(art[4].split("."))
                print (pr)
                checkout.append(item[0])
                checkout.append(item[1])
                checkout.append(int(item[1])*int(pr[0][1]))
    print(checkout,"\n", "Your total is Rs.: ", get_sum(checkout))
       
        
#############################################################################
begin()
access(option)
if granted:
    print("Welcome : "+name)
    show_options()


