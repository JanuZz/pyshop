import random
from flask import session

# 30 adjectives
adjectives = [
    "autumn", "hidden", "bitter", "misty", "silent",
    "empty", "dry", "dark", "summer", "icy",
    "delicate", "quiet", "white", "cool", "spring",
    "winter", "patient", "twilight", "dawn", "crimson",
    "wispy", "weathered", "blue", "billowing", "broken",
    "cold", "damp", "falling", "frosty", "green",
    "long", "late", "lingering", "bold", "little",
    "morning", "muddy", "old", "red", "rough",
    "still", "small", "sparkling", "throbbing", "shy",
    "wandering", "withered", "wild", "black", "young",
    "holy", "solitary", "fragrant", "aged", "snowy",
    "proud", "floral", "restless", "divine", "polished",
    "ancient", "purple", "lively", "nameless"
]

# 20 nouns
nouns = [
    "waterfall", "river", "breeze", "moon", "rain",
    "wind", "sea", "morning", "snow", "lake",
    "sunset", "pine", "shadow", "leaf", "dawn",
    "glitter", "forest", "hill", "cloud", "meadow",
    "sun", "glade", "bird", "brook", "butterfly",
    "bush", "dew", "dust", "field", "fire",
    "flower", "firefly", "feather", "grass", "haze",
    "mountain", "night", "pond", "darkness", "snowflake",
    "silence", "sound", "sky", "shape", "surf",
    "thunder", "violet", "water", "wildflower", "wave",
    "water", "resonance", "sun", "wood", "dream",
    "cherry", "tree", "fog", "frost", "voice",
    "paper", "frog", "smoke", "star"
]


def getItemId():
    return random.randbytes(4).hex()

def getItemName():
    return f"{random.choice(adjectives)} {random.choice(nouns)}"

### WEB UTILS ###

def getWebHeader(title: str, description: str = ""):
    # Optional username if logged in
    # STORE NAME - PAGE TITLE
    
    out = ''
    
    if(session.get("user")):
        out += f"<h2>Welcome, {session.get('user')}!</h2>"
    
    out += f"<h1>PyMart - {title}</h1>"
    
    return out

def getErrorPage(error: str):
    out = getWebHeader("Error")
    out += f"<h2>Error: {error}</h2>"
    out += "<a href='/'>Return to home</a>"
    return out