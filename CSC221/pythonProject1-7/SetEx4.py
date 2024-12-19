my_favorites = {'ant', 'bison', 'cow'}
noas_favorites = {input()}
inas_favorites = {input()}
sues_favorites = {input()}

''' Your code goes here '''
likeable_animals = my_favorites.union( noas_favorites, inas_favorites, sues_favorites)
print(f'My favorite animals: {sorted(my_favorites)}')
print(f"Noa's favorite animals: {sorted(noas_favorites)}")
print(f"Ina's favorite animals: {sorted(inas_favorites)}")
print(f"Sue's favorite animals: {sorted(sues_favorites)}")
print(f'Likeable animals: {sorted(likeable_animals)}')