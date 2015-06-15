## Names

This is a simple little Markov-chain based name generator suitable for tabletop RPGs or procedural-content computer games.

Place your name source lists in the `namedata/` folder. You can generate names based on each source list independently, for different cultural flavors. You can request a sequence of names from a sequence of source lists. Several source lists are provided.  

### Command Line Options

~~~
usage: names.py [-h] 
                [--count COUNT] 
                [--sequence] 
                [--star] 
                [--min MIN]
                [--max MAX]

optional arguments:
  -h, --help     show this help message and exit
  --count COUNT  number of names to generate
  --sequence     use name sets in order instead of randomly 
  --star         generate a star name in a fictional constellation
  --min MIN      minimum name length
  --max MAX      maximum name length
~~~

### Examples

#### Use as a standalone tool                                             

Get a name for a quasi-English woman.

~~~
: python names.py --sequence engf engsur
Gayne Fielly
~~~

The input files are UTF-8, so let's have a name for a pseudo-Norse god.

~~~
: python names.py norsem
Hriðr
~~~
 
Or a French woman with a Japanese father whose mother read too many fantasy novels.

~~~
: python names.py --sequence frenchf arthurianf japansur
Sylvaine Isonina Miyami
~~~
 
The `--sequence` options selects one from each of the name lists chosen; without it, the tool picks one name list at random to use from the lists you select.

~~~
: python names.py arthurianm arthurianf normanm normanf normansur saxonm saxonf
Goldry
~~~

Generate a bunch of names using all the name source lists as one big list.

~~~
: python names.py --count 10 all
Yudeli
Hardal
Clearia
Arrid
Lafi
Heskina
Oddrik
Astonna
Gavittia
Korg
~~~   
   
It also does pseudo-Bayer star names based on made-up constellations:

~~~
: python names.py --star
Beta Ambertus
~~~
     
#### Use as a module
Import the module and load the name data files. This can take a few seconds.

~~~
: python
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import names
~~~

You can do name sequences here too:

~~~
>>> print names.gen_names( ['engf','engsur'] )
Lina Fitter
~~~

~~~
>>> print names.gen_names( ['norsem'] )
Þorn
~~~  

~~~
>>> print names.gen_names( ['frenchf','arthurianf','japansur'] )
Jestée Lyona Harasahiro                                                             
~~~

The 'all' name set works here too.

~~~
>>> print names.gen_name( 'all' )
Lùshi 
>>> print names.gen_name( 'all' )
Ingarriphan
~~~

And stars.

~~~
>>> print names.gen_star_name()
Beta Agapidus
~~~

You can explicitly control the minimum and maximum name length yielded:

~~~
>>> print names.gen_name( 'engsur', 40, 120 )
Wienstowersonettermannetenthsteraffieder
~~~

...though at present the algorithm isn't guaranteed to terminate with all combinations of length limits and source lists, so use this option with caution. 


### Name Sets 

I've assembled a few name lists from various cultures, collected from various sources, some contemporary and some historical. Many of the names on these lists are probably ridiculous. Many cultures have had names "injected" into them from other cultures over the years, so the lists aren't very "pure". Feel free to alter them as you see fit.   

The format is simple: white space ignored, one name per line, lines beginning with `#` are comments.

The more names on the list, the more likely it is to successfully generate a name. 

Lists which include names coming from different languages are more likely to generate unpronounceable names, because it'll be switching orthographic rules in mid-word.  

These are the name data files in the current distribution:

~~~
albanianf        azerbaijanm    engm            incam           norsef
albanianm        azerbaijansur  engsur          japanf          norsem
albaniansur      countries      engtradenames   japanm          oldengsurnames
arabicf          czechf         frenchf         japansur        provinces
arabicm          czechm         frenchm         latinf          saxonf
arthurianf       czechsur       frenchsur       latinm          saxonm
arthurianm       engbynames     gothf           normanf         sumerianf
asteroids        engf           gothm           normanm         sumerianm
azerbaijanf      englocalities  incaf           normansur       swedishm   
~~~  

### Future Work

Verify behavior with right-to-left languages.

Improve name lists.

Guarantee termination of name generation by hook or by crook.
