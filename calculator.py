#==================================
#classroom points calculator
#==================================

#==Assignment operator==
#store the points earned by 5 classrooms teams
Team1 = 123
Team2 = 143
Team4 = 111
Team5 = 120

#==Arithmetic operators (+,-,*,/,)==
#calculating total and average
total = Team1 + Team2 +  Team4 + Team4
average = total / 5

print("total points:", total)
print("average per team:", average)

#each point give 4 reward stars
star_per_points = 4
reward_stars = total * star_per_points
print("star per points:", reward_stars)

#==floor division (//) and modulus (%)==
#packing reward stars into boxes of 25 stars each
boxes = reward_stars // 25
leftover = reward_stars % 25
print("full boxes packed:", boxes)
print("leftover stars:", leftover)

#==comparision operators (<,>,==,>=)==
#compare this week's points with the last week's points
last_week_points = 500

    




