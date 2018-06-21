# write to a file
with open("signups.txt", 'w') as f:
    f.write('this is my first file')


# read a file
with open("signups.txt", 'r') as f:
    users = f.readlines()


print(users)