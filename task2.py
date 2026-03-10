capitals={
    "France":"Paris",
    "Germany":"Berlin",
}
travel_log ={
    "France":["paris","Lille","Dijon"],
    "Germany":["Stuttgart","Berlin"],
}
print(travel_log["France"][1])
nested_list=["A","B",["C","D"]]
print(nested_list[2][1])

travel_log ={
    "France":{
        "cities_visited":["paris","Lille","Dijon"],
        "total_vists":12
        },
    "Germany":{
         "cities_visited":["Berlin","Hamburg","Stuttgart"],
        "total_vists":12
        },
}

print(travel_log["Germany"]["cities_visited"][2])