## Code Challenge: Game Events
Two teams are playing football(soccer) match and the recod of events for each team is available. There are 4 possible events, Goal(G), Yellow Card(Y), Red Card(R), and Substitutions (S). G,Y,R are represented as `player-name time event-name` and S is represented as `player-name time event-name second-player-name`. Time represented in minutes from start of game. Extra time may be given at end of second half which is represented as `time+extra-time`. Extra time always considered to have occurred before events of the next half so `45+2` happened earlier than `46`. 

Merge the events for each team into single game event with teams name in front and sorted by time and event in order of GYRS. In the case of the same event happening at the same time, output should be sorted lexicographically based on teams name and players name.

Return an array of strings.

#### Example:
```
Input:
    team1 = 'EDC' events1 = ['Name1 12 G', 'Firstname Lastname 43 Y']
    team2 = 'CDE' events2 = ['Name3 45+1 S SubName', 'Name4 46 G']
Output: ['EDC Name1 12 G', 'EDC Firstname Lastname 43 Y', 'CDE Name3 45+1 S SubName', 'CDE Name4 46 G']
```

Source: Leetcode discussion