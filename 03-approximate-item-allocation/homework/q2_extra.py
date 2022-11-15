import csv


def get_dict_voters_with_election_threshold_filtering(file_name, THRESHOLD):
    """
    loads the election results from a csv file into a dictionary and return a dict with the followinf format:
    {party name: party voters}
    """
    file = csv.reader(
        open(file_name, 'r', encoding='utf-8-sig'))
    d_votes = {}
    for row in file:
        name, seats, portion, votes = row
        # only parties above or equals the threshold
        if float(portion) * 100 >= THRESHOLD: 
            name = name[::-1]
            votes = votes.replace(',', '')
            d_votes[name] = int(votes)

    return d_votes


def generic_function(s, y):
    """"the function gets as input an integer s and y such that 0<y<s and returns s+y"""
    return s + y


def calculates_seats(d_votes, func, y):
    """
    gets a dict when the key is party's name and the value is the part's total votes,
    and returns a dict with the number of seats for each party, by using the given method
    """
    # initilazes a new dict with value 0 for all parties
    seats_results = {}
    for name in d_votes:
        seats_results[name] = 0

    free_seats = 120
    # the algorithem stops when all the seats were allocated
    while (free_seats > 0):
        temp_qutient = 0
        # index 0: party's name, index:1 party's seats
        max_qutient = ["null", 0]
        # calculates the qutient for each party, using the given function
        for name, seats in seats_results.items():
            func_result = func(seats, y)
            if func_result == 0:
                func_result = 1
            temp_qutient = d_votes[name] / func_result
            if temp_qutient > max_qutient[1]:
                max_qutient[1] = temp_qutient
                max_qutient[0] = name
        # allocates the next seat to the party with the bigest qutient
        seats_results[max_qutient[0]] += 1
        free_seats -= 1

    return seats_results


def is_equal(dict1, dict2):
    """"the function gets as an input two dicts and returns true if both the dicts are equal"""
    return dict1 == dict2


def get_dict_real_seats_with_election_threshold_filtering(file_name, flag=True):
    """
    loads the election results from a csv file into a dictionary and return a dict with the followinf format:
    {party name: party seats}
    if the flag is True (flag would be true by defult), then the function will apply the election threshold
    """
    THRESHOLD = 3.25
    file = csv.reader(
        open(file_name, 'r', encoding='utf-8-sig'))
    d_seats = {}
    if flag:  # only parties above or equals the threshold
        for row in file:
            name, seats, portion, votes = row
            if float(portion) * 100 >= THRESHOLD:
                name = name[::-1]
                d_seats[name] = int(seats)
    else:  # all the parties
        for row in file:
            name, seats, portion, votes = row
            name = name[::-1]
            d_seats[name] = int(seats)

    return d_seats


def find_max_y(d_votes, real_results):
    """
    the function finds the maximum value of y such that the results will be different from the real results,
    when f(s) = s + y
    """
    EPSILON = 0.000
    y = 1
    # initilazes a new dict with value 0 for all parties
    seats_results = None 
    while (not is_equal(seats_results, real_results)):
        print(y)
        y -= EPSILON
        seats_results = calculates_seats(d_votes, generic_function, y)
    
    return y


def main():
    election_results = 'election_results.csv'
    threshold = 3.25
    d_votes = get_dict_voters_with_election_threshold_filtering(
        election_results, threshold)
    # Adams: f(s) = s (threshold = 3.25%)
    y = 0
    seats_results = calculates_seats(d_votes, generic_function, y)
    print('Adams (threshold = 3.25%):', seats_results)
    # Webster: f(s) = s + 0.5 (threshold = 3.25%)
    y = 0.5
    seats_results = calculates_seats(d_votes, generic_function, y)
    print('Webster (threshold = 3.25%):', seats_results)
    # Jefferson: f(s) = s + 1 (threshold = 3.25%)
    y = 1
    seats_results = calculates_seats(d_votes, generic_function, y)
    print('Jefferson (threshold = 3.25%):', seats_results)

    threshold = 0
    d_votes = get_dict_voters_with_election_threshold_filtering(
        election_results, threshold)
    # Adams: f(s) = s (threshold = 0%)
    y = 0
    seats_results = calculates_seats(d_votes, generic_function, y)
    print('Adams (threshold = 0%):', seats_results)
    # Webster: f(s) = s + 0.5 (threshold = 0%)
    y = 0.5
    seats_results = calculates_seats(d_votes, generic_function, y)
    print('Webster (threshold = 0%):', seats_results)
    # Jefferson: f(s) = s + 1 (threshold = 0%)
    y = 1
    seats_results = calculates_seats(d_votes, generic_function, y)
    print('Jefferson (threshold = 0%):', seats_results)

    # d_seats = get_dict_real_seats_with_election_threshold_filtering(election_results)
    # print(real results:', d_seats)
    # y = find_max_y(d_votes, d_seats)
    # print(y)


if "__main__" == main():
    main()
