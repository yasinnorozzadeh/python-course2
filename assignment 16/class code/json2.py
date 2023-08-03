import json
data = {
    "manu":"bruno"
}
test_var = json.dumps(data)
# with open("path.json", "r") as j_f:
#     str_data = json.loads(j_f)

print(type(test_var))
print(test_var.items())