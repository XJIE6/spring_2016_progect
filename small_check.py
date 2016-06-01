import random

counter1 = 0
counter2 = 0
counter3 = 0

arr1 = random.sample(arr, 100)
arr2 = random.sample(arr, 100)

progress = 1

for (c1, a1, b1) in arr1 :
    for (c2, a2, b2) in arr2:
        c1_vec = vectorizer1.transform([c1])[0]
        c2_vec = vectorizer1.transform([c2])[0]
        a1_full = [a for a in a1]
        if len(a1_full) == 0 :
            a1_full = [' ']

        a2_full = [a for a in a2]
        if len(a2_full) == 0 :
            a2_full = [' ']

        b1_full = [b for b in b1]
        if len(b1_full) == 0 :
            b1_full = [' ']

        b2_full = [b for b in b2]
        if len(b2_full) == 0 :
            b2_full = [' ']

        a1_vec = vectorizer2.transform(a1_full)[0]
        a2_vec = vectorizer2.transform(a2_full)[0]

        b1_vec = vectorizer3.transform(b1_full)[0]
        b2_vec = vectorizer3.transform(b2_full)[0]

        c1_label = km1.predict(c1_vec)[0]
        c2_label = km1.predict(c2_vec)[0]

        a1_label = km2.predict(a1_vec)[0]
        a2_label = km2.predict(a2_vec)[0]

        b1_label = km3.predict(b1_vec)[0]
        b2_label = km3.predict(b2_vec)[0]

        counter1 += 3
        if (c1_label == c2_label) == (a1_label == a2_label) :
            counter2 += 1

        if (c1_label == c2_label) == (b1_label == b2_label) :
            counter2 += 1

        if (b1_label == b2_label) == (a1_label == a2_label) :
            counter2 += 1

        if ((c1_label == c2_label) == (a1_label == a2_label)) == ((b1_label == b2_label) == (c1_label == c2_label)) : #fail
            counter3 += 3

        if counter1 > progress:
            print(counter1)
            progress *= 2

print(counter1)
print(counter2)
print(counter3)