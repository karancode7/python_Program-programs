import json

data={
    "name": "8DP1",
    "discription": "jason and detetime",
    "author": "your name",
    "version": "1.0",


}

print("privious data",data)
print("privious data", type(data))

s=json.dumps(data)
print("data after json",s)
print("data after json",type(s))