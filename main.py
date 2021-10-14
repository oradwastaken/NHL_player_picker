def main():
    from hockey_classes import Rankings

    # Load Ranking data from CSV file
    player_rankings = Rankings()
    # player_rankings.from_hockey_reference()
    player_rankings.from_csv('rankings.csv')

    while True:
        print(player_rankings)
        player_rankings.random_matchup()
        player_rankings.to_csv('rankings.csv')


if __name__ == '__main__':
    main()