from audioop import reverse


places = ["Dubai", "Korea", "USA", "Germany", "Thailand"]
print(places)
#print(sorted(places))

#print(sorted(places, reverse=True))

#places.reverse()
places.sort()

print(places)

places.sort(reverse=True)
#places.reverse()
print(places)