Javascript Heiarchy and Mixin
=============================

To Run: 
    - **the modal version:** node mixin.js
    - **the real world version:** node people.js

Heiarchy tldr:
--------------
    -   Objects Should Be grouped into a relationship like Parent, child.
    -   When in a relationship, it should be grouped where parent objects pass thir methods and properties to the child objects.
            - this process is called ----  Inheritance ----
                --- Following the Inheritance Modal ---
                                think Vehicle: 
                                    bus, plane, car
                                    All require engines
                                    all requre a stearing wheel
                                    all have a length, capacity and color

                                    but car is small
                                    plans can fly and use jet fuel
                                    and busses have a high capasity 
                                Or mammals: 
                                    All have fur
                                    all have 4 limbs

                                    but a deer has antlers
                                    humans walk on legs and have thumbs
                                    and cows go moo
            Hierarchy: 
                [OBJ](Parent)
                  | 
        ___________________
        |        |        |      
      [obj]    [obj]    [obj] (Children)



