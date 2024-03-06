from classes.Item import StoreItem
from classes.Store import Store
from classes.User import StoreUser
from flask import app, request, session, redirect
import settings
import utils
server = app.Flask(__name__)
server.secret_key = settings.SECRET_KEY

store = Store("PyMart")
store.inventory.append(StoreItem(None, 1.99, 10))

@server.route("/")
def home():
    out = utils.getWebHeader("Welcome to PyMart", "The best place to buy stuff")
    
    out += "<h3>Here are some things you can do:</h3>"
    out += "<ul>"
    out += "<li><a href='/createUser'>Create a user</a></li>"
    if("user" in session):
        out += "<li><a href='/logout'>Logout</a></li>"
    else:
        out += "<li><a href='/login'>Login</a></li>"
    out += "<li><a href='/browse'>Browse the store</a></li>"
    out += "</ul>"
    
    return out

### Authentication ###
@server.route("/createUser", methods=["GET", "POST"])
def createUser():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        try:
            user = StoreUser(email, password)   # Create a new user and validate the input
            # Check if a user with the same email already exists
            for u in store.users:
                if u.email == user.email:
                    return utils.getErrorPage("User already exists")
            store.users.append(user)            # Add the user to the store's db of users
            session["user"] = user.email        # Store the user's email in the session, check the browser's cookies to see the session 
            return f"<h1>User created: {user.email}</h1>"
        except ValueError as e:
            return utils.getErrorPage(str(e))
    else:
        return StoreUser.createUserPage()

@server.route("/logout")
def logout():
    session.pop("user", None)   # Remove the user from the session
    return redirect("/")    # Redirect to the home page

@server.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        
        for user in store.users:
            if user.email == email and user.password == password:
                session["user"] = user.email
                return f"<h1>Welcome back, {user.email}</h1>"
        return utils.getErrorPage("Invalid email or password")
    else:
        return StoreUser.loginPage()
    
### Store ###
@server.route("/browse")
def browse():
    out = utils.getWebHeader("Browse")
    out += "<h2>Items for sale:</h2>"
    for item in store.inventory:
        out += f"<p>{item} <a href='{f"/addToCart/{item.id}" if 'user' in session else "/login"}'>{"Add to card" if 'user' in session else "Login to access cart"}</a></p>"
    return out

server.run()