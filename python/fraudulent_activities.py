def activityNotifications(expenditure, d):
    n = len(expenditure)
    occurences = [0] * 201
    firstDaysAmounts = expenditure[:d]
    notifications = 0

    for amount in firstDaysAmounts:
        occurences[amount] += 1

    for i, amount in enumerate(expenditure[d:]):
        limit = getLimit(occurences, d)

        if limit <= amount:
            notifications += 1

        occurences[amount] += 1
        occurences[expenditure[i]] -= 1

    return notifications


def getLimit(occurences, d):
    m1 = (d // 2)
    m2 = (d // 2) + 1

    median1 = 0
    median2 = 0
    position = 0

    for number, occurence in enumerate(occurences):
        position += occurence

        if not median1 and position >= m1:
            median1 = number

        if position >= m2:
            median2 = number
            break

    return median2 * 2 if d % 2 == 1 else (median1 + median2)

def printOccurrences(occurences):
    for number, occurence in enumerate(occurences):
        if occurence >= 1:
            print(f"{number}: {occurence}")

if __name__ == '__main__':
    expenditure = [10, 20, 30, 40, 50]
    d = 3
    print(f"expenditure = {expenditure}, d = {d}")
    print(f"notifications = {activityNotifications(expenditure, d)}")

    print("----------------------")

    expenditure = [2, 3, 4, 2, 3, 6, 8, 4, 5]
    d = 5
    print(f"expenditure = {expenditure}, d = {d}")
    print(f"notifications = {activityNotifications(expenditure, d)}")
