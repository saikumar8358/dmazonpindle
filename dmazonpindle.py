import pymysql
import os

username = "root"
password = ''
host = "localhost"
database = "dmazonpindle"

conn = pymysql.connect(host,username,password,database)
cur = conn.cursor()

response = input('''
        1.sign up
        2.Log in
        3.more features
    ''')
if response == "1":
    print("register to login")

    username = input("Enter your username: ")
    password = input("Enter your password: ")
    Conformyourpassword = input("Re-enter your password: ")
    Mobilenumber = input("enter your mobile number: ")
    Emailid = input("Enter your email-id: ")
    query = "INSERT INTO sign_up values('%s','%s','%s','%s','%s')"%(username,password,Conformyourpassword,Mobilenumber,Emailid)
    cur.execute(query)
    print("values inserted successfully")
    conn.commit()
elif  response == "2":
    username = input("enter your username: ")
    password = input("enter your password: ")

    query = "select*FROM sign_up"

    cur.execute(query)

    data = cur.fetchall()

    for i in data:
        if username == str(i[0]) and password == str(i[1]):
            print("you are logged in!....")
        conn.commit( )

    response = input("""
                    1.Telugu
                    2.English
                    3.Hindi
                    4.Tamil
                    5.Kannada
                    """)

    if response == "1":
        print("here are you go...!!!! search for telugu")
        try:
            con = pymysql.connect('localhost', 'root', '', 'dmazonpindle')
            import math, random
            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP
            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                           enter a valid OTP
                            TRY AGAIN......""")
                exit()
                cur = con.cursor()
            cur.execute("select * from telugu")

            telugu = cur.fetchall()
            print(telugu[0])
            for i in telugu:


                print(i)
                file = open('destination1/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])

        except Exception as e:
            print(e)
    elif response == "2":
        print("here you goo..!!!!!search for English")
        try:
            con = pymysql.connect('localhost', 'root', '', 'dmazonpindle')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")

            cur = con.cursor()
            print("test")
            cur.execute("select * from english")

            english = cur.fetchall()
            print(english[0])
            for i in english:


                print(i)
                file = open('destination1/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)

    elif response == "3":
        print("here you goo.....!!!!!search for hindi")
        try:
            con = pymysql.connect('localhost', 'root', '', 'dmazonpindle')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")

            cur = con.cursor()
            print("test")
            cur.execute("select * from hindi")

            hindi = cur.fetchall()
            print(hindi[0])
            for i in Hindi:


                print(i)
                file = open('destination1/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)

    elif response == "4":
        print("here you goo.......!!!!!search for tamil ")
        try:
            con = pymysql.connect('localhost', 'root', '', 'dmazonpindle')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")
                exit()
            cur = con.cursor()
            print("test")
            cur.execute("select * from tamil")

            tamil = cur.fetchall()
            print(tamil[0])
            for i in tamil:


                print(i)
                file = open('destination1/' + i[0] + "." + i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)

    elif response == "5":
        print("here you  gooo.....!!!!!search for kannada")
        try:
            con = pymysql.connect('localhost', 'root', '', 'dmazonpindle')
            import math, random


            def generateOTP():
                digits = "0123456789"
                OTP = ""
                for i in range(4):
                    OTP += digits[math.floor(random.random() * 10)]
                return OTP


            if __name__ == "__main__":
                print("OTP of 4 digits:", generateOTP())
            print("enter ur OTP for validation")
            otp = int(input("enter ur OTP"))
            a = int(generateOTP())
            print(a)
            b = int(input("enter val"))
            print(type(a))
            if a == b:
                print("okay")
            else:
                print("""
                                       enter a valid OTP
                                        TRY AGAIN......""")
                exit()
            cur = con.cursor()
            print("test")
            cur.execute("select * from kannada")

            kannada = cur.fetchall()
            print(kannada[0])
            for i in kannada:

                print(i)
                file = open('destination1/' + i[0] +"."+i[1], 'wb')
                file.write(i[2])
        except Exception as e:
            print(e)
elif response =="3":
    response = input("""
                 1.explore more catogiries 
                 2.singout
                  """)

    if response == "1":
     print("explore for more catogiries re-login")
    elif response == "2":
        print("ur singned out")
    files = os.listdir('destination1')

    print(files)

    print(type(files))

    for i in range(len(files)):
        os.remove('destination1/' + files[i])
        exit()
else:
    print("invalid selection")
    exit()
