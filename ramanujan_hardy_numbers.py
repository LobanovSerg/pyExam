# five numbers Ramanujan-Hardy
for i in range(1700, 40_000):
    counter = 0
    for j in range(1,33):
        for k in range(j,33):
            if j ** 3 + k ** 3 == i:
                counter +=1
                if counter == 2:
                    print(i)
