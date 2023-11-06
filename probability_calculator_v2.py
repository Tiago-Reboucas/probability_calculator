import copy
import random


class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        for color, count in kwargs.items():
            for n in range(count):
                self.contents.append(color)

    def draw(self, balls: int) -> list:
        self.drawn_balls = []
        
        if balls >= len(self.contents):
            return self.contents
        else:
            for i in range(balls):
                drawn = random.choice(self.contents)
                self.drawn_balls.append(drawn)
                self.contents.remove(drawn)
            return self.drawn_balls


def list_to_dict(l: list) -> dict:
    dic = {}
    for item in l:
        dic[item] = dic.get(item, 0) + 1
    return dic

def check_quantities(check: dict, have: dict):
    for k, v in have.items():
        if v <= check.get(k, 0): continue
        else: return False
    return True


def experiment(hat: object, expected_balls: dict, num_balls_drawn: int, num_experiments: int) -> float:
    m = 0
    for n in range(num_experiments):
        # print(f"\nExperiment {n}:")
        # print("Base dict:", hat.contents)
        hat_copy = copy.deepcopy(hat)
        # print("Copy dict:", hat_copy.contents)
        drawn_l = hat_copy.draw(num_balls_drawn)
        drawn_d = list_to_dict(drawn_l)
        # print("Drawn:", drawn_d)
        
        if check_quantities(drawn_d, expected_balls): 
            m += 1
            # print("M =", m)

    return m/num_experiments


def deviation(answer: float, expected: float) -> float:
    return round((answer-expected)/expected * 100, 3)



###################################################### TESTS ######################################################
# ----- Test 1 -----
print("\n" + " Test 1 - test_hat_class_contents ".center(50, "*"))
print("Case 1 -")
hat = Hat(red=3,blue=2)
print("Contents:", hat.contents)
expected = ["red","red","red","blue","blue"]
print("Expected:", expected)
print("They are the same?", hat.contents == expected)

print("\nCase 2 -")
hat2 = Hat(yellow=3, blue=2, green=6)
print("Contents from hat:", hat.contents)
print("Contents from hat2:", hat2.contents)
expected = ["yellow","yellow","yellow","blue","blue","green","green","green","green","green","green"]
print("Expected:", expected)
print("They are the same?", hat2.contents == expected)

# print("\nCase 3 -")
# hat3 = Hat(red=5, orange=4)
# print("Contents:", hat3.contents)
# expected = ["red","red","red","red","red","orange","orange","orange","orange"]
# print("Expected:", expected)
# print("They are the same?", hat3.contents == expected)

# print("\nCase 4 -")
# hat4 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=3)
# print("Contents:", hat4.contents)
# expected = ["red","red","red","red","red","orange","orange","orange","orange","black","pink","pink","striped","striped","striped"]
# print("Expected:", expected)
# print("They are the same?", hat4.contents == expected)

# ----- Test 2 -----
# hat = 1
# print(hat)
print("\n" + " Test 2 - test_hat_draw ".center(50, "*"))
hat = Hat(red=5,blue=2)
draw = hat.draw(2)
print("Draw:", draw)
print("Rest:", hat.contents)
print("Expected:", ['blue', 'red'], "(OBS: Can`t be expected a perfect match due to randomness)\n")

print("Contents length:", len(hat.contents), hat.contents)
print("Expected:", 5)
print("They are the same?", len(hat.contents) == 5)

# ----- Test 3 -----
print("\n" + " Test 3 - test_prob_experiment ".center(50, "*"))
hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
expected = 0.272
print("Case 1 -\nProbability:", probability)
print("Expected:", expected)
print(f"Deviation: {deviation(probability, expected)}%")

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability = experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
expected = 1.0
print("\nCase 2 -\nProbability:", probability)
print("Expeced:", expected)
print(f"Deviation: {deviation(probability, expected)}%")