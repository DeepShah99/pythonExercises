# access value 23
from pickle import NONE


head = {"value" : 11, "next": 
                            {"value" : 3, "next": 
                                                {"value" : 23, "next" : 
                                                                      {"value" : 7, "next" : NONE}}}}


print(head["next"]["next"]["value"])

#this will only work with LL
#print(myLL.head.next.next.value)