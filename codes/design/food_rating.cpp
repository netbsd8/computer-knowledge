#include "../base.h"

class FoodRatings {
private:
    unordered_map<string, set<pair<int, string>>> cuisineRates_;
    unordered_map<string, int> foodRates_;
    unordered_map<string, string> foodCuisines_;

public:
    FoodRatings(vector<string>& foods, vector<string>& cuisines, vector<int>& ratings) {
        for (int i = 0; i < foods.size(); i++) {
            foodRates_[foods[i]] = ratings[i];
            foodCuisines_[foods[i]] = cuisines[i];
            cuisineRates_[cuisines[i]].insert({-ratings[i], foods[i]});
        }
    }
    
    void changeRating(string food, int newRating) {
        auto& cuisine = foodCuisines_.find(food)->second;
        cuisineRates_[cuisine].erase({-foodRates_[food], food});
        cuisineRates_[cuisine].insert({-newRating, food});
        foodRates_[food] = newRating;
    }
    
    string highestRated(string cuisine) {
        return cuisineRates_[cuisine].begin()->second;
    }
};

/**
 * Your FoodRatings object will be instantiated and called as such:
 * FoodRatings* obj = new FoodRatings(foods, cuisines, ratings);
 * obj->changeRating(food,newRating);
 * string param_2 = obj->highestRated(cuisine);
 */