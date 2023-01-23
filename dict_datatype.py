myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}

print(myFavoriteFruitDictionary)
print(myFavoriteFruitDictionary["Akua"])

myFavoriteFruitDictionary["Akua"] = "1" 

print(myFavoriteFruitDictionary["Akua"])
print(myFavoriteFruitDictionary)

myFavoriteFruitDictionary["1"] = "2"
print(myFavoriteFruitDictionary)

del myFavoriteFruitDictionary ["1"]
print(myFavoriteFruitDictionary)