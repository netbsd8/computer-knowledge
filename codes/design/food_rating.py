from collections import defaultdict, heappush, heappop
from typing import List


class FoodRatings:
    # using heap to get sorted during each changeRate call
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.f2r = defaultdict(int)
        self.f2c = {}
        self.c2rf = defaultdict(list)

        for i in range(len(foods)):
            self.f2r[foods[i]] = -ratings[i]
            self.f2c[foods[i]] = cuisines[i]
            heappush(self.c2rf[cuisines[i]], (-ratings[i], foods[i]))
    
    def changeRating(self, food: str, newRating: int) -> None:
        self.f2r[food] = -newRating
        heappush(self.c2rf[self.f2c[food]], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # if the max rate is not the same with the newest rate in f2r
        # old rate and discard it
        while self.c2rf[cuisine] and self.f2r[self.c2rf[cuisine][0][1]] != self.c2rf[cuisine][0][0]:        
            heappop(self.c2rf[cuisine])

        return self.c2rf[cuisine][0][1]

    # # timeout
    # def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    #     self.cuisine_map = collections.defaultdict(set)
    #     self.food_map = {}

    #     for food, cuisine in zip(foods, cuisines):
    #         self.cuisine_map[cuisine].add(food)

    #     for rating, food in zip(ratings, foods):
    #         self.food_map[food] = rating
        

    # def changeRating(self, food: str, newRating: int) -> None:
    #     self.food_map[food] = newRating

    # def highestRated(self, cuisine: str) -> str:
    #     foods = self.cuisine_map[cuisine]

    #     ret = []
    #     cur_rate = -1
    #     for food in foods:
    #         if self.food_map[food] == cur_rate:
    #             ret.append(food)
    #         elif self.food_map[food] > cur_rate:
    #             cur_rate = self.food_map[food]
    #             ret = [food]

    #     return sorted(ret)[0]



# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)