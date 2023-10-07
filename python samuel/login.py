def register(reg_name, reg_password, reg):
    if reg_name == 'SAMi-SIKi' or st_name or st_name1:
        print('Username already registered!')
    else:
        print('Successfully registered!')
        user_name, user_password = reg_name, reg_password
        login(reg_name, reg_password, user_name, user_password)
        reg = True
        reg = False


def login(user_name, user_password, reg_name, reg_password):
    if user_name == 'SAMi-SIKi' and user_password == '123':
        print('Login successful!')
        admin()
        y = input('Do you want to logout?(y/n): ')
        logout(y)
    elif user_name == reg_name and user_password == reg_password and reg_name != '':
        print('Login successful!')
        y = input('Do you want to logout?(y/n): ')
        logout(y)
    elif (user_name == st_name or user_name == st_name1) and (user_password == st_password or user_password == st_password1):
        print('Login successful!')
        y = input('Do you want to logout?(y/n): ')
        logout(y)
    else:
        print('Login failed!')
        y = input('Do you want to try again?(y/n): ')
        logout(y)


def storage_manager(reg_name, reg_password, st_name, st_password, st_name1, st_password1):
    if reg_name != '' and st_name == '':
        st_name = reg_name, st_password = reg_password
    elif st_name != '' and reg_name != st_name:
        st_name1 = reg_name, st_password1 = reg_name


def admin():
    print('Welcome boss!')
    # planiram dodati još neke stvari


def init(l_or_r):
    global reg_name
    global reg_password
    l_or_r = input('Register[r]/Login[l]: ')
    if l_or_r == 'r':
        reg_name = input('Username: ')
        reg_password = input('Password: ')
        register(reg_name, reg_password, reg)
    if l_or_r == 'l':
        user_name = input('Username: ')
        user_password = input('Password: ')
        login(user_name, user_password, reg_name, reg_password)


def logout(y):
    if y == 'y':
        init(l_or_r)


reg = False
l_or_r, reg_name, reg_password, st_name, st_password, st_name1, st_password1, y = '', '', '', '', '', '', '', ''

print('Welcome, do you want to be registered or login?')
init(l_or_r)

if reg == True:
    storage_manager(reg_name, reg_password, st_name,
                    st_password, st_name1, st_password1)

#!!!moraš poraviti storage manager!!!
