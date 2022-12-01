import re

with open(r"AoC2020_Day4_input.txt", 'r') as file:
    data = [[{k.split(':')[0]:k.split(':')[1]} for k in list(i.split())]
            for i in file.read().split('\n\n')]

Data = []
for i in data:
    p = dict()
    for k in i:
        p.update(k)
    Data.append(p)

""" 
with open(r"input.txt", 'r') as file:
    smalldata = [[{k.split(':')[0]:k.split(':')[1]} for k in list(i.split())]
                 for i in file.read().split('\n\n')]

SmallData = []
for i in smalldata:
    p = dict()
    for k in i:
        p.update(k)
    SmallData.append(p) """


def checkValidOld(passport):
    if (len(passport) < 7) or ((len(passport) == 7) and ("cid" in passport)):
        return False
    return True


def checkValidNew(passport):
    if (len(passport) < 7) or ((len(passport) == 7) and ("cid" in passport)):
        return False
    try:
        if (1920 <= int(passport["byr"]) <= 2002) and (2010 <= int(passport["iyr"]) <= 2020) and (2020 <= int(passport["eyr"]) <= 2030) and ((150 <= int(passport['hgt'][:-2]) <= 193) if (passport["hgt"][-2:] == "cm") else (59 <= int(passport['hgt'][:-2]) <= 76)) and ((len(passport['hcl']) == 7) and bool(re.match(r'#[0-9a-f]{6}', passport['hcl']))) and (passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']) and ((len(passport['pid']) == 9) and bool(re.match(r'[0-9]{9}', passport['pid']))):
            return True
    except:
        print(passport)
        return 0
    return False


# A fuckin patchwork , should revisit this , one of the Passport has a fckin empty 'ecl' value hence was giving error for a long time , but anyways <(＿　＿)>
cnt = 0
for i in Data:
    if checkValidNew(i):
        cnt += 1
print(cnt)
# ANSWER = 156
