## Names

This is a simple little Markov-chain based name generator suitable for tabletop RPGs or procedural-content computer games.

Place your name source lists in the `namedata/` folder. You can generate names based on each source list independently, for different cultural flavors. You can request a sequence of names from a sequence of source lists. Several source lists are provided.

### Examples

Import the module and load the name data files. This can take a few seconds.

~~~
: python
Python 2.7.5 (default, Mar  9 2014, 22:15:05) 
[GCC 4.2.1 Compatible Apple LLVM 5.0 (clang-500.0.68)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import names
~~~

Get a name for a quasi-English woman.

~~~
>>> print names.gen_names( ['engf','engsur'] )
Lina Fitter
~~~

The input files are UTF-8, so let's have a name for a pseudo-Norse god.

~~~
>>> print names.gen_names( ['norsem'] )
Þorn
~~~

My character concept is... a pseudo-French woman with a quasi-Japanese father, whose mother read a lot of fantasy novels!

~~~
>>> print names.gen_names( ['frenchf','arthurianf','japansur'] )
Jestée Lyona Harasahiro                                                             
~~~

The module also does pseudo-Bayer star names based on made-up constellations:

~~~
>>> print names.gen_star_name()
Beta Agapidus
~~~

With a single name set, you can explicitly control the minimum and maximum name length yielded:

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

### Future Work

Verify behavior with right-to-left languages.

Improve name lists.

Guarantee termination of name generation by hook or by crook.
