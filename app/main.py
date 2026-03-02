from models.customer import Customer
from models.accounts import Account




customer_db = {}
cos_id = 1









    
def create_customer():

    global cos_id

    name = input("Enter Your Name:")
    phone = input("Enter Your Phone No. :")
    email = input("Enter Your Email:")
    cid = cos_id
    cos_id = cos_id+1
    
    customer_obj = Customer(name,phone,email,cid)
    customer_db[cid] = customer_obj    
    
    
create_customer()


pass





    