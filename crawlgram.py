from pygram import PyGram

# Instagram authentication
pygram = PyGram('username', 'password')

# Get username from terminal
print("Enter Username: ", end="")
profile_details = pygram.get_profile(input())

# Print profile details
print("--------------------------")
print("Full Name:       ",profile_details['full_name'])
print("Followers Count: ",profile_details['followers_count'])
print("Following Count: ",profile_details['followed_count'])
print("Website:         ",profile_details['external_url'])
print("Biography:       ",profile_details['biography'])