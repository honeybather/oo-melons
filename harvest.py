############
# Part 1   #
############


class MelonType:
    """A species of melon at a melon farm."""



    def __init__(
        self, name, code, first_harvest, color, is_seedless, is_bestseller
    ):
        """Initialize a melon."""

        self.pairings = []
        self.name = name
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller



    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code



def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    musk = MelonType('Muskmelon','musk', 1998, 'green', True, True)
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('Casba','cas', 2003, 'orange', False, False)
    cas.add_pairing('mint', 'strawberries')
    all_melon_types.append(cas)

    cren = MelonType('Crenshaw','cren', 1996, 'green', False, False)
    cren.add_pairing('prosciutto')
    all_melon_types.append(cren)

    yw = MelonType('Yellow Watermelon','yw', 2013, 'yellow', False, True)
    yw.add_pairing('ice cream')
    all_melon_types.append(yw)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon in melon_types:
        print(f"{melon.name} pairs with {melon.pairings}")


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""
    melon_type_code = {} # created a dictionary
    for melon in melon_types: # loop through each melon type in the list
        melon_type_code[melon.code] = melon # connect melon's code to the actual melon
    return melon_type_code

############
#  Part 2  #
############


class Melon:
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, harvested_from_field, harvested_by):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.harvested_from_field = harvested_from_field
        self.harvested_by = harvested_by

    def is_sellable(self):

       return (self.shape_rating > 5) and (self.color_rating > 5) and (self.harvested_from_field != 3)

def make_melons(melon_types):
        """Returns a list of Melon objects."""
        melons = []

        melon_1 =  Melon(melon_types['yw'], 8, 7, 2, 'sheila')
        melons.append(melon_1)
        melon_2 =  Melon(melon_types['yw'], 3, 4, 2, 'sheila')
        melons.append(melon_2)
        melon_3 =  Melon(melon_types['yw'], 9, 8, 3, 'sheila')
        melons.append(melon_3)
        melon_4 =  Melon(melon_types['cas'], 10, 6, 35, 'sheila')
        melons.append(melon_4)
        melon_5 =  Melon(melon_types['cren'], 8, 9, 35, 'michael')
        melons.append(melon_5)
        melon_6 =  Melon(melon_types['cren'], 8, 2, 35, 'michael')
        melons.append(melon_6)
        melon_7 =  Melon(melon_types['cren'], 2, 3, 4, 'michael')
        melons.append(melon_7)
        melon_8 =  Melon(melon_types['musk'], 6, 7, 4, 'michael')
        melons.append(melon_8)
        melon_9 =  Melon(melon_types['yw'], 7, 10, 3, 'sheila')
        melons.append(melon_9)

        return melons

def get_sellability_report(melons):
        """Given a list of melon object, prints whether each one is sellable."""

        for melon in melons:
            sellable = melon.is_sellable()

            if sellable:
                print(f'Harvseted by {melon.harvested_by} from Field {melon.harvested_from_field} (CAN BE SOLD)')
            else:
                print(f'Harvseted by {melon.harvested_by} from Field {melon.harvested_from_field} (NOT SELLABLE)')


if __name__ == "__main__":
    # Part 1: Create melon types
    melon_types = make_melon_types()

    # Part 2: Create melons based on melon types
    melons = make_melons(make_melon_type_lookup(melon_types))

    # Part 3: Print sellability report for each melon
    print("Sellability Report:")
    get_sellability_report(melons)

