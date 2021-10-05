def main():
    from hockey_stuff import Player, Position, SkaterStats, GoalieStats, Rankings
    from datetime import date

    player_rankings = Rankings()
    player_rankings.add_player(Player('Brayden Point', 'Tampa Bay Lightning', date(1996, 3, 13), 1000, Position.RW, 56,
                                      SkaterStats(G=23, A=25, Blk=18, Hit=23)))
    player_rankings.add_player(Player('Victor Olofsson', 'Buffalo Sabres', date(1995, 7, 18), 1000, Position.RW, 56,
                                      SkaterStats(G=13, A=19, Blk=12, Hit=17)))
    player_rankings.add_player(Player('Carey Price', 'Montreal Canadiens', date(1987, 8, 16), 1000, Position.G, 25,
                                      GoalieStats(W=12, L=7, GAA=2.64, SVPcT=.901, SO=1)))

    while True:
        print(player_rankings)
        player_rankings.random_matchup()

if __name__ == '__main__':
    main()
