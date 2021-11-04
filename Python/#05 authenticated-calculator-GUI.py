import PySimpleGUI as sg

username = ''
password = ''

# PROGRESS BAR

def progress_bar(): # Making a progress bar for visual appeasing
    sg.theme('LightBlue2')
    layout = [  [sg.Text('Creating your account..')],
                [sg.ProgressBar(1000, orientation='h', size=(20,20), key='progbar')],
                [sg.Cancel()]]

    window = sg.Window('Working..', layout)
    for i in range(1000):
        event, values = window.read(timeout=1)
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        window['progbar'].update_bar(i + 1)
    window.close()

def create_account(): # Creating an account to be stored with data
    global username, password
    sg.theme('LightBlue2')
    layout = [[sg.Text("Sign Up", size=(15,1), font=40, justification='c')],
                [sg.Text("E-Mail", size=(15,1), font=16), sg.InputText(key='-email-', font=16)],
                [sg.Text("Re-enter E-mail", size=(15, 1), font=16), sg.InputText(key='-remail-', font=16)],
                [sg.Text("Create Username", size=(15, 1), font=16), sg.InputText(key='-user-', font=16)],
                [sg.Text("Create Password", size=(15, 1), font=16), sg.InputText(key='-password-', font=16, password_char='*')],
                [sg.Button("Submit"), sg.Button("Cancel"), sg.Button("Log-in")]]
    window = sg.Window("Sign Up", layout)
    while True:
        event, values = window.read()
        if event == 'Cancel' or event == sg.WIN_CLOSED:
            break
        elif event == 'Log-in':
            login()
        else:
            if event == "Submit":
                password = values['-password-']
                username = values['-user-']
                if values['-email-'] != values['-remail-']:
                    sg.popup_error("The E-mail is not the same \nPlease check your E-mail again", font=16)
                    continue
                elif values['-email-'] == values['-remail-']:
                    progress_bar()
                    break
    window.close()

def login(): # Making a log-in page 
    global username,password
    sg.theme("LightBlue2")
    layout = [  [sg.Text("Log In", size=(15,1), font=40)],
                [sg.Text("Username", size=(15,1), font=16), sg.InputText(key='-usrnm-', font=16)],
                [sg.Text("Password", size=(15,1), font=16), sg.InputText(key='-pwd-', password_char='*', font=16)],
                [sg.Button('OK'), sg.Button('CANCEL'), sg.Button('Sign Up')]]

    window = sg.Window("Log In", layout)

    while True:
        event,values = window.read()
        if event == "Cancel" or event == sg.WIN_CLOSED:
            break
        elif event == "Sign Up":
            create_account()
        else:
            if event == "OK":
                if values['-usrnm-'] == username and values['-pwd-'] == password:
                    sg.popup("Welcome! %s" %(username,))
                    break
                elif values['-usrnm-'] != username or values['-pwd-'] != password:
                    sg.popup("Invalid Login. Try again.")
    window.close()
    
create_account()
login()
