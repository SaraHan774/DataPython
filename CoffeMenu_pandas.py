import pandas as pd

Coffee = {
        "espresso" : [3.5, 4.0], "americano" : [3.5, 4.0] ,
        "cafelatte" : [3.8, 4.3] , "cappucino" : [3.8, 4.3]
        ,"Price" : ["Hot", "Cold"]}
data = pd.DataFrame(Coffee)
HotOrCold = data.set_index("Price")
print(HotOrCold)



#output_is: 

#          espresso  americano  cafelatte  cappucino
#Price                                           
#Hot         3.5        3.5        3.8        3.8
#Cold        4.0        4.0        4.3        4.3
