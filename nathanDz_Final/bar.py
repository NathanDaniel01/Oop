class Alcohol(object):
    # Class attribute
    containsLiquor = True
    def __init__(self, alcType, proof):
        self.alcType = alcType
        self.proof = proof
    
    # To get alcType
    def getAlcType(self):
        return self.alcType
  
    # To get proof
    def getProof(self):
        return  self.proof

class Garnish(object):
    containsLiquor = False

    def __init__(self, garnType, ammount):
        self.garnType = garnType
        self.ammount = ammount

    # To get garnType
    def getGarnType(self):
        return self.garnType
    # To get ammount
    def getAmmount(self):
        return self.ammount

class Topper(object):
    def __init__(self, topType, containsLiquor):
        self.topType = topType
        self.containsLiquor = containsLiquor
    # To get topType
    def getTopType(self):
        return self.topType
    # To get containsLiquor
    def getContainsLiquor(self):
        return self.containsLiquor

class MixedDrinks(Alcohol,Garnish, Topper):
    def __init__(self, drinkname, alc, afOZ, garn, top, tfOZ,price):
        self._alc = alc
        self._garn = garn
        self._top = top
        self.drinkname = drinkname
        self.afOZ = afOZ
        self.tfOZ = tfOZ
        self.price = price
    def description(self):
        print( "| " , self.drinkname , "   | price: ", "$",self.price, " |")
        print( "| Alcohol: ", self._alc.getAlcType(), "|  Proof: ", self._alc.getProof(), " | Fluid Oz: ", self.afOZ , " |")
        print( "| Garnish:", self._garn.getGarnType(),"| Topper: ", self._top.getTopType(),"| Fluid Oz: ", self.tfOZ , " |")
    def garnishinfo(self):
        print( "| Garnish:", self._garn.getGarnType(),"| Ammount needed: ", self._garn.getAmmount()," |")
    def getDrinkName(self):
        return self.drinkname
    def getAlc(self):
        return self._alc
    def getAfOZ(self):
        return self.afOZ
    def getGarn(self):
        return self._garn
    def getTop(self):
        return self._top
    def getTfOZ(self):
        return self.tfOZ
    def getPrice(self):
        return self.price
  
def main():
    
    vodka = Alcohol("Vodka", 45)
    lime = Garnish("Fruit", 1)
    hangover = Garnish("Hangover",8)
    gingerbeer = Topper("gingerBeer", False)
    redbull = Topper("redbull", False)
    moscowMuel = MixedDrinks("Moscow Muel", vodka, 2,lime, gingerbeer, 4,10.99)
    vodkaRedbull = MixedDrinks("Vodka Redbull", vodka, 2, hangover,redbull, 4, 8.51 )


    moscowMuel.description()
    vodkaRedbull.description()
    vodkaRedbull.garnishinfo()
    print("-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+")
    print("Breakdown of vodka:")
    print("Alcohol: ",vodka.getAlcType())
    print("  Proof: ",vodka.getProof())



if __name__ == "__main__":
    main()