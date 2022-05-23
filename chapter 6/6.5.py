rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'mississipi': 'eeuu',
    'yenisei': 'russia',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")
print("\n")
for river in rivers.keys():
    print(river.title())
print("\n")
for country in rivers.values():
    print(country.title())