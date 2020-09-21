class Object:
    def __init__(self):
        return

    def get_name(self):
        return "name"

    def get_describe(self):
        return "describe"

class SecretBagGoblet(Object):
    def __init__(self):
        self.name = "Secret Bag of Goblet"
        self.description = "Trade it and you may pick up an object from the pile. May not be traded with another secret bag. The bag truns into a [GOBLET] as soon as all objects have been picked."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class SecretBagKey(Object):
    def __init__(self):
        self.name = "Secret Bag of Key"
        self.description = "Trade it and you may pick up an object from the pile. May not be traded with another secret bag. The bag truns into a [KEY] as soon as all objects have been picked."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


# ---------- Goblet ----------

class Goblet_1(Object):
    def __init__(self):
        self.name = "Goblet"
        self.description = "The brotherhood may problaim the victory if they own at least 3 goblets."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Goblet_2(Object):
    def __init__(self):
        self.name = "Goblet"
        self.description = "The brotherhood may problaim the victory if they own at least 3 goblets."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Goblet_3(Object):
    def __init__(self):
        self.name = "Goblet"
        self.description = "The brotherhood may problaim the victory if they own at least 3 goblets."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

# ---------- End of Goblet ----------

# ---------- Key ----------

class Key_1(Object):
    def __init__(self):
        self.name = "Key"
        self.description = "The Order may proclaim the victory if they own at least 3 keys."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Key_2(Object):
    def __init__(self):
        self.name = "Key"
        self.description = "The Order may proclaim the victory if they own at least 3 keys."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Key_3(Object):
    def __init__(self):
        self.name = "Key"
        self.description = "The Order may proclaim the victory if they own at least 3 keys."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

# ---------- End of Key ----------

class Brokenmirror(Object):
    def __init__(self):
        self.name = "Broken Mirror"
        self.description = "This card must be accepted in a trade. The object that you receive in exchange does not come into effect."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Tome(Object):
    def __init__(self):
        self.name = "Tome"
        self.description = "Trade it and you may exchange the profession with your trading passenger. Professions that are face-up are turned face-down again."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Monocle(Object):
    def __init__(self):
        self.name = "Monocle"
        self.description = "Trade it and you may take a look at your trading passenger's association."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Sixtant(Object):
    def __init__(self):
        self.name = "Sixtant"
        self.description = "Trade it and you may assign a direction. All passengers must pass on an object of their own choice to their nerghbor in the given direction."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Poisonring(Object):
    def __init__(self):
        self.name = "Poison Ring"
        self.description = "You will win in a stand-off dual if you are either the attacker or the defender."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Whip(Object):
    def __init__(self):
        self.name = "Whip"
        self.description = "If you are supporting a defender during a dual, he may add 1 to his result."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Gloves(Object):
    def __init__(self):
        self.name = "Gloves"
        self.description = "You may add 1 to your result if you are the defender. This does NOT count when you are supporting another passenger."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Armorcoat(Object):
    def __init__(self):
        self.name = "The coat of armor of the loge"
        self.description = "You may proclaim your solo victory if you own this object with three gobles/keys. (e.g. 2 goblets and 1 key)"
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Coat(Object):
    def __init__(self):
        self.name = "Coat"
        self.description = "Trade it and you may pick a new profession from those left over and put face-down in front of yourself. Put your old profession down to the profession pile. i.e. You can NOT use your old profession."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Dagger(Object):
    def __init__(self):
        self.name = "Dagger"
        self.description = "You may add 1 to your result if you are the attacker in a dual. This does NOT count when you are supporting another passenger."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Privilege(Object):
    def __init__(self):
        self.name = "Privilege"
        self.description = "Trade it and you may take a look at all of your trading passenger's objects."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Castingknives(Object):
    def __init__(self):
        self.name = "Casting Knives"
        self.description = "If you are supporting and attacker in a dual, he may add 1 to his result."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Blackpearl(Object):
    def __init__(self):
        self.name = "Black Pearl"
        self.description = "Must be accepted if offered during a trade. Whoever owns it can not proclaim the victory of his association."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description