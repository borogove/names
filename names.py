#!/usr/bin/ppython
# -*- coding: utf-8 -*-

"""

Copyright (c) 2010-2015 Russell Borogove. All rights reserved. 

"""  

import os
import random
from collections import defaultdict

NAME_DATA_FOLDER = "./namedata"
GREEK_ALPHABET = """Alpha 
Beta 
Gamma  
Delta  
Epsilon
Zeta   
Eta  
Theta  
Iota   
Kappa  
Lambda 
Mu	
Nu	
Xi	
Omicron
Pi
Rho
Sigma
Tau
Upsilon
Phi
Chi
Psi
Omega""".split()  

# == MARKOV CHAIN BASED NAMER =========================================

class MarkovChainNamer( object ):
    def __init__(self):
        self.chains = defaultdict(list)
        self.splat = defaultdict(str)
        # Read all the name data files we have provided.
        self.load_name_data()  

    def next( self, setname, current ):
        if not current:
            return "^"
        k = unicode(current)
        while True:
            if k:
                if (setname,k) in self.chains:
                    return random.choice( self.chains[(setname,k)] )
                k = k[1:]   
            else:
                return random.choice(self.splat[setname])

     

    def load_chains( self, setname, name ):
        if not name:
            return
        name = "^" + name + "|"
        self.splat[setname] = self.splat[setname] + name
        # initials[setname] = initials[setname] + name[0]
        for count in range(2,4):
            for i in range(len(name)):
                seq = name[i:i+count]
                if len(seq) > 1:
                    prefix = seq[:-1]
                    self.chains[(setname,prefix)].append( seq[-1] ) 
 

    def load_one( self, setname, filename ):
        names = [line.strip() for line in open(os.path.join(NAME_DATA_FOLDER,filename),'rt').readlines()]
        for name in names:
            if name.startswith('#'):
                continue                
            # Keep everything as unicode internally
            name = name.decode('utf-8')   
            self.load_chains( setname, name )
            self.load_chains( "all", name )
    

    def load_name_data(self):
        for fn in os.listdir( NAME_DATA_FOLDER ):
            if fn.endswith(".txt"):
                base, ext = os.path.splitext(fn)
                self.load_one( base, fn )

    def gen_name( self, nameset, minlen, maxlen ):
        ok = False
                         
        if nameset not in self.splat:
            raise ValueError("Nameset %s not loaded"%nameset)
            
        while not ok:
            name = "^"
    
            while len(name) < maxlen:
                next = self.next( nameset, name )
                if next != "|":
                    name += next
                else:
                    if len(name) > minlen:
                        ok=True
                    break
    
        return name.replace("^","")


# == SELECTOR =========================================================

markov = MarkovChainNamer()    

# A function to name a star using Bayer-style names in made-up  
# constellations with pseudo-latin names.
def gen_star_name():
    # Generate a pseudo-latin constellation name.
    if random.randrange(2):
        constellation = markov.gen_name( "latinm", 7, 16 )
    else:
        constellation = markov.gen_name( "latinf", 5, 16 )

    # Choose a rank for the star within the constellation; 
    # making the brighter ranks (Alpha, Beta...) more likely 
    # because we're magnitude elitists.
    rank = random.randrange(5)
    while random.randrange(2):
        rank += 1
    # Take that ranked Greek letter; if we rolled an 
    # extraordinarily high rank, just wrap around the list.            
    rankname = GREEK_ALPHABET[ rank % 24 ]
    
    # for example, "Epsilon Athanatille"
    return "%s %s"%(rankname,constellation)    
  

# Generate a "full name" given a sequence 
def gen_names( sourceSequence ):
    generated = []
    for source in sourceSequence:
        generated.append( markov.gen_name( source, 3, 15 ) )
        
    return " ".join(generated)
 
def gen_name( nameset, minlen, maxlen ):
    return markov.gen_name( nameset, minlen, maxlen )          
     
# =====================================================================

if __name__ == "__main__": 
     
    # Generate a star name.
    print gen_star_name()
                          
    # Generate an individual person's full name - in this case, a pseudo-French woman 
    # with a quasi-Japanese father, whose mother read a lot of fantasy novels.
    # example result: Jestée Lyona Harasahiro
    print gen_names( ["frenchf","arthurianf","japansur"] )
    
    # Produce several pages of names for your RPG setting - print 'em out, and 
    # when you introduce an NPC, pick a name off an appropriate list and cross it off.
    groups = [  ("Island Provinces", ["arthurianm", "arthurianf", "normanm", "normanf", "normansur", "saxonm", "saxonf"] ),
                ("Western Lands", ["asteroids", "albanianm", "albanianf" ] ),
                ("Old Lands", ["provinces","engbynames","englocalities","engtradenames"] ),
                ("Desert Nomads", ["arabicm","arabicf"] ),
                ("Other", ["all"] ) ]
     
    for group,nameSets in groups:
        print "%s Names"%group
        for name in range(47):       
            col1 = markov.gen_name( random.choice(nameSets), 3, 13 )   
            col2 = markov.gen_name( random.choice(nameSets), 3, 13 )  
            col3 = markov.gen_name( random.choice(nameSets), 3, 13 )  
            print "  %15s %15s %15s"%(col1,col2,col3)
        print 