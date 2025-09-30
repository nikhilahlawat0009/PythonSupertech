# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description: Dictionary

import pprint
movies ={'kymran': ['indiana jones', 'bridget jones', 'mamma mia'],
         'charles': ['puss in boots', 'the last wish', 'django unchained'],
         'diren': ['top gum', 'wolf of the wallstreet', 'rio']
}

# grow on dict

movies['nikhil'] = ['3 idiots', 'sikander', 'rang se basanti' ]
movies['grace'] = ['fast and the furious', 'tarzan']

# shrink a dict

movies.pop('charles') # remove keyvalue
movies.popitem() # remove last one inserted

print(movies)


print(f"Nikhil's fav movies: {movies['nikhil']}")

pprint.pprint(movies)

films = movies.copy()

pprint.pprint(films)
