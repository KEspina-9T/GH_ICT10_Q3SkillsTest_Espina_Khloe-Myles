# sign up / login in 
from pyscript import display, document # type: ignore (quick fix feature)


def sign_in(e):
    document.getElementById('output').innerHTML='' #ensures the output wont repeat

    Pword = document.getElementById('pword').value
    Uname = document.getElementById('uname').value 

    
    

    if len(Pword) >= 10: 
        if  not Pword.isalpha(): #isalpha() checks if the input is only letters. 
            if Pword.isdigit(): #isdigit() checks if the input in only numbers.
                display(f'Please ensure that your password has letters', target="output")
            else:
                display(f'Your Password is valid!', target="output")
        
        elif Pword.isalpha():
            display(f'Please ensure that your password has numbers', target="output")
    elif not len(Pword) >= 10:
            display(f'Please ensure that your password has 10 CHARACTERS.', target="output")
    if len(Uname) >= 7:#len() checks the length of the input, so if it's less than 10, it will result in an "invalid" unsername
        display(f'Username {Uname} is valid.', target="output")
    else:
        display(f'Please ensure your username has 7 CHARACTERS.', target="output")


    