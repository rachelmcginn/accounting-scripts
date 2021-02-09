"""Print out all the melons in our inventory."""


from melons import melon_data

def print_all_melons():
    """Print each melon with corresponding attribute information."""

    for i in melon_data:
        print(f"\n{melon_data[i]['Name']}:")
        print(f"\tPrice: {melon_data[i]['Price']}")
        print(f"\tSeedless: {melon_data[i]['Seedless']}")
        print(f"\tFlesh color: {melon_data[i]['Flesh color']}")
        print(f"\tWeight: {melon_data[i]['Weight']}")
        print(f"\tRind color: {melon_data[i]['Rind color']}")
        print(f"\tOrigin: {melon_data[i]['Origin']}")
        print("===========================")

print_all_melons()
