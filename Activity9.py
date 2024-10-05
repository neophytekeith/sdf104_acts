class Bacterium:
    #class attribute
    is_unicellular =  True
                              #parameters
    def __init__(self, name, classification, shape, habitat, gram_stain, x, y, life_counter):   #initializer
        #instance attributes
        self.name = name
        self.classification = classification
        self.shape = shape
        self.habitat = habitat
        self.gram_stain = gram_stain
        self.x = x
        self.y = y
        self.life_counter = life_counter

                    #instances
bacteriumOne = Bacterium("E. coli", "bacillus", "rod-shaped", "intestines", "gram-negative", 10, 20, 100)
bacteriumTwo = Bacterium("S. aureus", "cocci", "spherical", "skin", "gram-positive", 50, 75, 80)
bacteriumThree = Bacterium("B. anthracis", "bacillus", "rod-shaped", "soil", "gram-positive", 15, 30, 120)

print(bacteriumOne.name, bacteriumOne.classification, bacteriumOne.shape, bacteriumOne.habitat, bacteriumOne.gram_stain, bacteriumOne.x, bacteriumOne.y, bacteriumOne.life_counter)
print(bacteriumTwo.name, bacteriumTwo.classification, bacteriumTwo.shape, bacteriumTwo.habitat, bacteriumTwo.gram_stain, bacteriumTwo.x, bacteriumTwo.y, bacteriumTwo.life_counter)
print(bacteriumThree.name, bacteriumThree.classification, bacteriumThree.shape, bacteriumThree.habitat, bacteriumThree.gram_stain, bacteriumThree.x, bacteriumThree.y, bacteriumThree.life_counter)
