def getEventsOrder(team1, team2, events1, events2):

    parsed1 = parse(team1, events1)
    parsed2 = parse(team2, events2)
    sorted_parsed = sorted(parsed1 + parsed2)
    return [event for time, card, event in sorted_parsed]


def sort_by_event_card(card):
    """return numbers to sort events by GYRS."""
    if card == 'G':
        return 0
    if card == 'Y':
        return 1
    if card == 'R':
        return 2
    if card == 'S':
        return 3


def parse(team, events):
    # events = ['player-name time event', player-name time event second-player', ...]
    # first split each event in events into arrays of [1st player, time, event, 2nd player]
        # second players are optional
        # additional time will be denoted by a +additional-time
        # if time does not have "+" in it then means no additional time
        # additional time occurs before the events of the next half, so 45+2 is before 46

    # parsed to be list of 'team-name player-name time event second-player'
    parsed = []
    for e in events:
        split = e.split()
        # figure out time and sort by time
        # builtin function .isnumeric() --> checks if string is numerical chars
        # if no extra time (no + in string) then .isnumeric == True
        time = None
        card = None
        if split[1].isnumeric(): # if 1st player has only one name
            time = int(split[1])
            card = sort_by_event_card(split[2])
        elif split[2].isnumeric(): # if 1st player has two names
            time = int(split[2])
            card = sort_by_event_card(split[3])
        elif not split[1].isnumeric():
            time = int(''.join(split[1].split('+')))
            card = sort_by_event_card(split[2])
        elif not split[2].isnumeric():
            time = int(''.join(split[2].split('+')))
            card = sort_by_event_card(split[3])

        # to sort the times, format the times to be triple digits (45+2 --> 452, 46 --> 460)
        # last digit will represent the additional time, and first two digits will be for sorting
        # if no additinal time --> then currently is two digits, so make into 3 digits
        if time // 100 == 0:
            time += 10

        parsed.append((time, card, team + ' ' + e))
    return parsed


if __name__ == '__main__':
    
    team1 = 'EDC'
    events1 = ['FirstName LastName 43 Y', 'Name1 12 G']
    team2 = 'CDE'
    events2 = ['AAA1 46 G', 'Name3 45+1 S SubName']
    print(getEventsOrder(team1, team2, events1, events2)) # 'EDC Name1 12 G', 'EDC Firstname Lastname 43 Y', 'CDE Name3 45+1 S SubName', 'CDE Name4 46 G']

    team3 = 'ABC'
    events3 = ['Hello 35+3 S Goodbye', 'AAA 35 G', 'ABA 35 G']
    team4 = 'DEF'
    events4 = ['Hello 35 Y', 'AAA 35 R', 'Goodbye 35+3 S Hello']
    print(getEventsOrder(team3, team4, events3, events4)) # ['ABC AAA 35 G', 'ABC ABA 35 G', 'DEF Hello 35 Y', 'DEF AAA 35 R', 'ABC Hello 35+3 S Goodbye', 'DEF Goodbye 35+3 S Hello']


