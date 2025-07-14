from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        n=len(foods)
        self.food_rating={}
        self.food_cui={}
        self.ratings=ratings
        self.cui_ord_set=defaultdict(SortedSet)
        for i in range(n):
            self.food_rating[foods[i]]=ratings[i]
            self.food_cui[foods[i]]=cuisines[i]
            self.cui_ord_set[cuisines[i]].add((-ratings[i], foods[i]))
            
    def changeRating(self, food: str, newRating: int) -> None:
        cui_name=self.food_cui[food]
        old_element=(-self.food_rating[food], food)
        self.cui_ord_set[cui_name].remove(old_element)
        self.food_rating[food]=newRating
        self.cui_ord_set[cui_name].add((-newRating, food))
    def highestRated(self, cuisine: str) -> str:
        high_rated=self.cui_ord_set[cuisine][0]
        return high_rated[1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)