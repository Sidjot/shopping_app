from operator import itemgetter
import uuid
session_id=0
user_type = None
granted = False
cart=[]
newlist2=[]
checkout=[]
category=[]
title=[]
product_list=[]
no_articles=[]
uom=[]
price=[]
stock=[]
newlist=[]

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
                category_in(catg_option)
                '''if catg_option==str(1): 
                    category_in(catg_option)
                elif catg_option==str(2):
                    pass
                    #remove_category()'''
            elif option==str(2):
                pass
                add_modify_item()
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
                
def add_modify_item():
    global newlist2
    while True:
        option=input("Please enter category number you want to modify(press q to quit)")
        cat_name=""
        flag = 0
        if option.lower() == "q":
            break
        for i in newlist2:
            print(i)
            if option == i[0]:
                cat_name = i[1]
                flag = 1
            break
        if flag == 0:
            print("Please enter proper category number")
        else:
            operation=input("1. Add item\n2. Modify quantity, price of item\n3. remove item(press q to quit)")
            if operation.lower() == "q":
                break
            elif operation == "1":
                nam = input("Please state the products' names: ")
                um= input("Please state the unit of measurement: ")
                rs = input("Please state the price of the product: ")
                qty = input("Please input the qty in stock: ")
                newlist2.append([option,cat_name,nam,um,"Rs."+rs,qty])
                write_to_file(newlist2)
            elif operation == "2":
                while True:
                    cat_name = input("Please enter product name(press q to quit)")
                    if cat_name.lower() == "q":
                        break
                    flag =0;
                    temp_item=[]
                    for i in range(len(newlist2)):
                        if newlist2[i][2].lower() == cat_name.lower():
                            flag = 1
                            index = i
                            break
                    if flag==0:
                        print("Please enter proper product name")
                    else:
                        option1=input("1. Modify Quantity\n2. Modify Price(press q to quit)")
                        if option1.lower() == "q":
                            break
                        elif option1 == "1":
                            while True:
                                new_qty=int(input("Please enter new quantity"))
                                if new_qty > 0:
                                    newlist2[index][5] = new_qty
                                    write_to_file(newlist2)
                                    print("Quantity updated successfully!")
                                    break
                                else:
                                    print("Please enter valid quantity")
                        elif option1 == "2":
                            while True:
                                new_price=int(input("Please enter new price"))
                                if new_price > 0:
                                    newlist2[index][4] = "Rs."+str(new_price)
                                    write_to_file(newlist2)
                                    print("Price updated successfully!")
                                    break
                                else:
                                    print("Please enter valid price")
                break
            elif operation == "3":
                while True:
                    prod_name = input("Please enter product name you want to remove(press q to quit)")
                    if prod_name.lower() == "q":
                        break
                    else:
                        temp_list=[]
                        flag =0
                        for i in newlist2:
                            if i[2].lower() == prod_name.lower():
                                flag = 1
                            else:
                                temp_list.append(i)
                                
                            
                        if flag == 0:
                            print("Please enter valid product")
                        else:
                            write_to_file(temp_list)
                            print("Product removed successfully!")
                            newlist2 = temp_list
                            break
                            
                        
                
                
def category_in(catg_option):
    while catg_option==str(1):
        cat_no=input("Please state the category numbers you would like (q to quit):")
        if cat_no!="q":
            category.append(cat_no)
            tit = input("Please input title of the category: ")
            title.append(tit)
            it_no = input("Please state no. of articles in this category: ")
            no_articles.append(int(it_no))
            for i in range (int(it_no)):
                nam = input("Please state the products' names: ")
                product_list.append(nam)
                um= input("Please state the unit of measurement: ")
                uom.append(um)
                rs = input("Please state the price of the product: ")
                price.append(rs)
                qty = input("Please input the qty in stock: ")
                stock.append(qty)
                
                
            
        else:
            if len(title)>0:
                sum_no=[sum(no_articles[:i+1]) for i in range(len(no_articles))]
                print("The categories introduced are: ")
                print(no_articles)
                print(product_list)
                print(sum_no)
                with open("NewFile.txt","w")as NewFile:
                    for i in range (len(category)):
                        if i-1>=0: 
                            get=itemgetter(slice(sum_no[i-1],sum_no[i]))
                            p=get(product_list)
                            z=get(uom)
                            q=get(price)
                            r=get(stock)
                            for j in range(len(p)):
                                record=str(category[i])+","+str(title[i])+","+str(p[j])+","+str(z[j])+","+"Rs."+str(q[j])+","+str(r[j])+"\n"
                                NewFile.write(record)
                        else:
                            get = itemgetter(slice(0,sum_no[i]))
                            p=get(product_list)
                            z=get(uom)
                            q=get(price)
                            r=get(stock)
                            for j in range(len(p)):
                                record=str(category[i])+","+str(title[i])+","+str(p[j])+","+str(z[j])+","+"Rs."+str(q[j])+","+str(r[j]+"\n")
                                NewFile.write(record)
            break
    
            
    while catg_option==str(2):
        cat_no=input("Please state the category you would like to remove: ")
        filtered_items=[]
        create_items()
        for item in newlist2:
            if int(item[0]) != int(cat_no):
                filtered_items.append(item)
        write_to_file(filtered_items)
        break
    create_items()
def write_to_file(items):
    with open("NewFile.txt","w")as NewFile:
        for item in items:
            NewFile.write(get_string(item)+"\n")
                
def get_string(item):
    temp=""
    for i in item:
        if temp == "":
            temp=i
        else:
            temp=temp+","+str(i)
    
    return temp       

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
    with open("NewFile.txt","r") as NewFile:
        f=NewFile.readlines()
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

def payment_method():
    global checkout
    s=get_sum(checkout)
    while s!=0:
        pay=input("Please select payment method:\n 1. Credit Card \n 2. UPI \n 3. Debit Card (1/2/3 - q to quit) ")
        print(type(pay))
        if pay=="1" or pay=="2" or pay=="3":
            print("Your bill total of Rs ",s,"has been booked. Thank you for shopping at JeremyJohn!")
            s=0
            break
        elif pay.lower() == "q" and s!=0:
            print("Please complete your payment")
    print("We look forward to see you again soon!")
def reduce_from_stock():
    global newlist2
    for i in cart:
        for j in range(len(newlist2)-1):
            if i[0].lower() == newlist2[j][2].lower():
                newlist2[j][5] = newlist2[j][5] - i[1]
                break
def checkOut():
    #print (newlist2)
    reduce_from_stock()
    global checkout
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
    payment_method()
       
        
#############################################################################
begin()
access(option)
if granted:
    print("Welcome : "+name)
    show_options()
