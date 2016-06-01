import pymongo
import re
import pickle

def check(a):
    added = []
    deleted = []
    if 'files' in a:
        for i in a['files']:
            if re.match('.*\.java', i['filename']):
                if 'patch' in i:
                    for j in i['patch'].split('\n'):
                        if (j[0] == '-'):
                            deleted.append(j[1:])
                        if (j[0] == '+'):
                            added.append(j[1:])
    return (added, deleted)


client = pymongo.MongoClient()
db = client['msr14']
collection = db['commits']
ans = 0
counter = 0
coll = collection.find()
res = []
for i in coll:
    (added, deleted) = check(i)
    if added != [] or deleted != []:
        commit = i['commit']['message']
        res.append((commit, added, deleted))
    counter += 1
    if counter % 10000 == 0:
        print (str(counter) + '/' + str(coll.count()))
pickle.dump(res, open('./resources/data/data.txt', 'ab'))