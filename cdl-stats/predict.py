import pandas as pd

matchday_amount = 5


def get_all_invidual_qualifier_results(schedule: pd.DataFrame):
    results = pd.DataFrame(columns=schedule.columns)

    # TODO split schedule into matchdays
    for _, row in schedule.iterrows():
        order = row["ORDER"]
        team_a = row["TEAM A"]
        team_b = row["TEAM B"]

        for i in range(3):
            results = results.append({
                "ORDER": order,
                "TEAM A": team_a,
                "TEAM B": team_b,
                "MAPS A": 3,
                "MAPS B": i,
            }, ignore_index=True)

            results = results.append({
                "ORDER": order,
                "TEAM A": team_b,
                "TEAM B": team_a,
                "MAPS A": 3,
                "MAPS B": i,
            }, ignore_index=True)

    return results


def get_all_qualifier_results_combinations(results: pd.DataFrame):
    combinations = []
    for i in range(0, len(results)):
        print(results[i])

    return combinations


def get_all_qualifier_standings(standings: pd.DataFrame, results: pd.DataFrame):
    all_qualifier_standings: list(pd.DataFrame) = []

    for _, row in results.iterrows():
        qs = pd.DataFrame(columns=standings.columns)

    return all_qualifier_standings
