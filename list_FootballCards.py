team_A_list=["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10","A-11"]
team_B_list=["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10","B-11"]
red_lst = []
red_lst = [item for item in input("Enter the red card holder as list items : ").split()]
print(red_lst)
team_A_list = [ele for ele in team_A_list if ele not in red_lst]
#print(team_A_list)
team_B_list = [ele for ele in team_B_list if ele not in red_lst]
#print(team_B_list)
print("Team A - " + str(len(team_A_list)) + "; Team B - " + str(len(team_B_list)))
if len(team_A_list)<7:
    print("Game was terminated")
if len(team_B_list)<7:
    print("Game was terminated")