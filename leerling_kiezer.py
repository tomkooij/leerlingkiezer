# kies een random leerling uit een SOMtoday klassenexport
# Somtoday gebruik CSV met ; als scheidingsteken en UTF-8 unicode
import pandas as pd
import random

# klassen bijbehorende SOMtoday CSV export
csvfiles = { '1b' : '1b.csv', '3e': '3e.csv', '5na1': '5na1.csv' }
namen = {}

def lees_namen_uit_csv(filename):
    """ Lees de leerlingnamen via Pandas dataframe
    return lijst van namen
    """

    df = pd.read_csv(filename, header = 0, delimiter=';') # ,encoding='utf-8'

    return list(df['Naam'])

def trek_naam(lijst):
    """ kies een random naam uit een een lijst """
    return lijst[random.randint(0,len(lijst)-1)]

def maak_groepjes(lijst, n):
    """ maak RANDOM groepjes van n leerlingen
    return list of lists """

    random.shuffle(lijst)

    return [lijst[x:x+n] for x in range(0,len(lijst),n)]



if  __name__ == '__main__':

    for klas in csvfiles:
        print "klas %s uit %s " % (klas, csvfiles[klas])
        namen[klas] = lees_namen_uit_csv(csvfiles[klas])

    klas1b = namen['1b']
    klas3e = namen['3e']
    klas5na1 = namen['5na1']
    """
    print "DEMO: willekeurige leerling uit 1b:", trek_naam(klas1b)

    groepjes1b = maak_groepjes(klas1b,3)

    for groep in groepjes1b:
        print "DEMO: groepje: ", groep
    """
