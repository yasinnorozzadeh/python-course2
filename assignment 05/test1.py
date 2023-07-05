score = 39
threshhold = 35
# if score > threshhold:
#     state = "good"
# else:
#     state = "bad"

# print(state)

##short hand if
state = "good" if (score > threshhold) else "bad"
print(state)