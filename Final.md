Creating A OOP Bar:
Run Main: python bar.py
Run Test: python test_bar.py

The Idea:
I wanted to create a virtual bar that can keep track of:
    1) what alcohol you have
    2) what garnishes you have
    3) what toppers you have
I also wanted to know what the recipes for mixed drinks so I can make them.
This can eventually become a full fleged app with filters and a search but i wanted 
to start with just the mixed drinks and supplys in the bar. I was looking at using 
multiple inheritance for approaching the assignment. I also needed the mixed drinks 
to be able to hold predefined objects inside of the mixed drinks object. The reason 
for this is that you might want to use diferent types of alcohol for the same mixed 
drink. I also tryed basic encapsilation where only nessessary things can be accesed. 
I also tried basic abstraction where theres limited on the client(main) side of 
things and more can be done behind th sceens. 

## The BreakDown ##

-obj-  Alcohol
    I wanted to have the first object be a bottle of alcohol.
    I wanted to know what  type of alcohol and the proof.
    you can put in the brand or just what type of alcohol it 
    contains as the name of the object.
    I can also thought to add more descriptors if needed but deemed unnessisary for 
    the scope of the assignment.
**Example:** 
    : nameofalc = alcohol(type, proof)
    : GreyGoose = alcohol("Vodka", 45)

-obj- Garneshes
    I wanted to have garneshes of X type and tell me how many needed
    Its very basic for a object but all good mixed drinks tipicly 3 things
**Example:** 
    : nameofgarn = Garnish(type, ammount)
    : Lime = Garnish("Fruit", 1)

-obj- Topper
    I wanted the topper to hold again another string type that can tell us what kind 
    of topper is needed when creating the drinks. This can also be used in a filter 
    to see what  kind of (sodas, juices, etc.) you have to put into a mixed drink.
    we can also see if it is alcoholic or not. Just incase you want a vodka vodka
**Example:** 
    : nameoftop = Topper(type, containsAlcohol)
    : OrangeJucie = Topper("juice", False)

-obj- MixedDrink
    This was the biggest and most important Object in my bar program. It is what 
    will be taking in the objects of everything. and you can also specify how many 
    ounces are needed, and a price if it is for a actual bar.
    It can also allow for a description on what steps  are needed or if anything fancy like a specific glass or shaken and strained.
**Example:** 
    : MixedDrink = MixedDrinks("Name",alcohol,alcOZ,Garnigh,Topper,TopperOZ,Price)