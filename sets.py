#Sets in python

info = {"Saugat", False, 19,"Hello"}
# set occur in random order so we cannot aceess using index method
print(info)
#to print type of empty set we need to use name = set() or else it will print dict.
name = {}
print(type(name))
name2=set()
print(type(name2))

#using for loop in set
for i in info:
    print(i)

#set methods in python
s1={1,2,5,6}
s2={3,6,7}
print(s1)
s1.update(s2) 
print(s1,s2)


city = {"Tokiyo", "Madrid", "Berlin","Delhi"}
city2 = {"Tokiyo", "Seoul","Kabul","Madrid"}
#prints everything from the set
city3= city.union(city)
print(city3)

city4 = city.intersection(city2)
print(city4)
#it updates the city 
# city.intersection_update(city2)
# print(city)

#it prints except the intersection
city5 = city.symmetric_difference(city2) 
print(city5)

city6 = city.difference(city2)
print(city6)

city7=city.isdisjoint(city2)
print(city7)

city.remove("Tokiyo")
print(city)