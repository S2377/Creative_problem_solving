def valid_teams(ratings):
    def is_team(a,b,c):
            if a < b < c or a > b > c :
                return True
    count = 0
    for i in range(len(ratings)):
        if i < len(ratings) -2:
            if is_team(ratings[i],ratings[i+1],ratings[i+2]) :
                count += 1
    print(count)