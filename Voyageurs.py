class Voyageurs:
    """Classe creant les voyageurs allant prendre le train"""

    def __init__(self, numero, place=0):
        """constructeur ,par default il n'as pas de billet lors de la creation"""
        self.place = place
        self.numero = numero
        

    def __repr__(self):
        """affiche nos voyageurs dans la console"""
        return "voyageur{}".format(self.numero)
    
