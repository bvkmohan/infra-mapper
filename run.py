import yaml

with open("inventory.yml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
    except yaml.YAMLError as exc:
        print(exc)

for i in data["networks"]:
    for network, values in i.items():
        print(network + " -> " + str(values["node"]))
