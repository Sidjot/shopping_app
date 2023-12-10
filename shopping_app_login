import uuid
session_id=0
user_type = None
granted = False
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
            register(name,password,1)
        else:
            register(name,password,0)
            
        
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
                pass
                #Add_item_cart()
            elif option == str(3):
                pass
                # Remove_item_cart()
            elif option == str(4):
                pass
                #Bill_checkout()
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
    session_id=0
    user_type = None
    granted = False
    print("You have been successfully logged out")
        
def show_all_items():
    with open("MyFile.txt","r") as MyFile:
        f=MyFile.readlines()
        newlist=[]
        for line in f:
            if line[-2]== '-':
                #newlist.append(line[:-27])
                pass
            else:
                newlist.append(line[:-1])

                
       # for line in newlist:
           # newlist2=[str(catg).split(",") for catg in newlist]
        newlist2=[str(catg).split(",") for catg in newlist]
        
        for item in newlist2:
            print(item,"\n")
        
#################################################################################
begin()
access(option)
if granted:
    print("Welcome : "+name)
    show_options()


