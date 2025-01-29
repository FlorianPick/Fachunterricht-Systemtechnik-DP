""" Beschreibung des Moduls. """
def bike_labeler(Bikename,**bike_options):
    """ Dies ist ein Docstring. Er beginnt mit drei Anführungszeichen 
    und endet mit weiteren drei Anführungszeichen. Der Text dazwischen 
    kann mehrere Zeilen lang sein. 
    Der Docstring enthält eine Beschreibung der Funktion und wird z.B. 
    vom help()- System angezeigt. 
    """
    BikeLabel={}                                  # Kommentar fuer 
    BikeLabel["Name"] = Bikename                  # internen Gebrauch
    for key,value in bike_options.items():
        BikeLabel[key] = value
    return BikeLabel

#######################
### Funktion Tester ###
#######################
def Tester():
    pass

### Neue Funktion ###
def working_message(probname, progname="Geheim"):
    '''Gebe eine Nachricht aus '''
    return("Program " + progname +" working on " + probname)