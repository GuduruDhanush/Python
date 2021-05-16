from IPython.display import clear_output
from art import logo

print(logo)


def find_highest_bidder(bidding_dict):
    highest_bid = 0
    winner = ''

    for name in bids:
        if bids[name] > highest_bid:
            highest_bid = bids[name]
            winner = name

    print(f'the winner is {winner} with ${highest_bid}')


should_continue = False

bids = {}

while not should_continue:

    name = input('what is your name? : ')
    bid = int(input('Enter your bid amount? : $ '))

    bids[name] = bid

    is_compleated = input('is there anyoneelse? Enter yes or no? : ')

    if is_compleated == 'no':
        find_highest_bidder(bids)
        should_continue = True

    elif is_compleated == 'yes':
        should_continue = False
        clear_output()
