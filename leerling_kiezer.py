# kies een random leerling uit een SOMtoday klassenexport
import pandas as pd
import random

FILENAME = 'export-60697.csv'
def lees_namen_uit_csv(filename):
    """ Lees de leerlingnamen via Pandas dataframe
    return lijst van namen
    """

    df = pd.read_csv(filename, header = 0, delimiter=';')

    return list(df['Naam'])

def trek_naam(lijst):
    """ kies een random naam uit een een lijst """
    return lijst[random.randint(0,len(lijst)-1)]


if  __name__ == '__main__':

    if 'namen' not in globals():
        print "Laad namen uit: ", FILENAME
        global namen
        namen = lees_namen_uit_csv(FILENAME)
    else:
        print "Namen reeds geladen..."

    print trek_naam(namen)
