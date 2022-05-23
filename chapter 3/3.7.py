names = ["Elvis Presley", "Kurt Cobain", "Madonna"]
print(f"Dear {names[0]}, you're invited to my birthday party.")
print(f"Dear {names[1]}, you're invited to my birthday party.")
print(f"Dear {names[2]}, you're invited to my birthday party.")

print(f"\n{names[0]} apologies for not comming to the party.\n")
names[0] = "Rihanna"
print(f"Dear {names[0]}, you're invited to my birthday party.")
print(f"Dear {names[1]}, you're invited to my birthday party.")
print(f"Dear {names[2]}, you're invited to my birthday party.")

print("\nMore guests are invited to this party, we found a bigger table.\n")

names.insert(0,"Marilyn Monroe")
names.insert(2,"Eminem")
names.append("Jim Morrison")

print(f"Dear {names[0]}, you're invited to my birthday party.")
print(f"Dear {names[1]}, you're invited to my birthday party.")
print(f"Dear {names[2]}, you're invited to my birthday party.")
print(f"Dear {names[3]}, you're invited to my birthday party.")
print(f"Dear {names[4]}, you're invited to my birthday party.")
print(f"Dear {names[5]}, you're invited to my birthday party.")

print("\nOnly 2 persons are allowed in this party.\n")
popped_name = names.pop()
print(f"Dear {popped_name}, you're no longer invited to the party, sorry.")
popped_name = names.pop()
print(f"Dear {popped_name}, you're no longer invited to the party, sorry.")
popped_name = names.pop()
print(f"Dear {popped_name}, you're no longer invited to the party, sorry.")
popped_name = names.pop()
print(f"Dear {popped_name}, you're no longer invited to the party, sorry.\n")

print(f"Dear {names[0]}, you're still invited to my birthday party.")
print(f"Dear {names[1]}, you're still invited to my birthday party.")

del names[0]
del names[0]

print(names)
