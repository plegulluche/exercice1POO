class Train:
    """classe creant notre train, celui ci doit contenir par default 150 voyageurs"""
    import string
    PLACES_MAX = 150

    letters = [letter for letter in string.ascii_uppercase]
    numbers = ["1","2","3","4","5","6","7","8","9","10"]

    def listAZ(letters, numbers):
        """fonction creant une liste de A1 a A10 , B1 a B10 jusqua Z10 ordonnée"""
        list10 = []
        for letter in letters:
            for num in numbers:
                if int(num) < 11:
                    a = letter + num
                    list10.append(a)
        return list10

    listAZ(letters, numbers)
    PLACES = dict ( (key , 0) for key in listAZ(letters, numbers))

    def __init__(self):
        """ constructeur de la classe"""
   
    def __repr__(self):
        """affichage du train dans la console"""
        return "Un train de {} places".format(self.PLACES_MAX)