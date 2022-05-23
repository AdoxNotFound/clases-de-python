favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

new_users = ['adox', 'sarah', 'wachimingo', 'edward']
for new_user in new_users:
    if new_user in favorite_languages.keys():
        print(f"{new_user.title()}, thanks for responding the poll <3")
    else:
        print(f"{new_user.title()} please take the poll >:v")