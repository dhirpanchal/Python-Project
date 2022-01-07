class FoodOrdering():
    def __init__(self):
        self.food_id=0
        self.dict_foodlist={}
        self.user_registration_details={}
        self.login_credentials={}

    def add_food_item(self,name,price,quantity):  
        name=input("Enter name of item:")
        price=input("Enter Price:")
        quantity=input("Enter Quantity:")                
        self.food_id+=1
        self.dict_foodlist[self.food_id]=[name,price,quantity]
        
    def edit_food_item(self,foodid,name1,price1,quantity1):
        foodid=input("Enter Food ID:")
        name1=input("Enter name of food item;")
        quantity1=input("Enter Quantity;")
        self.dict_foodlist[foodid]=[name1,price1,quantity1]
        
    def remove_food_item(self,foodid):
        foodid=input("Enter Food ID:")
        del self.dict_foodlist[foodid]

    def user_registration(self,name,email_id,phone,address,password):
        name=input("Enter your name:")
        email_id=input("Enter your Email ID:")
        phone=input("Enter your Phone number:")
        address=input("Enter address:")
        password=input("Enter password:")
        self.user_registration_details[email_id]=[name,phone,address,password]
        self.login_credentials[email_id]=password

    def user_login(self,email_id,password):
        email_id=input("Enter your email ID:")
        password=input("Enter Paswword:")
        if self.login_credentials[email_id]==password:
            print("Login Successful")
        else:
            print("Invalid Credentials")

    def show_list_of_food(self):
        print(self.dict_foodlist)

    def place_order(self,foodid1,ordered_quantity):
        foodid1=input("Enter Food ID:")
        ordered_quantity=int(input("Quantity:"))
        self.dict_foodlist[foodid1][2]-ordered_quantity
    
    def order_history(self,foodid2,quantity2):
        pass
    
    def update_profile(self):
        email_id=input("Enter email ID:")
        password=input("Enter Password:")
        name=input("Enter name:")
        phone=input("Enter Phone:")
        address=input("Enter address:")
        if self.login_credentials[email_id]==password:
            self.user_registration_details[email_id]=[name,phone,address,password]


m1=FoodOrdering()

while True:
    user_input=int(input("1. Admin \n 2. User Login\n"))
    if user_input==1:
        user_input1= int(input("1.Add Food Item \n 2.Edit Food Item \n 3.Remove food item \n 4.Show list of food \n 5.Exit \n"))
            
        if user_input1==1:
            m1.add_food_item()
        elif user_input1==2:
            m1.edit_food_item()
        elif user_input1==3:
            m1.remove_food_item()
        elif user_input1==4:
            m1.show_list_of_food()
        elif user_input1==5:
            print("You have exit")
            break
        else:
            print("Invalid Input")
    
    if user_input==2:
        user_input2=int(input("1.Register \n 2.Login \n "))
        if user_input2==1:
            m1.user_registration()
        elif user_input2==2:
            a=m1.user_login()
            if a=="Login Successful":
                user_input3=int(input("1.Show Menu \n 2.Place Order \n 3.Order history \n 4.Edit Profile"))
                if user_input3==1:
                    m1.show_list_of_food()
                elif user_input3==2:
                    m1.place_order()
                elif user_input3==3:
                    m1.order_history()
                elif user_input3==4:
                    m1.update_profile()

    



m1=FoodOrdering()


        
m1=FoodOrdering()
m1.add_food_item("cake","200rs",2)
m1.add_food_item("pizza","400rs",1)
m1.add_food_item("burger","150rs",5)
print(m1.dict_foodlist)
m1.edit_food_item(2,"chapati",633,8)
print(m1.dict_foodlist)
m1.remove_food_item(2)
print(m1.dict_foodlist)