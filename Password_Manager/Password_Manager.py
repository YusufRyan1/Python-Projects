from cryptography.fernet import Fernet
def load_key():
    file = open(r'C:\Users\yusuf\Desktop\Job Hunt\DataScience Journey\Python Projects\Password_Manager\key.key','rb')
    key = file.read()
    file.close()
    return key 


master_pwd = input("Enter your master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

def write_key():
    key = Fernet.generate_key()
    with open(r'C:\Users\yusuf\Desktop\Job Hunt\DataScience Journey\Python Projects\Password_Manager\key.key','wb') as key_file:
        key_file.write(key)

def view():
    with open(r'C:\Users\yusuf\Desktop\Job Hunt\DataScience Journey\Python Projects\Password_Manager\passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            username,password = data.split("|")
            print("Account:", username, "| Password:", fer.decrypt(password.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open(r'C:\Users\yusuf\Desktop\Job Hunt\DataScience Journey\Python Projects\Password_Manager\passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True: 
    mode = input("Would you like to add a new password or view existing ones? (add/view), Press 'q' to quit: ").lower()
    if mode =='q':
        break
    elif mode =='view':
        view()
    elif mode == 'add':
        add()

    else:
        print("Invalid mode.")
        continue    