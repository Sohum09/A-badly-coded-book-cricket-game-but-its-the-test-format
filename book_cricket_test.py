import random

'''
Dot balls... 80% chance of 0 or the rest of the function executing.

Plan for conditions:
Include a ball tracker
Pitches = NORMAL, GREEN, DRY, FLAT
No changes if normal
Green: For upto 40-50 (yet to finalize) balls bowled, Aggression = 1 for Innings 1, 2 and 0 thereafter; 0 for Innings 3 and 4
Dry: For innings 1, 2, random change between Aggression = 0 and Aggression = -1, random chance between 0 and 1 for innings 3 and 4
Flat: For innings 1, 2, random change between Aggression = 0 and Aggression = -1, random chance between -1 and 0 for innings 3 and 4

Outfield: Slow, Normal, Fast
If slow: val = 10 will fetch 2 instead of 4 and vals 7-9 will fetch a random number between 0-1
If normal: no changes.
If fast: vals 7-9 will fetch a random between 1-2 and 10 will be 4.

'''

def map_prob_to_score(runs, wickets, aggression, outfield, pitch, innings, ball_count):
    if pitch != 'NORMAL':
        dot_ball = random.randint(1, 10)
        if innings < 3 and ball_count < random.randint(180, 300):
            if dot_ball > 2:
                return runs, wickets
        else:
            if dot_ball > 4:
                return runs, wickets
    val = random.randint(0, 10)
    if val == 0:
        if aggression == -1:
            x = random.randint(0, 1)
            if x:
                wickets += 1
                return runs, wickets
            else:
                return runs, wickets
        wickets += 1
        return runs, wickets
    elif 1 <= val <= 4:
        runs += val
    elif val == 5:
        runs += 4
    elif val == 6:
        runs += 6
    elif 7 <= val <= 9:
        if outfield == -1: #Slow
            runs += random.randint(0, 1)
            return runs, wickets
        elif outfield == 1: #Fast
            runs += random.randint(1, 2)
            return runs, wickets
        runs += 1
        return runs, wickets
    elif val == 10:
        if wickets >= 8 or aggression == 1:
            wickets += 1
            return runs, wickets
        else:
            if outfield == -1: #Slow
                runs += random.randint(2, 3)
                return runs, wickets
            runs += 4
            return runs, wickets
    return runs, wickets

def drawn_match(innings1, innings1_runs, innings1_wickets,  innings2, innings2_runs, innings2_wickets, innings3 = '', innings3_runs=0, innings3_wickets=0, innings4 = '', innings4_runs=0, innings4_wickets=0, target=0):
    print("\nExhausted alloted global ball quota!")
    if innings1_wickets == 10:
        print(f"Innings 1: {innings1} - {innings1_runs} all out")
    else:
        print(f"Innings 1: {innings1} - {innings1_runs}/{innings1_wickets} time-out/declared")
    if innings2_wickets == 10:
        print(f"Innings 2: {innings2} - {innings2_runs} all out")
    else:
        print(f"Innings 2: {innings2} - {innings2_runs}/{innings2_wickets} time-out/declared")
    if innings3_runs > 0:
        if innings3_wickets == 10:
            print(f"Innings 3: {innings3} - {innings3_runs} all out")
        else:
            print(f"Innings 3: {innings3} - {innings3_runs}/{innings3_wickets} time-out/declared")
    if innings4_runs > 0:
        if innings4_wickets == 10:
            print(f"Innings 4: {innings4} - {innings4_runs} all out")
        else:
            print(f"Innings 4: {innings4} - {innings4_runs}/{innings4_wickets} time-out (Target = {target})")
    print("Result: Match drawn.")

def match():
    print("Welcome to Sohum's terrible book cricket game knockoff on Test Cricket powered by badly written code!")
    print("What? It's a text based game, deal with it.")
    team1 = input("Enter Team 1: ")
    team2 = input("Enter Team 2: ")
    pitch = input("Select Pitch [NORMAL, GREEN, DRY, FLAT]: ").upper()
    outfield = random.choice([-1, 0, 1]) #Slow, Normal, Fast
    print("Outfield selected = ", outfield)
    innings1, innings2 = '', ''

    toss = random.randint(0, 1) #0 = Team 1, 1 = Team 2
    if toss: #Team 1 wins
        print(f"{team1} wins the toss!")
        choice = input("Bat/Bowl? ").upper()
        if choice == 'BAT':
            innings1, innings2 = team1, team2
        else:
            innings1, innings2 = team2, team1
    else: #Team 2 wins
        print(f"{team2} wins the toss!")
        choice = input("Bat/Bowl? ").upper()
        if choice == 'BAT':
            innings1, innings2 = team2, team1
        else:
            innings1, innings2 = team1, team2

    global_balls = 0
    global_ball_limit = 1500
    rain_affect = random.randint(1, 10)
    if team1.upper() in ['ENGLAND', 'SRI LANKA', 'NEW ZEALAND']:
        if rain_affect < 6:
            print("Rain will affect the match!")
            global_ball_limit = random.randint(700, 1400)
            print(f"New ball count = {global_ball_limit}")
    else:
        if rain_affect < 3:
            print("Rain will affect the match!")
            global_ball_limit = random.randint(700, 1400
                                               )
            print(f"New ball count = {global_ball_limit}")

    #----------Innings 1-------------
    print("------------------------------------Innings 1----------------------------------")
    print("Press any key to declare. Otherwise, just hit enter to continue.")
    if pitch == 'GREEN':
        aggression = 1
    if pitch == 'DRY':
        aggression = random.randint(-1, 0)
    if pitch == 'FLAT':
        aggression = -1
    if pitch == 'NORMAL':
        aggression = 0
    print(f"Aggression = {aggression}")
    declareFlag = False
    runs, wickets = 0, 0
    balls = 0
    while(True):
        declare = input().upper()
        if len(declare) > 0:
            declareFlag = True
            break
        if wickets >= 10:
            break
        runs, wickets = map_prob_to_score(runs, wickets, aggression, outfield, pitch, 1, balls)
        balls += 1
        global_balls += 1
        if balls == 40 and pitch == 'GREEN':
            aggression = 0
            print("aggression changed to 0")
        if balls == 60 and pitch == 'GREEN':
            aggression = -1
            print("aggression changed to -1")
        print(f"{innings1}: {runs}/{wickets}, Overs {balls//6}.{balls%6}", end='\r')

    innings1_res = f'{innings1} - {runs} all out' if declareFlag == False else f'{innings1} - {runs}/{wickets} declared'
    if declareFlag == False:
        print(f"End of Innings 1: {innings1} - {runs} all out")
    else:
        print(f"End of Innings 1: {innings1} - {runs}/{wickets} declared")
    print(f"Global ball count = {global_balls}/{global_ball_limit}")
    innings1_runs = runs #Setup for innings 2
    innings1_wickets = wickets

    #----------Innings 2-------------
    print("------------------------------------Innings 2----------------------------------")
    print("Press any key to declare. Otherwise, just hit enter to continue.")
    if pitch == 'GREEN':
        aggression = 1
    if pitch == 'DRY':
        aggression = random.randint(-1, 0)
    if pitch == 'FLAT':
        aggression = -1
    if pitch == 'NORMAL':
        aggression = 0
    print(f"Aggression = {aggression}")
    declareFlag = False
    runs, wickets = 0, 0
    balls = 0
    while(True):
        declare = input().upper()
        if len(declare) > 0:
            declareFlag = True
            break
        if wickets >= 10:
            break
        runs, wickets = map_prob_to_score(runs, wickets, aggression, outfield, pitch, 2, balls)
        balls += 1
        global_balls += 1
        if global_balls > global_ball_limit:
            drawn_match(innings1, innings1_runs, innings1_wickets, innings2, runs, wickets)
            return
        if balls == 30 and pitch == 'GREEN':
            aggression = 0
            print("aggression changed to 0")
        if balls == 60 and pitch == 'GREEN':
            aggression = -1
            print("aggression changed to -1")
        if runs < innings1_runs:
            print(f"{innings2}: {runs}/{wickets}, Overs {balls//6}.{balls%6}, trail by {innings1_runs - runs}", end='\r')
        elif runs > innings1_runs:
            print(f"{innings2}: {runs}/{wickets}, Overs {balls//6}.{balls%6}, lead by {runs - innings1_runs}", end='\r')
        else:
            print(f"{innings2}: {runs}/{wickets}, Overs {balls//6}.{balls%6}, scores level", end='\r')
        
    innings2_res = f'{innings2} - {runs} all out' if declareFlag == False else f'{innings2} - {runs}/{wickets} declared'
    if declareFlag == False:
        print(f"End of Innings 2: {innings2} - {runs} all out")
    else:
        print(f"End of Innings 2: {innings2} - {runs}/{wickets} declared")

    innings2_runs = runs #Setup for innings 3
    innings2_wickets = wickets

    print("------------------------------------End of first round----------------------------------")
    print(f"Innings 1: {innings1_res}")
    print(f"Innings 2: {innings2_res}")
    print(f"Global Ball count = {global_balls}/{global_ball_limit}")

    innings3 = ''
    follow_on_flag = False
    if innings1_runs - innings2_runs > 200:
        print(f"Does {innings1} want to enforce the follow on? (Y/N)")
        if input().upper() == 'Y':
            follow_on_flag = True
            innings3 = innings2
        else:
            follow_on_flag = False
            innings3 = innings1
    else:
        follow_on_flag = False
        innings3 = innings1

    #----------Innings 3-------------
    print("------------------------------------Innings 3----------------------------------")
    print("Press any key to declare. Otherwise, just hit enter to continue.")
    if pitch == 'GREEN':
        aggression = random.randint(-1, 0)
    if pitch == 'DRY':
        aggression = random.randint(0, 1)
    if pitch == 'FLAT':
        aggression = random.randint(-1, 0)
    if pitch == 'NORMAL':
        aggression = 0
    print(f"Aggression = {aggression}")
    declareFlag = False
    runs, wickets = 0, 0
    balls = 0
    while(True):
        declare = input().upper()
        if len(declare) > 0:
            declareFlag = True
            break
        if wickets >= 10:
            break
        runs, wickets = map_prob_to_score(runs, wickets, aggression, outfield, pitch, 3, balls)
        balls += 1
        if not follow_on_flag:
            if runs + innings1_runs < innings2_runs:
                print(f"{innings3}: {runs}/{wickets}, Overs {balls//6}.{balls%6}, trail by {innings2_runs - runs - innings1_runs}", end='\r')
            elif runs + innings1_runs > innings2_runs:
                print(f"{innings3}: {runs}/{wickets}, Overs {balls//6}.{balls%6}, lead by {runs + innings1_runs - innings2_runs}", end='\r')
            else:
                print(f"{innings3}: {runs}/{wickets}, Overs {balls//6}.{balls%6}, scores level", end='\r')
        else:
            if runs + innings2_runs < innings1_runs:
                print(f"{innings3}: {runs}/{wickets} (f/o), Overs {balls//6}.{balls%6}, trail by {innings1_runs - runs - innings2_runs}", end='\r')
            elif runs + innings2_runs > innings1_runs:    
                print(f"{innings3}: {runs}/{wickets} (f/o), Overs {balls//6}.{balls%6}, lead by {runs + innings2_runs - innings1_runs}", end='\r')
            else:    
                print(f"{innings3}: {runs}/{wickets} (f/o), Overs {balls//6}.{balls%6}, scores level", end='\r')
        global_balls += 1
        if global_balls > global_ball_limit:
            drawn_match(innings1, innings1_runs, innings1_wickets, innings2, innings2_runs, innings2_wickets, innings3, runs, wickets)
            return

    if not follow_on_flag:
        innings3_res = f'{innings3} - {runs} all out' if declareFlag == False else f'{innings3} - {runs}/{wickets} declared'
    else:
        innings3_res = f'{innings3} - {runs} (f/o) all out' if declareFlag == False else f'{innings3} - {runs}/{wickets} (f/o) declared'
    if declareFlag == False:
        if not follow_on_flag:
            print(f"End of Innings 3: {innings3} - {runs} all out")
        else:
            print(f"End of Innings 3: {innings3} - {runs} (f/o) all out")
    else:
        if not follow_on_flag:
            print(f"End of Innings 3: {innings3} - {runs}/{wickets} declared")
        else:
            print(f"End of Innings 3: {innings3} - {runs}/{wickets} (f/o) declared")
    print(f"Global Ball count = {global_balls}/{global_ball_limit}")

    innings3_runs = runs #Setup for innings 3
    innings3_wickets = wickets

    innings4 = ''
    target = 0
    balls = 0
    if follow_on_flag:
        if runs + innings2_runs < innings1_runs:
            print("Results: ")
            print(f"Innings 1: {innings1_res}")
            print(f"Innings 2: {innings2_res}")
            print(f"Innings 3: {innings3_res} (follow on)")
            print(f"{innings1} wins by an innings and {innings1_runs - innings3_runs - innings2_runs} runs")
            return
        else:
            innings4 = innings1
            target = innings2_runs + innings3_runs - innings1_runs + 1
            print(f"Target for {innings4} = {target}")
    else:
        if runs + innings1_runs < innings2_runs:
            print("Results: ")
            print(f"Innings 1: {innings1_res}")
            print(f"Innings 2: {innings2_res}")
            print(f"Innings 3: {innings3_res}")
            print(f"{innings2} wins by an innings and {innings2_runs - innings3_runs - innings1_runs} runs")
            return
        else:
            innings4 = innings2
            target = innings1_runs + innings3_runs - innings2_runs + 1
            print(f"Target for {innings4} = {target}")

    #----------Innings 4-------------
    print("------------------------------------Innings 4----------------------------------")
    print("Press any key to declare. Otherwise, just hit enter to continue.")
    if pitch == 'GREEN':
        aggression = random.randint(-1, 0)
    if pitch == 'DRY':
        aggression = random.randint(0, 1)
    if pitch == 'FLAT':
        aggression = random.randint(-1, 0)
    if pitch == 'NORMAL':
        aggression = 0
    print(f"Aggression = {aggression}")
    target_met = False
    declareFlag = False
    runs, wickets = 0, 0
    while(True):
        declare = input().upper()
        if len(declare) > 0:
            declareFlag = True
            break
        if wickets >= 10:
            break
        if runs >= target:
            target_met = True   
            break
        runs, wickets = map_prob_to_score(runs, wickets, aggression, outfield, pitch, 4, balls)
        balls += 1
        print(f"{innings4}: {runs}/{wickets}, Overs {balls//6}.{balls%6}, need {target - runs} runs to win", end='\r')
        global_balls += 1
        if global_balls % 50 == 0:
            print(f"\nGlobal Ball count so far = {global_balls}/{global_ball_limit}")
        if global_balls > global_ball_limit:
            drawn_match(innings1, innings1_runs, innings1_wickets, innings2, innings2_runs, innings2_wickets, innings3, innings3_runs, innings3_wickets, innings4, runs, wickets, target)
            return

    innings4_runs = runs #Final runs
    innings4_wickets = wickets
    innings4_res = f'{innings4} - {runs}/{wickets}' if target_met == True or declareFlag == True else f'{innings4} - {runs} all out'
    print("------------------------------------End of match----------------------------------")
    print(f"Innings 1: {innings1_res}")
    print(f"Innings 2: {innings2_res}")
    print(f"Innings 3: {innings3_res}")
    print(f"Innings 4: {innings4_res} (Target = {target})")
    print(f"Global Ball count = {global_balls}/{global_ball_limit}")

    if target - innings4_runs - 1 == 0:
        print(f"Match is tied!")
        return
    if target_met:
        print(f"{innings4} wins by {10 - innings4_wickets} wickets.")
    else:
        print(f"{innings3} wins by {target - innings4_runs - 1} runs.")

match()   
