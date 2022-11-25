import os

if not os.path.exists("passwords"):
    os.mkdir("passwords")

def main():
    salt = input("Welcome to passman.\nEnter Salt (master password): ")
    usrinput = input("Choose option 1 to encrypt passwords.\nChoose option 2 to unencrypt passwords.\nOption: ")

    if usrinput == "1":
        name = input("Enter name of password: ")
        
        if not os.path.exists(f'passwords/{name}.pass'):  
            password = input("Enter the password: ")
            string = password + salt
            key = ""
            saltnum = 0

            for j in salt:
                saltnum += ord(j)

            for i in string:
                k = ord(i) - saltnum
                key += str(k) + "."
                    
            key = key.removesuffix(".")

            f = open(f'passwords/{name}.pass', "x")
            f.write(key)
            f.close()
        else:
            print("Password already exists! Delete the file and try again.")
         
    if usrinput == "2":
        name = input("Enter name of password: ")
        password = ""
        if os.path.exists(f'passwords/{name}.pass'):
            f = open(f'passwords/{name}.pass', "r")
            string = f.read()
            split_string = string.split('.')

            ascii = ""
            
            saltnum = 0

            for j in salt:
                saltnum += ord(j)

            for i in split_string:
                k = int(i) + saltnum
                ascii += str(k) + "."       

            ascii = ascii.removesuffix(".")

            split_ascii = ascii.split('.')

            decrypted = ""

            for i in split_ascii:
                j = chr(int(i))
                
                decrypted += j
            
            decrypted = decrypted.removesuffix(salt)

            print(f'Password decrypted: {decrypted}')
        else:
            print("Password doesn't exist!")

main()