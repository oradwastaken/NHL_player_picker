def main():
    from hockey_stuff import Player, Position, SkaterStats, GoalieStats
    from datetime import date

    player1 = Player('Brayden Point', 'Tampa Bay Lightning', date(1996, 3, 13), 1000, Position.RW, 56,
                     SkaterStats(G=23, A=25, Blk=18, Hit=23))
    player2 = Player('Victor Olofsson', 'Buffalo Sabres', date(1995, 7, 18), 1000, Position.RW, 56,
                     SkaterStats(G=13, A=19, Blk=12, Hit=17))

    print(player1.skater_stats)
    # print(player2.G)


if __name__ == '__main__':
    main()
