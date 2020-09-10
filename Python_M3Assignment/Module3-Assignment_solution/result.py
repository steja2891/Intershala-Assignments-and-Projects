import cricket_functions

p1 = {'name': 'Virat Kohli', 'role': 'bat', 'runs': 112, '4': 10, '6': 0, 'balls': 119, 'field': 0}
p2 = {'name': 'du Plessis', 'role': 'bat', 'runs': 120, '4': 11, '6': 2, 'balls': 112, 'field': 0}
p3 = {'name': 'Bhuvneshwar Kumar', 'role': 'bowl', 'wkts': 1, 'overs': 10, 'runs': 71, 'field': 1}
p4 = {'name': 'Yuzvendra Chahal', 'role': 'bowl', 'wkts': 2, 'overs': 10, 'runs': 45, 'field': 0}
p5 = {'name': 'Kuldeep Yadav', 'role': 'bowl', 'wkts': 3, 'overs': 10, 'runs': 34, 'field': 0}

dic1 = cricket_functions.Total_points_bat(p1)
dic2 = cricket_functions.Total_points_bat(p2)
dic3 = cricket_functions.Total_points_bowl(p3)
dic4 = cricket_functions.Total_points_bowl(p4)
dic5 = cricket_functions.Total_points_bowl(p5)

final_list = [dic1, dic2, dic3, dic4, dic5]
for i in final_list:
    print(i)

scores = []
for j in final_list:
    if "batscore" in j:
        points = j.get("batscore")
        scores.append(points)
    else:
        points = j.get("bowlscore")
        scores.append(points)

temp = max(scores)
print()
for score in final_list:
    if "batscore" in score:
        if temp == score.get("batscore"):
            print("Now, the Man-of-the-Match award goes to {} with {} points".format(score.get("name"), max(scores)))
            print("congratualtions {}".format(score.get("name")))
            break
    else:
        if temp == score.get("bowlscore"):
            print("Now, the Man-of-the-Match award goes to {} with {} points".format(score.get("name"), max(scores)))
            print("Congratualtions {}".format(score.get("name")))
            break
