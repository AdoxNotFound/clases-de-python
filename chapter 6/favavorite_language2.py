favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

#for name in sorted(favorite_languages.keys()):
#    print(f"{name.title()}, thank you for takinf the poll.")

print("The following languageshave been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())