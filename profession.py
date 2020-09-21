class Profession: 
    def __init__(self):
        return

    def get_name(self):
        return "name"

    def get_description(self):
        return "descript"


class Bodyguard(Profession):
    def __init__(self):
        self.name = "Body Guard"
        self.description = "When you support someone in a dual, he may add 1 to his result."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Doctor(Profession):
    def __init__(self):
        self.name = "Doctor"
        self.description = "[ONLY ONCE IN THE GAME] You may prevent the offedcts immediately after dual."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Hypnotist(Profession):
    def __init__(self):
        self.name = "Hypnotist"
        self.description = "If you are the attacker, you may appoint someone to abstain from supporting someone else eise even after he has already announced his support."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Duelist(Profession):
    def __init__(self):
        self.name = "Duelist"
        self.description = "[ONLY ONCE IN THE GAME] You as the attacker or defender may designate that nobody may support this duel. During this dual you may add 1 to your result."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
        

class Diplomat(Profession):
    def __init__(self):
        self.name = "Diplomat"
        self.description = "[ONLY ONCE IN THE GAME] You may demand that another palyer trade a certain object of your choice. You may only do so on your turn. Your turn ends if the player does not have the object."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Grandmaster(Profession):
    def __init__(self):
        self.name = "Grand Master"
        self.description = "You may add 1 to your result if you are the defender in a dual."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Poisonmaster(Profession):
    def __init__(self):
        self.name = "Poison Master"
        self.description = "[ONLY ONCE IN THE GAME] You may appoint the winner of a dual. But not if you are the attacker or the defender."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Thug(Profession):
    def __init__(self):
        self.name = "Thug"
        self.description = "You may add 1 to your result if you are the attacker in a dual."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description


class Clairvoyant(Profession):
    def __init__(self):
        self.name = "Clairvoyant"
        self.description = "[ONLY ONCE IN THE GAME] You may look at the pile of objects and pick out two of them during your turn. Afterward shuffle the pile and put down the chosen objects in any order face down on top of the pile."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description

class Pirest(Profession):
    def __init__(self):
        self.name = "Pirest"
        self.description = "[ONLY ONCE IN THE GAME] You may prevent a struggle before the other players announce their support. If the attacker owns at least two objects, he must give one ohbject of his own choice to you, the attacker's turn end."
    
    def get_name(self):
        return self.name
    
    def get_description(self):
        return self.description
