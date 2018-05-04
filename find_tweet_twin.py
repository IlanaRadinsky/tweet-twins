import pprint

f = open("usersToHashtags.txt", "r")

users = {}

lines = f.readlines()
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

f = open("hashtagsToUsers.txt", "r")

hashtagUsers = {}
prev = None

lines = f.readlines()
for l in lines:
    ans = l.split("|")
    hashtag = ans[0]
    user_name = ans[1]
    perc = ans[2]

    try:
        if hashtag in hashtagUsers:
            hashtagUsers[hashtag].append((float(perc), user_name))
        else:
            hashtagUsers[hashtag] = [(float(perc), user_name)]

        if prev and hashtag != prev:
            hashtagUsers[prev].sort()
       
        prev = hashtag
    
    except:
        continue
f.close()

#pp = pprint.PrettyPrinter(indent=4)
#print("*************USERS******************")
#pp.pprint(users)
#print("************HASHTAGS****************")
#pp.pprint(hashtagUsers)

searchUser = input("Input a user to find his/her friends!")
#searchUser = "floridarussian"
twinTweeters = {}

for hashtag in users[searchUser]:
    usage = hashtag[0]
    for targetUser in hashtagUsers[hashtag[1]]:
        targetUsage = targetUser[0]
        diff = abs(usage-targetUsage)
        if targetUser[1] != hashtag[1] and diff < 0.05:
            if targetUser[1] in twinTweeters:
                twinTweeters[targetUser[1]] += usage/(1+diff) # the larger the difference between the perc
                                                          # vals, the smaller your rank will be. the
                                                          # larger the usage percentage, the more your
                                                          # rank will be weighted.
            else:
                twinTweeters[targetUser[1]] = usage/(1+diff)

twinTweetersList = [(v,k) for k, v in twinTweeters.items()]
twinTweetersList.sort(reverse=True)
print(twinTweetersList)            
