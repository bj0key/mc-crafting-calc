from recipebook import recipebook

def get_materials(product):
    "Get the materials recursively required for an item."
    if product in recipebook:
        direct_recipe = recipebook[product] # the direct recipe for the item
        total_materials = {}
        for shallow_part, shallow_amount in direct_recipe.items(): # "shallow" this-level of recursion parts
            indirect_recipe = get_materials(shallow_part)
            for deep_part, deep_amount in indirect_recipe.items(): # "deep" already exhausted parts coming back up through the recursion
                total_materials[deep_part] = total_materials.get(deep_part, 0) + deep_amount*shallow_amount 
        return total_materials
    else:
        return {product:1}


def get_materials_pretty():
    item = input("What item would you like the components for?\n")
    print("="*64)
    material_dict = get_materials(item)
    for material, amount in material_dict.items():
        stack, single = divmod(amount, 64)
        print(material.ljust(32), f"{stack} stacks + {single}".ljust(24), f"({amount})")


def main():
    get_materials_pretty()
    pass


if __name__ == "__main__":
    main()
    input()