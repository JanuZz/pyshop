import re
import utils

from classes.Item import StoreItem 

class StoreUser:
    def __init__(self, email : str, password : str):
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            raise ValueError("Invalid email")
        self.email = email
        self.cart : list[StoreItem] = []
        
        if len(password) < 8:
            raise ValueError("Password too short")
        self.password = password
    
    def getForm(redir : str):
        out = f"<form action='{redir}' method='post'>"
        out += "<label for='email'>Email:</label>"
        out += "<input type='text' id='email' name='email'><br>"
        out += "<label for='password'>Password:</label>"
        out += "<input type='password' id='password' name='password'><br>"
        out += "<input type='submit' value='Submit'>"
        out += "</form>"
        
        return out
    
    def loginPage():
        out = utils.getWebHeader("Login", "Please enter your email and password")
        out += StoreUser.getForm("/login")
        return out
    
    def createUserPage():
        out = utils.getWebHeader("Create User", "Please enter your email and password")
        out += StoreUser.getForm("/createUser")
        return out