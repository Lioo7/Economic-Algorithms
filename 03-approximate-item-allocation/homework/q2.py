import csv


def election_threshold_filtering(file_name, flag=True):
    """
    loads the election results from a csv file into a dictionary and returns it
    if the flag is True (flag would be true by defult), then the function will apply the election threshold
    """
    THRESHOLD = 3.25
    file = csv.reader(
        open(file_name, 'r', encoding='utf-8-sig'))
    d_votes = {}
    if flag:  # only parties above or equals the threshold
        for row in file:
            name, seats, portion, votes = row
            if float(portion) * 100 >= THRESHOLD:
                name = name[::-1]
                votes = votes.replace(',', '')
                d_votes[name] = int(votes)
    else:  # all the parties
        for row in file:
            name, seats, portion, votes = row
            name = name[::-1]
            votes = votes.replace(',', '')
            d_votes[name] = int(votes)

    return d_votes


def webster_f(s):
    """"Webster function that gets as input an integer and returns the given number plus one"""
    return s + 1


def webster_method(d_votes):
    """
    gets a dict when the key is party's name and the value is the part's total votes,
    and returns a dict with the number of seats for each party, by using the Webster method
    """
    # initilazes two new dicts with value 0 for all parties
    seats_results = {}
    for name in d_votes:
        seats_results[name] = 0

    free_seats = 120
    i = 0
    # the algorithem stops when all the seats were allocated
    while (free_seats > 0 and i < 2):
        temp_qutient = 0
        # index 0: party's name, index:1 party's seats
        max_qutient = ["null", 0]
        # calculates the qutient for each party, using webster's function
        for name, seats in seats_results.items():
            # print(i, name, seats)
            temp_qutient = d_votes[name] / webster_f(seats)
            # print(int(d_votes[name]), webster_f(seats), temp_qutient)
            # print(int(d_votes[name]), webster_f(seats), temp_qutient)
            if temp_qutient > max_qutient[1]:
                max_qutient[1] = temp_qutient
                max_qutient[0] = name
        # allocates the next seat to the party with the bigest qutient
        seats_results[max_qutient[0]] += 1
        free_seats -= 1

    return seats_results


def main():
    election_results = 'election_results.csv'
    d_votes = election_threshold_filtering(election_results)
    seats_results = webster_method(d_votes)
    print(seats_results)


if "__main__" == main():
    main()
