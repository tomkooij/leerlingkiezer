# kies een random leerling uit een SOMtoday klassenexport
import pandas as pd
import random

# klassen bijbehorende SOMtoday CSV export
csvfiles = { '1b' : 'export-60697.csv', '3e': 'export-60697.csv' }
namen = {}

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

    for klas in csvfiles:
        print "klas %s uit %s " % (klas, csvfiles[klas])
        namen[klas] = lees_namen_uit_csv(csvfiles[klas])

    #print trek_naam(namen)
