import requests
import json



# >>> api_url = "https://jsonplaceholder.typicode.com/todos/10"
# >>> response = requests.get(api_url)
# >>> response.json()
# {'userId': 1, 'id': 10, 'title': 'illo est ... aut', 'completed': True}
#
# >>> todo = {"userId": 1, "title": "Wash car", "completed": True}
# >>> response = requests.put(api_url, json=todo)
# response.json()
# todo = {"title": "Mow lawn"}
# >>> response = requests.patch(api_url, json=todo)
# api_url = "https://jsonplaceholder.typicode.com/todos/10"
# >>> response = requests.delete(api_url)
# >>> response.json()




# https://dailyjournal.gitbook.io/hackerrank-solutions/certify/rest-api-intermediate


def getTotalGoals(team='Barcelona', year=2011):
    """
    The function must fetch all the matches that a given team played in the given year
    :param team:
    :param year:
    :return:
    """

    # BASE_URL = 'https://fakestoreapi.com'
    matches_url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year)
    # hr_url = 'https://jsonmock.hackerrank.com/api/football_matches/discovery'
    # response = requests.get(f"{BASE_URL}/products")
    wins = 0
    home_away = ["team1", "team2"]
    for _ in home_away:
        params = {
            _: str(team),
        }
        response = requests.get(f"{matches_url}", params=params)
        # print(response.json())
        # print('Status Code:', response.status_code)
        tw_json = response.json()
        for __ in tw_json['data']:
            if _ == "team1":
                wins += int(__['team1goals'])
            elif _ == "team2":
                wins += int(__['team2goals'])
    print(team + ' Wins:', wins)
    # goals in the year = 35, team barcelona
    return wins

def getNumDraws(year=2011):
    """
    The function must return an integer denoting the number of matches in the given year that ended up in a draw.
    You can safely assume that no team ever scored more than 10 goals.
    :param year:
    :return: draws
    """
    # BASE_URL = 'https://fakestoreapi.com'
    matches_url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year)
    # hr_url = 'https://jsonmock.hackerrank.com/api/football_matches/discovery'
    # response = requests.get(f"{BASE_URL}/products")
    draws = 0
    for _ in range(11):
        params = {
                    "team1goals": str(_),
                    "team2goals": str(_),
            # 'filter': 'team1goals==1',
                  }

        response = requests.get(f"{matches_url}", params=params)
        # print(response.json())
        # print('Status Code:', response.status_code)

        draws += response.json()['total']
    print('Draws:', draws)
    # 516
    return draws

def getWinnerTotalGoals(competition='English Premier League',year=2011):
    """
    The function must return an integer denoting the total number of goals
     scored in all matches in the given competition by the team who won the competition.
    :param competition:
    :param year:
    :return: t_goals
    """
    comp_url = 'https://jsonmock.hackerrank.com/api/football_competitions?name=' + str(competition) + '&year=' + str(year)
    comp_params = {}
    comp_response = requests.get(f"{comp_url}", params=comp_params)
    comp_json = comp_response.json()

    winner = comp_json['data'][0]['winner']

    #////////////////
    matches_url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year)
    matches_params = {
        "team1": str(winner),
        "competition": str(competition)
    }
    matches_response = requests.get(f"{matches_url}", params=matches_params)
    matches_json = matches_response.json()
    total_pages_1 = matches_json['total_pages']
    #////////////////
    goals_1 = 0
    for _ in range(1, total_pages_1 + 1):
        matches_url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year)
        params_t1 = {
            # 'filter': 'team1=' + winner + ' OR team2=' + winner,
            "team1": str(winner),
            "page": int(_),
            "competition": str(competition)
        }
        response = requests.get(f"{matches_url}", params=params_t1)
        pages_json = response.json()
        for __ in pages_json['data']:
            if __['team1'] == winner:
                goals_1 += int(__['team1goals'])
    # ////////////////
    matches_url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year)
    matches_params = {
        "team2": str(winner),
        "competition": str(competition)
    }
    matches_response = requests.get(f"{matches_url}", params=matches_params)
    matches_json = matches_response.json()
    total_pages_2 = matches_json['total_pages']
    # ////////////////
    goals_2 = 0
    for _ in range(1, total_pages_2 + 1):
        matches_url = 'https://jsonmock.hackerrank.com/api/football_matches?year=' + str(year)
        params_t2 = {
            # 'filter': 'team1=' + winner + ' OR team2=' + winner,
            "team2": str(winner),
            "page": int(_),
            "competition": str(competition)
        }
        response_ = requests.get(f"{matches_url}", params=params_t2)
        pages_json = response_.json()
        for __ in pages_json['data']:
            if __['team2'] == winner:
                goals_2 += int(__['team2goals'])

    t_goals = goals_1 + goals_2
    print(t_goals)
    # totalWinGoals = 28
    return t_goals


if __name__ == '__main__':

    team = 'Barcelona'
    years = list(range(2011, 2016))
    for _ in years:
        print('Year:', _)
        getTotalGoals(team, _)
    print('////////////////')
    years = list(range(2011, 2016))
    for _ in years:
        print('Year:', _)
        getNumDraws(_)
    print('////////////////')
    # competition = 'English Premier League'
    competition = "UEFA Champions League"
    year = 2011
    print('Year:', year)
    print('Competition:', competition)
    getWinnerTotalGoals(competition, year)
    print('////////////////')

