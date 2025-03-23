import requests

def check_minecraft_name(username):
    url = f"https://api.mojang.com/users/profiles/minecraft/{username}"
    response = requests.get(url)
    if response.status_code==200:
        print(f"The username '{username}' is taken.")
    elif response.status_code==204:
        print(f"The username '{username}' is available! Grab it!")
    else:
        print("Error checking username. Please try again.")
username = input("Enter a Minecraft username to check: ")
check_minecraft_name(username)
