favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " +
      favorite_languages['sarah'].title() +
      ".")

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

print()
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages:
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() +
              ", I see your favorite language is " + 
              favorite_languages[name].title() + "!")
        
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# To get a sorted list of the keys
for name in sorted(favorite_languages):
    print(f"{name.title()}, thank you for taking the poll.")

# Looping through the values in the dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

print()
# Put them in a set to remove duplicates
print("Here they are again without duplicates:")
for language in set(favorite_languages.values()):
    print(language.title())


favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}
for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())