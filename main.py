def main():
    from hockey_stuff import Player, Position, SkaterStats, GoalieStats, Rankings
    from datetime import date

    player_rankings = Rankings()
    player_rankings.read_list_from_file()

    # player_rankings.add_player(Player('Brayden Point', 'Tampa Bay Lightning', date(1996, 3, 13), 1000, Position.RW, 56,
    #                                   SkaterStats(G=23, A=25, Blk=18, Hit=23)))
    # player_rankings.add_player(Player('Victor Olofsson', 'Buffalo Sabres', date(1995, 7, 18), 1000, Position.RW, 56,
    #                                   SkaterStats(G=13, A=19, Blk=12, Hit=17)))
    # player_rankings.add_player(Player('Connor McDavid', 'Edmonton Oilers', date(1997, 1, 13), 1000, Position.C, 56,
    #                                   SkaterStats(G=33, A=72, Blk=24, Hit=61)))
    # player_rankings.add_player(Player('Carey Price', 'Montreal Canadiens', date(1987, 8, 16), 1000, Position.G, 25,
    #                                   GoalieStats(W=12, L=7, GAA=2.64, SVPcT=.901, SO=1)))
    # player_rankings.add_player(Player('Marc-Andre Fleury', 'Chicago Blackhawks', date(1984, 11, 28), 1000, Position.G, 36,
    #                                   GoalieStats(W=26, L=10, GAA=1.98, SVPcT=.928, SO=6)))

    while True:
        print(player_rankings)
        player_rankings.random_matchup()
        player_rankings.write_list_to_file()


if __name__ == '__main__':
    main()
