import pymysql
class Customer:
    con=pymysql.connect(host='localhost',user='root',password='sushant',database='myspace')
   # mycursor=con.cursor()


    def __init__(self):
        self.id=0
        self.name=""
        self.mobile=0
        self.age=0
    def addcust(self):
        mycursor = Customer.con.cursor()
        strquery="insert into customer values(%s,%s,%s,%s)"
        mycursor.execute(strquery,(self.id,self.name,self.age,self.mobile))
        Customer.con.commit()




    def searchcust(self):
        mycursor=Customer.con.cursor()
        strquery="select * from customer where id=%s"
        rowaffected=mycursor.execute(strquery,(self.id))
        data=mycursor.fetchone()
        self.name=data[1]
        self.age=data[2]
        self.mobile=data[3]
        if(rowaffected==0):
            raise Exception("id doesnt exist")





    def deletecust(self):
        mycursor=Customer.con.cursor()
        strquery="delete from customer where id=%s"
        rowaffected=mycursor.execute(strquery,(self.id))
        Customer.con.commit()

    def modify(self):
        mycursor=Customer.con.cursor()
        strquery="update customer set name=%s,age=%s,mobile=%s where id=%s"
        rowaffected=mycursor.execute(strquery,(self.name,self.age,self.mobile,self.id))
        Customer.con.commit()
        if(rowaffected==0):
            raise Exception("id doesnt exist")


    def display(self):
        mycursor=Customer.con.cursor()
        strquery="select * from customer"
        mycursor.execute(strquery)
        for row in mycursor.fetchall():
            for cell in row:
                print(cell,end='\t')
            print()

#if(__name__=="_main_"):
while (1):

    print("1: to add new customer")
    print("2:to search customer by id")
    print("3:to delete customer by id")
    print("4:to modify customer")
    print("5:display all customers")
    print("6:exit")

    ch = input("enter ur choice u wish to do")
    if (ch == "1"):

        cus=Customer()
        cus.id=input("enter id")
        cus.name=input("enter name")
        cus.age=input("enter age")
        cus.mobile=input("enter mobileno")
        cus.addcust()
    elif(ch=="2"):

        try:


            cus=Customer()
            cus.id=input("enter id to be searched")
            cus.searchcust()
            print("customer name",cus.name,"\t customer age",cus.age,"\t customer mobileno",cus.mobile)
        except Exception as ex:
            print(ex)
    elif(ch=="3"):
        cus=Customer()
        cus.id=input("enter id to be deleted")
        cus.deletecust()
    elif(ch=="4"):
        try:
            cus=Customer()
            cus.id=input("enter id to be modified")
            cus.name=input("enter new name")
            cus.age=input("enter new age")
            cus.mobile=input("enter new mobileno")

            cus.modify()
        except Exception as ex:
            print(ex)

    elif(ch=="5"):
        cus=Customer()
        cus.display()
    elif(ch=="6"):
        exit()
