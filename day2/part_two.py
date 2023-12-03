import re

# Possible:
# 12 red cubes
# 13 green cubes
# 14 blue cubes
RULES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}


def get_input(src: str) -> list[str]:
    games = []
    with open(src, "r") as f:
        for line in f:
            games.append(line.strip())
    return games


def organize_colors(game_set: list[str]) -> list[dict[str, int]]:
    plays = []
    for sets in game_set:
        cubes = sets.split(", ")
        cubes_dict = {}
        for cube in cubes:
            play = re.findall(r"\d+|\w+", cube)
            cubes_dict[play[-1]] = int(play[0])
        plays.append(cubes_dict)
    return plays


def organize_games(games: str) -> dict[str, list[str, int]]:
    arranged_games = {}
    for game in games:
        game_id = re.search(r"Game\s(\d+):", game).group(1)
        game_sets = re.findall(r"(?<=:|;)\s(.*?)(?=;|$)", game)
        plays = organize_colors(game_sets)
        arranged_games[game_id] = plays
    return arranged_games


def get_max_color(games: list[dict[str, int]]) -> dict[str, int]:
    maximum = {
        "red": 0,
        "blue": 0,
        "green": 0,
    }
    for game in games:
        maximum["red"] = max(maximum.get("red"), game.get("red", 0))
        maximum["green"] = max(maximum.get("green"), game.get("green", 0))
        maximum["blue"] = max(maximum.get("blue"), game.get("blue", 0))

    return maximum


def sum_games_power(arranged_games: dict[str, list[str, int]]) -> int:
    total = 0
    for id, games in arranged_games.items():
        maximum = get_max_color(games)
        total += maximum["red"] * maximum["green"] * maximum["blue"]
    return total


def main():
    games = get_input("input.txt")
    arranged_games = organize_games(games)
    total = sum_games_power(arranged_games)
    print(total)


if __name__ == "__main__":
    main()
