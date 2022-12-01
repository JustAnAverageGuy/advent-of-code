with open("AoC2020_Day16_input.txt", 'r') as file:
    hmm = file.readlines()
    rules = [((int(rule[rule.find(':')+2: rule.find('-')]), int(rule[rule.find('-')+1:rule.find(' or ')])),
              tuple(map(int, rule[rule.find(" or ")+4:].strip().split('-')))) for rule in hmm[:20]]
    nearby = [list(map(int, i.strip().split(','))) for i in hmm[25:]]

ticket_scanning_error_rate = 0


def checkValid(n, rules):
    for i in rules:
        if i[0][0] <= n <= i[0][1] or i[1][0] <= n <= i[1][1]:
            return True
    return False


# part 1
""" 
for ticket in nearby:
    for i in ticket:
        if not checkValid(i, rules):
            ticket_scanning_error_rate += i

print(ticket_scanning_error_rate)
"""
good_nearby = []


def checkGoodTicket(ticket, rules):
    for i in ticket:
        if not checkValid(i, rules):
            return False
    return True


for i in nearby:
    if checkGoodTicket(i, rules):
        good_nearby.append(i)


def checkPossibleDataName(dataname, colmn):
    a, b, c, d = rules[dataname][0][0], rules[dataname][0][1], rules[dataname][1][0], rules[dataname][1][1]
    for i in range(len(good_nearby)):
        if not (a <= good_nearby[i][colmn] <= b or c <= good_nearby[i][colmn] <= d):
            return False
    return True


for j in range(len(rules)):
    for i in range(len(good_nearby[0])):
        if checkPossibleDataName(j, i):
            print((j, i), end=',')

# I am pretty sure this can be coded as well, but eh , manually plotted these points and manually and algorithmitaccly elimnated stuff and found the solution
