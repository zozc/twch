# Tested on 12-03-2020 1:42PM
# Contact: facebook.com/cse.tufayel
# Changes on twitter website will break down code and developer takes no responsibilities hereby
# Runs in 3 modes.
# 1. Direct code edit mode
# 2. Console mode (python lookup.py -u username)
# 3. Mass check mode (python lookup.py -l list.txt)
import requests
import json
import sys
import sys, os, time
#username = "226m" # change username here or run as python lookup.py -u username
#username = "bdd4"
def look(username):
    #print("You are looking for '" + username + "'")
    url = "https://api.twitter.com/graphql/P8ph10GzBbdMqWZxulqCfA/UserByScreenName?variables=%7B%22screen_name%22%3A%22" + username + "%22%2C%22withHighlightedLabel%22%3Atrue%7D"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br",
        "accept-language": "en-US,en;q=0.9,bn;q=0.8",
        'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
        "content-type": "application/json",
        "dnt": "1",
        'origin': 'https://twitter.com',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Mobile Safari/537.36',
        'x-twitter-active-user': 'yes',
        'x-twitter-client-language': 'en'
        }
    resp  = json.loads(requests.get(url, headers=headers).text)
    # you can play around with resp variable output and get other profile info
    # such as follower, bio, display name, account creation time etc.
    try:

        namex = resp["data"]["user"]["legacy"]["name"]
        namexx=namex.replace(" ", "")
        return namexx

        #print("Username unavailable since " + resp["data"]["user"]["legacy"]["created_at"])
    except:
        #eoe="404"

        return
'''if len(sys.argv) > 2:
    if sys.argv[1] == "-l":
        try:
            user_list = open(sys.argv[2], "r").read().split("\n")
            for username in user_list:
                look(username)
        except:
            print("Recheck input file name again")
    else:
        look(sys.argv[2])
else:
    look(username)'''
list_usernames = open("TW3L.txt", "r").read().splitlines()
for username in list_usernames :
    x=look(username)
    s = str(x)
    ss= len(s)
    if ss >= 6:#BEFORE 5
        pos1 = s + "@hotmail.com"
        pos2 = s + "@yahoo.com"
        #pos3 = s + "@outlook.com"
        #pos4 = s + "@outlook.com"
        poss = [pos1, pos2]
        for email in poss:
            if "None" in email:
                print("EROR")
            else:
                Turl = "https://api.twitter.com/i/users/email_available.json?email=" + email
                tres = requests.get(Turl)
                found = tres.text
                untaken = '"taken":false'
                taken = '"taken":true'
                if untaken in found:

                    print("Email is not Vaild")
                    print(email)
                    print('=================================')

                elif taken in found:
                    print("Email is Vaild")
                    print(email)
                    with open('$TW3LFUCK.txt', 'a',encoding="utf-8") as file:
                        file.write("\n" + "[" + username + "]" + email)
                    print('=================================')

                else:
                    print("Someting Wrong")
                #time.sleep(2)
                time.sleep(1)
    else:
        pass


