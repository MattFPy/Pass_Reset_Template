from tkinter import *
from tkinter import ttk

# Main callout for the tkinter.
root = Tk()

# Default window settings for the main window, including its title, icon used, and its width x height.
root.title("Passcode templates generator")
# root.iconbitmap('cool_examples\icon_of_neco_ark.ico')
root.geometry("365x140")

# Temporary frame for placing other widgets, useful for removing them entirely from the function below.
widgetsFrame = Frame(root, width=365, height=140)
widgetsFrame.place(x=10, y=30)


"""Where all the widgets get deleted, has to be called each time in passOptionsSelected(event)."""
def deleteWidgets(event):
    for widgets in widgetsFrame.winfo_children():
        widgetsFrame.destroy()


"""Widget for the contact info"""
def contactInfo(event):

    root.geometry("365x140")

    widgetsFrame = Frame(root, width=365, height=140)
    widgetsFrame.place(x=10, y=30)

    infoTextBox = Text(widgetsFrame, height=3, width=40)
    infoTextBox.place(x=10, y=30)
    infoString = "Contact:\nEmail - mattsartsandfarts@gmail.com\nGithub - https://github.com/MattFPy"
    infoTextBox.insert('1.0', infoString)

"""
   Widgets for Domain AD Password Reset copy-paste.
   The format for all of them goes like this:
   
   0. Define the function first (What???? No way),
   1. Define the size of the main window, and its frame where all of the widgets 
      are placed,
   2. Define the display and modify textbox function using the widgets below,
   3. Define the widges seperately, with Label, Options list, empty string, 
      the input StringVar, and finally the OptionBox, while calling out the
      PrintOut function. There can be multiple of those, depending on which 
      password reset type is chosen.
   4. Display the textbox with the text too for instant copy-paste needs, in case
      if the default options are fine.
   5. Repeat for the other password reset options.
"""
def ADPassReset(event):

    root.geometry("930x410")

    widgetsFrame = Frame(root, width=950, height=410)
    widgetsFrame.place(x=10, y=30)

    def passOptionPrintOut(*args):
        tempPRTextBox.destroy()
        the3PUIsString = f'Customer\'s identity validated w/ 2 PUI\'s? - {the3PUIsVar.get()}\n'
        loginSuccessString = f'Customer logged in successfully with a new password? - {loginSuccessVar.get()}\n'
        tryPassString = f'Did the customer try use https://password.global.none.com? (If yes, did something go wrong?  If not, why not?):\n{tryPassVar.get()}'
        restOfThePRString = "\nAD Password Reset.\n====================\nPhone:"
        restOfThePRTextBox = Text(widgetsFrame, height=9, width=111)
        restOfThePRTextBox.place(x=10, y=210)
        restOfThePRTextBox.insert('1.0',
                                  the3PUIsString + loginSuccessString + "\n" + tryPassString + "\n" + restOfThePRString)


    # Widgets
    the3PUIsLabel = Label(widgetsFrame, text="Customer's identity validated w/ 2 PUI's?").place(x=10, y=45)
    the3PUIsOptions = ('3PUIs.', '2PUIs.', '1PUIs.', 'None.')
    the3PUIsString = " "
    the3PUIsVar = StringVar()
    the3PUIsDropdown = ttk.OptionMenu(widgetsFrame,
                                      the3PUIsVar,
                                      the3PUIsOptions[0],
                                      *the3PUIsOptions,
                                      command=passOptionPrintOut)
    the3PUIsDropdown.place(x=310, y=45)

    loginSuccessLabel = Label(widgetsFrame, text="Customer logged in successfully with a new password?").place(x=10, y=85)
    loginSuccessOptions = ('Yes!', 'No.')
    loginSuccessString = " "
    loginSuccessVar = StringVar()
    loginSuccessDropdown = ttk.OptionMenu(widgetsFrame,
                                          loginSuccessVar,
                                          loginSuccessOptions[0],
                                          *loginSuccessOptions,
                                          command=passOptionPrintOut)
    loginSuccessDropdown.place(x=310, y=85)

    tryPassLabel = Label(widgetsFrame, text="Did the customer try use https://password.global.none.com? "
                                    "(If yes, did something go wrong?  If not, why not?)").place(x=10, y=120)
    tryPassOptions = [
        "Caller was locked out of their PC.",
        "Caller couldn't access their PC.",
        "Caller didn't knew about the website before."
    ]
    tryPassString = " "
    tryPassVar = StringVar()
    tryPassDropdown = ttk.OptionMenu(widgetsFrame,
                                     tryPassVar,
                                     tryPassOptions[0],
                                     *tryPassOptions,
                                     command=passOptionPrintOut)
    tryPassDropdown.place(x=310, y=150)

    tempPRString = ("Customer's identity validated w/ 2 PUI's? - 3PUIs.\n"
                   "Customer logged in successfully with a new password? - Yes!\n"
                   "\nDid the customer try use https://password.global.none.com? (If yes, did something go wrong?  If not, why not?):\n"
                   "Caller was locked out of their PC.\n"
                   "\nAD Password Reset.\n"
                   "====================\n"
                   "Phone:")
    tempPRTextBox = Text(widgetsFrame, height=9, width=111)
    tempPRTextBox.place(x=10, y=210)
    tempPRTextBox.insert('1.0', tempPRString)


"""Widgets for the bitlocker copy-paste. It's the shortest one too!"""
def Bitlocker(event):

    root.geometry("450x265")

    widgetsFrame = Frame(root, width=450, height=265)
    widgetsFrame.place(x=10, y=30)


    def bitlockerPrintOut(*args):
        tempBitlockTextBox.destroy()
        the3PUIsString = f'Customer\'s identity validated w/ 2 PUI\'s? - {the3PUIsVar.get()}\n'
        bitEncryptionString = f'Drive Encryption resumed? - {bitEncryptionVar.get()}\n'
        restOfThePRString = "\nBitlocker Encryption Code Generation.\n====================\nPhone:"
        restOfThePRTextBox = Text(widgetsFrame, height=6, width=51)
        restOfThePRTextBox.place(x=10, y=115)
        restOfThePRTextBox.insert('1.0', the3PUIsString + bitEncryptionString + restOfThePRString)


    # Widgets
    the3PUIsLabel = Label(widgetsFrame, text="Customer's identity validated w/ 2 PUI's?").place(x=10, y=25)
    the3PUIsOptions = ('3PUIs.', '2PUIs.', '1PUIs.', 'None.')
    the3PUIsString = " "
    the3PUIsVar = StringVar()
    the3PUIsDropdown = ttk.OptionMenu(widgetsFrame,
                                      the3PUIsVar,
                                      the3PUIsOptions[0],
                                      *the3PUIsOptions,
                                      command=bitlockerPrintOut)
    the3PUIsDropdown.place(x=250, y=25)

    bitEncryptionLabel = Label(widgetsFrame, text="Drive Encryption resumed?").place(x=10, y=65)
    bitEncryptionOptions = ('Yes!', 'No.')
    bitEncryptionString = " "
    bitEncryptionVar = StringVar()
    bitEncryptionDropdown = ttk.OptionMenu(widgetsFrame,
                                           bitEncryptionVar,
                                           bitEncryptionOptions[0],
                                           *bitEncryptionOptions,
                                           command=bitlockerPrintOut)
    bitEncryptionDropdown.place(x=250, y=60)

    tempBitlockString = ("Customer's identity validated w/ 2 PUI's? - 3PUIs.\n"
                         "Drive Encryption resumed? - Yes!\n"
                         "\nBitlocker Encryption Code Generation.\n"
                         "====================\n"
                         "Phone:")
    tempBitlockTextBox = Text(widgetsFrame, height=6, width=51)
    tempBitlockTextBox.place(x=10, y=115)
    tempBitlockTextBox.insert('1.0', tempBitlockString)


"""Widgets for the MyID/SmartCard copy-paste."""
def MyIDSlashSmartCard(event):

    root.geometry("485x305")

    widgetsFrame = Frame(root, width=485, height=305)
    widgetsFrame.place(x=10, y=30)


    def MyIDPrintOut(*args):
        tempMyIDTextBox.destroy()
        the3PUIsString = f'Customer\'s identity validated w/ 2 PUI\'s? - {the3PUIsVar.get()}\n'
        cardUnlockString = f'Card unlocked? - {cardUnlockVar.get()}\n'
        succSignString = f'User signed in successfully? - {succSignVar.get()}\n'
        restOfThePRString = "\nMyID/SmartCard Unlock.\n====================\nPhone:"
        restOfThePRTextBox = Text(widgetsFrame, height=7, width=55)
        restOfThePRTextBox.place(x=10, y=135)
        restOfThePRTextBox.insert('1.0', the3PUIsString + cardUnlockString + succSignString + restOfThePRString)


    # Widgets
    the3PUIsLabel = Label(widgetsFrame, text="Customer's identity validated w/ 2 PUI's?").place(x=10, y=25)
    the3PUIsOptions = ('3PUIs.', '2PUIs.', '1PUIs.', 'None.')
    the3PUIsString = " "
    the3PUIsVar = StringVar()
    the3PUIsDropdown = ttk.OptionMenu(widgetsFrame,
                                      the3PUIsVar,
                                      the3PUIsOptions[0],
                                      *the3PUIsOptions,
                                      command=MyIDPrintOut)
    the3PUIsDropdown.place(x=270, y=20)

    cardUnlockLabel = Label(widgetsFrame, text="Card unlocked?").place(x=10, y=65)
    cardUnlockOptions = ('Yes!', 'No.')
    cardUnlockString = " "
    cardUnlockVar = StringVar()
    cardUnlockDropdown = ttk.OptionMenu(widgetsFrame,
                                        cardUnlockVar,
                                        cardUnlockOptions[0],
                                        *cardUnlockOptions,
                                        command=MyIDPrintOut)
    cardUnlockDropdown.place(x=270, y=60)

    succSignLabel = Label(widgetsFrame, text="User signed in successfully?").place(x=10, y=105)
    succSignOptions = ('Yes!', 'No.')
    succSignString = " "
    succSignVar = StringVar()
    succSignDropdown = ttk.OptionMenu(widgetsFrame,
                                      succSignVar,
                                      succSignOptions[0],
                                      *succSignOptions,
                                      command=MyIDPrintOut)
    succSignDropdown.place(x=270, y=100)

    tempMyIDString = ("Customer's identity validated w/ 2 PUI's? - 3PUIs.\n"
                      "Card unlocked? - Yes!\n"
                      "User signed in successfully? - Yes!\n"
                      "\nMyID/SmartCard Unlock.\n"
                      "====================\n"
                      "Phone:")
    tempMyIDTextBox = Text(widgetsFrame, height=7, width=55)
    tempMyIDTextBox.place(x=10, y=135)
    tempMyIDTextBox.insert('1.0', tempMyIDString)


"""Widgets for the SecurID copy-paste. This is the longest one."""
def SecurID(event):

    root.geometry("665x575")

    widgetsFrame = Frame(root, width=665, height=575)
    widgetsFrame.place(x=10, y=30)


    def SecurIDPrintOut(*args):
        tempSecurIDTextBox.destroy()
        the3PUIsString = f'Customer\'s identity validated w/ 2 PUI\'s? - {the3PUIsVar.get()}\n'
        thePINClearString = f'PIN Cleared? - {thePINClearVar.get()}\n'
        tokenEnableString = f'Token enabled? - {tokenEnableVar.get()}\n'
        accUnlockString = f'Account unlocked? - {accUnlockVar.get()}\n'
        tenOTPString = f'10 OTP generated? - {tenOTPVar.get()}\n'
        succSignString = f'User signed in successfully? - {succSignVar.get()}\n'
        remainCodesString = f'Remaining codes sent via e-mail\provided verbally? - {remainCodesVar.get()}\n'
        typeOfResetString = f'\n{typeOfResetVar.get()}'
        restOfThePRString = "\n====================\nPhone:"
        restOfThePRTextBox = Text(widgetsFrame, height=11, width=77)
        restOfThePRTextBox.place(x=10, y=335)
        restOfThePRTextBox.insert('1.0',
                                  the3PUIsString +
                                  thePINClearString +
                                  tokenEnableString +
                                  accUnlockString +
                                  tenOTPString +
                                  succSignString +
                                  remainCodesString +
                                  typeOfResetString +
                                  restOfThePRString)


    # Widgets
    the3PUIsLabel = Label(widgetsFrame, text="Customer's identity validated w/ 2 PUI's?").place(x=10, y=25)
    the3PUIsOptions = ('3PUIs.', '2PUIs.', '1PUIs.', 'None.')
    the3PUIsString = " "
    the3PUIsVar = StringVar()
    the3PUIsDropdown = ttk.OptionMenu(widgetsFrame,
                                      the3PUIsVar,
                                      the3PUIsOptions[0],
                                      *the3PUIsOptions,
                                      command=SecurIDPrintOut)
    the3PUIsDropdown.place(x=300, y=25)

    thePINClearLabel = Label(widgetsFrame, text="PIN Cleared?").place(x=10, y=65)
    thePINClearOptions = ('Yes!', 'No.')
    thePINClearString = " "
    thePINClearVar = StringVar()
    thePINClearDropdown = ttk.OptionMenu(widgetsFrame,
                                         thePINClearVar,
                                         thePINClearOptions[1],
                                         *thePINClearOptions,
                                         command=SecurIDPrintOut)
    thePINClearDropdown.place(x=300, y=65)

    tokenEnableLabel = Label(widgetsFrame, text="Token Enabled?").place(x=10, y=105)
    tokenEnableOptions = ('Yes!', 'No.')
    tokenEnableString = " "
    tokenEnableVar = StringVar()
    tokenEnableDropdown = ttk.OptionMenu(widgetsFrame,
                                         tokenEnableVar,
                                         tokenEnableOptions[0],
                                         *tokenEnableOptions,
                                         command=SecurIDPrintOut)
    tokenEnableDropdown.place(x=300, y=105)

    accUnlockLabel = Label(widgetsFrame, text="Account Unlocked?").place(x=10, y=145)
    accUnlockOptions = ('Yes!', 'No.')
    accUnlockString = " "
    accUnlockVar = StringVar()
    accUnlockDropdown = ttk.OptionMenu(widgetsFrame,
                                            accUnlockVar,
                                            accUnlockOptions[0],
                                            *accUnlockOptions,
                                            command=SecurIDPrintOut)
    accUnlockDropdown.place(x=300, y=145)

    tenOTPLabel = Label(widgetsFrame, text="10 OTP generated?").place(x=10, y=185)
    tenOTPOptions = ('Yes!', 'No.')
    tenOTPString = " "
    tenOTPVar = StringVar()
    tenOTPDropdown = ttk.OptionMenu(widgetsFrame,
                                    tenOTPVar,
                                    tenOTPOptions[1],
                                    *tenOTPOptions,
                                    command=SecurIDPrintOut)
    tenOTPDropdown.place(x=300, y=185)

    succSignLabel = Label(widgetsFrame, text="User signed in successfully?").place(x=10, y=225)
    succSignOptions = ('Yes!', 'No.')
    succSignString = " "
    succSignVar = StringVar()
    succSignDropdown = ttk.OptionMenu(widgetsFrame,
                                      succSignVar,
                                      succSignOptions[0],
                                      *succSignOptions,
                                      command=SecurIDPrintOut)
    succSignDropdown.place(x=300, y=225)

    remainCodesLabel = Label(widgetsFrame, text="Remaining codes sent via e-mail\provided verbally?").place(x=10, y=265)
    remainCodesOptions = ('Via e-mail.', 'Via IM', 'Verbally.', 'No codes were generated.')
    remainCodesString = " "
    remainCodesVar = StringVar()
    remainCodesDropdown = ttk.OptionMenu(widgetsFrame,
                                         remainCodesVar,
                                         remainCodesOptions[3],
                                         *remainCodesOptions,
                                         command=SecurIDPrintOut)
    remainCodesDropdown.place(x=300, y=265)

    typeOfResetLabel = Label(widgetsFrame, text="Type of action:").place(x=10, y=305)
    typeOfResetOptions = ('SecurID PIN Reset.', 'SecurID Account Unlock.',  'SecurID One-Time Use Tokencode Creation.')
    typeOfResetString = "SecurID PIN Reset."
    typeOfResetVar = StringVar()
    typeOfResetDropdown = ttk.OptionMenu(widgetsFrame,
                                         typeOfResetVar,
                                         typeOfResetOptions[0],
                                         *typeOfResetOptions,
                                         command=SecurIDPrintOut)
    typeOfResetDropdown.place(x=300, y=305)

    tempSecurIDString = ("Customer's identity validated w/ 2 PUI's? - 3PUIs.\n"
                         "PIN Cleared? - No.\n"
                         "Token enabled? - Yes!\n"
                         "Account unlocked? - Yes!\n"
                         "10 OTP generated? - No.\n"
                         "User signed in successfully? - Yes!\n"
                         "Remaining codes sent via e-mail\provided verbally? - No codes were generated.\n"
                         "\nSecurID PIN Reset.\n"
                         "====================\n"
                         "Phone:")
    tempSecurIDTextBox = Text(widgetsFrame, height=11, width=77)
    tempSecurIDTextBox.place(x=10, y=335)
    tempSecurIDTextBox.insert('1.0', tempSecurIDString)


"""Widgets for the DUO."""
def DUO(event):

    root.geometry("605x405")

    widgetsFrame = Frame(root, width=605, height=405)
    widgetsFrame.place(x=10, y=30)


    def DUOPrintOut(*args):
        tempDUOTextBox.destroy()
        the3PUIsString = f'Customer\'s identity validated w/ 2 PUI\'s? - {the3PUIsVar.get()}\n'
        succSignString = f'User logged in successfully? - {succSignVar.get()}\n'
        duoAuthString = f'Added new Duo Authenticator to Duo? - {duoAuthVar.get()}\n'
        duoRemoveString = f'Removed old authenticator from Duo? - {duoRemoveVar.get()}\n'
        typeOfDUOString = f'\n{typeOfDUOVar.get()}\n'
        restOfThePRString = "====================\nPhone:"
        restOfThePRTextBox = Text(widgetsFrame, height=8, width=70)
        restOfThePRTextBox.place(x=10, y=225)
        restOfThePRTextBox.insert('1.0', the3PUIsString +
                                         succSignString +
                                         duoAuthString +
                                         duoRemoveString +
                                         typeOfDUOString +
                                         restOfThePRString)


    # Widgets
    the3PUIsLabel = Label(widgetsFrame, text="Customer's identity validated w/ 2 PUI's?").place(x=10, y=25)
    the3PUIsOptions = ('3PUIs.', '2PUIs.', '1PUIs.', 'None.')
    the3PUIsString = " "
    the3PUIsVar = StringVar()
    the3PUIsDropdown = ttk.OptionMenu(widgetsFrame,
                                      the3PUIsVar,
                                      the3PUIsOptions[0],
                                      *the3PUIsOptions,
                                      command=DUOPrintOut)
    the3PUIsDropdown.place(x=300, y=25)

    succSignLabel = Label(widgetsFrame, text="User logged in successfully?").place(x=10, y=65)
    succSignOptions = ('Yes!', 'No.')
    succSignString = " "
    succSignVar = StringVar()
    succSignDropdown = ttk.OptionMenu(widgetsFrame,
                                      succSignVar,
                                      succSignOptions[0],
                                      *succSignOptions,
                                      command=DUOPrintOut)
    succSignDropdown.place(x=300, y=65)

    duoAuthLabel = Label(widgetsFrame, text="Added new Duo Authenticator to Duo?").place(x=10, y=105)
    duoAuthOptions = ('Yes!', 'No.')
    duoAuthString = " "
    duoAuthVar = StringVar()
    duoAuthDropdown = ttk.OptionMenu(widgetsFrame,
                                      duoAuthVar,
                                      duoAuthOptions[1],
                                      *duoAuthOptions,
                                      command=DUOPrintOut)
    duoAuthDropdown.place(x=300, y=105)

    duoRemoveLabel = Label(widgetsFrame, text="Removed old authenticator from Duo?").place(x=10, y=145)
    duoRemoveOptions = ('Yes!', 'No.')
    duoRemoveString = " "
    duoRemoveVar = StringVar()
    duoRemoveDropdown = ttk.OptionMenu(widgetsFrame,
                                     duoRemoveVar,
                                     duoRemoveOptions[1],
                                     *duoRemoveOptions,
                                     command=DUOPrintOut)
    duoRemoveDropdown.place(x=300, y=145)

    typeOfDUOLabel = Label(widgetsFrame, text="Type of action:").place(x=10, y=185)
    typeOfDUOOptions = ('DUO Bypass Codes Creation.', 'DUO Unlock.')
    typeOfDUOString = "DUO Bypass Codes Creation."
    typeOfDUOVar = StringVar()
    typeOfDUODropdown = ttk.OptionMenu(widgetsFrame,
                                         typeOfDUOVar,
                                         typeOfDUOOptions[0],
                                         *typeOfDUOOptions,
                                         command=DUOPrintOut)
    typeOfDUODropdown.place(x=300, y=185)

    tempDUOString = ("Customer's identity validated w/ 2 PUI's? - 3PUIs.\n"
                     "User logged in successfully? - Yes!\n"
                     "Added new Duo Authenticator to Duo? - No.\n"
                     "Removed old authenticator from Duo? - No.\n"
                     "\nDUO Bypass Codes Creation.\n"
                     "====================\n"
                     "Phone:")
    tempDUOTextBox = Text(widgetsFrame, height=8, width=70)
    tempDUOTextBox.place(x=10, y=225)
    tempDUOTextBox.insert('1.0', tempDUOString)


"""Widgets for the iOS PIN."""
def iOSPIN(event):

    root.geometry("605x260")

    widgetsFrame = Frame(root, width=605, height=260)
    widgetsFrame.place(x=10, y=30)


    def iOSPINPrintOut(*args):
        tempiOSTextBox.destroy()
        the3PUIsString = f'Customer\'s identity validated w/ 2 PUI\'s? - {the3PUIsVar.get()}\n'
        newPINString = f'User logged in successfully? - {newPINVar.get()}\n'
        restOfThePRString = "\niOS PIN Reset.\n====================\nPhone:"
        restOfThePRTextBox = Text(widgetsFrame, height=6, width=70)
        restOfThePRTextBox.place(x=10, y=105)
        restOfThePRTextBox.insert('1.0', the3PUIsString +
                                         newPINString +
                                         restOfThePRString)


    # Widgets
    the3PUIsLabel = Label(widgetsFrame, text="Customer's identity validated w/ 2 PUI's, if applicable?").place(x=10, y=25)
    the3PUIsOptions = ('3PUIs.', '2PUIs.', '1PUIs.', 'None.')
    the3PUIsString = " "
    the3PUIsVar = StringVar()
    the3PUIsDropdown = ttk.OptionMenu(widgetsFrame,
                                      the3PUIsVar,
                                      the3PUIsOptions[0],
                                      *the3PUIsOptions,
                                      command=iOSPINPrintOut)
    the3PUIsDropdown.place(x=300, y=25)

    newPINLabel = Label(widgetsFrame, text="Customer logged in successfully with new PIN?").place(x=10, y=65)
    newPINOptions = ('Yes!', 'No.')
    newPINString = " "
    newPINVar = StringVar()
    newPINDropdown = ttk.OptionMenu(widgetsFrame,
                                      newPINVar,
                                      newPINOptions[0],
                                      *newPINOptions,
                                      command=iOSPINPrintOut)
    newPINDropdown.place(x=300, y=65)

    tempiOSString = ("Customer's identity validated w/ 2 PUI's? - 3PUIs.\n"
                     "User logged in successfully? - Yes!\n"
                     "\niOS PIN Reset.\n"
                     "====================\n"
                     "Phone:")
    tempiOSTextBox = Text(widgetsFrame, height=6, width=70)
    tempiOSTextBox.place(x=10, y=105)
    tempiOSTextBox.insert('1.0', tempiOSString)


"""Widgets for the SAP P1S"""
def SAPP1S(event):

    root.geometry("605x355")

    widgetsFrame = Frame(root, width=605, height=355)
    widgetsFrame.place(x=10, y=30)


    def SAPP1SPrintOut(*args):
        the3PUIsString = f'Customer\'s identity validated w/ 2 PUI\'s? - {the3PUIsVar.get()}\n'
        SAPPassChangeString = f'Customer was able to change password and login successfully?? - {SAPPassChangeVar.get()}\n'
        noIssuesLeftString = f'Customer had no further issues to be addressed? - {noIssuesLeftVar.get()}\n'
        typeOfSAPString = f'\n{typeOfSAPVar.get()}\n'
        restOfThePRString = "====================\nPhone:"
        restOfThePRTextBox = Text(widgetsFrame, height=7, width=70)
        restOfThePRTextBox.place(x=10, y=185)
        restOfThePRTextBox.insert('1.0', the3PUIsString +
                                         SAPPassChangeString +
                                         noIssuesLeftString +
                                         typeOfSAPString +
                                         restOfThePRString)


    # Widgets
    the3PUIsLabel = Label(widgetsFrame, text="Customer was authenticated with 2 PUI's?").place(x=10, y=25)
    the3PUIsOptions = ('3PUIs.', '2PUIs.', '1PUIs.', 'None.')
    the3PUIsString = " "
    the3PUIsVar = StringVar()
    the3PUIsDropdown = ttk.OptionMenu(widgetsFrame,
                                      the3PUIsVar,
                                      the3PUIsOptions[0],
                                      *the3PUIsOptions,
                                      command=SAPP1SPrintOut)
    the3PUIsDropdown.place(x=365, y=25)

    SAPPassChangeLabel = Label(widgetsFrame, text="Customer was able to change password and login successfully?").place(x=10, y=65)
    SAPPassChangeOptions = ('Yes!', 'No.')
    SAPPassChangeString = " "
    SAPPassChangeVar = StringVar()
    SAPPassChangeDropdown = ttk.OptionMenu(widgetsFrame,
                                           SAPPassChangeVar,
                                           SAPPassChangeOptions[0],
                                           *SAPPassChangeOptions,
                                           command=SAPP1SPrintOut)
    SAPPassChangeDropdown.place(x=365, y=65)

    noIssuesLeftLabel = Label(widgetsFrame, text="Customer had no further issues to be addressed?").place(x=10, y=105)
    noIssuesLeftOptions = ('Yes!', 'No.')
    noIssuesLeftString = " "
    noIssuesLeftVar = StringVar()
    noIssuesLeftDropdown = ttk.OptionMenu(widgetsFrame,
                                           noIssuesLeftVar,
                                           noIssuesLeftOptions[0],
                                           *noIssuesLeftOptions,
                                           command=SAPP1SPrintOut)
    noIssuesLeftDropdown.place(x=365, y=105)

    typeOfSAPLabel = Label(widgetsFrame, text="Type of action:").place(x=10, y=145)
    typeOfSAPOptions = ('SAP P1S Password reset.', 'SAP P1S Account unlock.')
    typeOfSAPString = "SAP P1S Password reset."
    typeOfSAPVar = StringVar()
    typeOfSAPDropdown = ttk.OptionMenu(widgetsFrame,
                                       typeOfSAPVar,
                                       typeOfSAPOptions[0],
                                       *typeOfSAPOptions,
                                       command=SAPP1SPrintOut)
    typeOfSAPDropdown.place(x=365, y=145)

    tempSAPString = ("Customer's identity validated w/ 2 PUI's? - 3PUIs.\n"
                     "Customer was able to change password and login successfully?? - Yes!\n"
                     "Customer had no further issues to be addressed? - Yes!\n"
                     "\nSAP P1S Password reset.\n"
                     "====================\n"
                     "Phone:")
    tempSAPTextBox = Text(widgetsFrame, height=7, width=70)
    tempSAPTextBox.place(x=10, y=185)
    tempSAPTextBox.insert('1.0', tempSAPString)


"""Function for deleting the previous widget set, and displaying a new one."""
def passOptionsSelected(event):

    if passOptionsVar.get() == passOptions[0]:
        deleteWidgets(event)
        contactInfo(event)
    elif passOptionsVar.get() == passOptions[1]:
        deleteWidgets(event)
        ADPassReset(event)
    elif passOptionsVar.get() == passOptions[2]:
        deleteWidgets(event)
        Bitlocker(event)
    elif passOptionsVar.get() == passOptions[3]:
        deleteWidgets(event)
        MyIDSlashSmartCard(event)
    elif passOptionsVar.get() == passOptions[4]:
        deleteWidgets(event)
        SecurID(event)
    elif passOptionsVar.get() == passOptions[5]:
        deleteWidgets(event)
        DUO(event)
    elif passOptionsVar.get() == passOptions[6]:
        deleteWidgets(event)
        iOSPIN(event)
    elif passOptionsVar.get() == passOptions[7]:
        deleteWidgets(event)
        SAPP1S(event)
    else:
        root.destroy()

# Main dropdown options, visible at the start
passOptions = ["Select...",
               "Domeny (ACCT01-05, US, INTL, itp.)",
               "Bitlocker",
               "MyID/SmartCard",
               "SecurID",
               "DUO",
               "iOS PIN",
               "SAP P1S"]

passOptionsVar = StringVar()
passOptionsDropdown = ttk.OptionMenu(root,
                                     passOptionsVar,
                                     passOptions[0],
                                     *passOptions,
                                     command=passOptionsSelected)

passOptionsDropdown.place(x=10, y=10)

# Aaaand the mainloop for tkinter to run at all times.
root.mainloop()

# That is it!
