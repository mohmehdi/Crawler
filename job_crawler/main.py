import json
import os

f = open('out.json', )
data = json.load(f)

select = -1

while select != 0:

    select = int(input("""
    0 close app
    1 view titles
    2 view locations
    3 view days left
    4 view by skills
    5 view by budget
    6 select
    """))
    if select != 6:
         os.system("cls")


    if select == 0:
        break
    elif select == 1:
        [print(f"{d['id']}- {d['job title']} ") for d in data]
    elif select == 2:
        [print(f"{d['id']}- {d['location']} ") for d in data]
    elif select == 3:
        [print(f"{d['id']}- {d['time expire']} ") for d in data]
    elif select == 4:
        [print(f"{d['id']}- {d['skills']} ") for d in data]
    elif select == 5:
        [print(f"{d['id']}- {d['budget']} ") for d in data]
    elif select == 6:
        job_id = int(input("Select :"))
        if  job_id < len(data):
            for item in data[job_id]:
                print(f"{item} ::  {data[job_id][item]}")
    else:
        continue
    input("continue?")

# Closing file
f.close()

"""
0 close app
1 view titles
2 view locations
3 view days left
4 view by skills
4 view by budget
5 select
"""
