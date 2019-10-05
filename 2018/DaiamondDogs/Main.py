diamonds_prices = []


def pricer(n):
    return 2**n

def claim_amount(start, end):
    total = 0
    for x in diamonds_prices[start-1,end]:
        total += x
    return total

def main():
    diamonds_size = int(input())

    diamonds = [int(x) for x in input().split()]
    diamonds_prices = [pricer(x) for x in diamonds]

    dogs_size = int(input())

    claims = []
    for _ in range(dogs_size):
        claims.append((int(x) for x in input().split()))


    dogs_money = []
    for x in claims:
        dogs_money.append(claim_amount(x[0],x[1])) 


    print(dogs_money)


if __name__ == '__main__':
    main()
