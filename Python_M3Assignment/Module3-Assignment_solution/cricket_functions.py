# batting_points Function:

def batting_function(dict):
    runs = dict.get("runs")
    balls_faced = dict.get("balls")
    strike_rate = int((runs / balls_faced) * 100)
    fours = dict.get("4")
    sixes = dict.get("6")
    batting_points = 0
    if runs >= 50:
        batting_points += 5
    if runs >= 100:
        batting_points += 10
    if strike_rate in range(80, 101):
        batting_points += 2
    if strike_rate > 100:
        batting_points += 4
    if fours > 0:
        batting_points += fours * 1
    if sixes > 0:
        batting_points += sixes * 2
    batting_points += runs // 2
    return batting_points


# bowling_points Function:

def bowling_function(dict):
    wickets_taken = dict.get("wkts")
    overs_bowled = dict.get("overs")
    runs_given = dict.get("runs")
    economy_rate = runs_given // overs_bowled
    bowling_points = 0
    bowling_points += wickets_taken * 10
    if wickets_taken == 3:
        bowling_points += 5
    if wickets_taken >= 5:
        bowling_points += 10
    if 3.5 < economy_rate < 4.5:
        bowling_points += 4
    elif 2 < economy_rate < 3.5:
        bowling_points += 7
    elif economy_rate < 2:
        bowling_points += 10
    return bowling_points


def fielding_function(dict):
    no_of_fields = dict.get("field")
    fielding_points = 0
    fielding_points += no_of_fields * 10
    return fielding_points

def Total_points_bat(dict):
    return {"name":dict.get("name"), "batscore":batting_function(dict)+fielding_function(dict)}

def Total_points_bowl(dict):
    return {"name":dict.get("name"), "bowlscore":bowling_function(dict)+fielding_function(dict)}