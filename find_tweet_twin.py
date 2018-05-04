import pprint

f = open("results200-1.txt", "r")

users = {}

lines = f.readline()
for l in lines:
    ans = l.split("|")
    user_name = ans[0]
    hashtag = ans[1]
    perc = ans[4]

    if user_name in users:
        users[user_name].append((float(perc), hashtag))
    else:
        users[user_name] = [(float(perc), hashtag)]
f.close()

f = open("hashtagUsers.txt", "r")

hashtagUsers = {}
prev = None
for l in lines:
    ans = l.split("|")
    hashtag = ans[0]
    user_name = ans[1]
    perc = ans[2]

    if hashtag in hashtagUsers:
        hashtagUsers[hashtag].append((float(perc), user_name))
    else:
        hashtagUsers[hashtag] = [(float(perc), user_name)]

    if hashtag != prev:
        hashtagUsers[prev].sort()

    prev = hashtag
    
f.close()

pp = PrettyPrinter(indent=4)
pp.pprint(users)
pp.pprint(hashtagUsers)
