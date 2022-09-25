from recipebook import recipebook as rb

def get_materials(product: str) -> dict[str, int]:
    "Get the materials recursively required for an item."
    if product not in rb:
        return {product: 1}

    direct_recipe = rb[product]  # the direct recipe for the item
    total_materials = {}
    for (shallow_part, shallow_amount) in direct_recipe.items():
        indirect_recipe = get_materials(shallow_part)
        for (deep_part, deep_amount) in indirect_recipe.items():
            # "deep" already exhausted parts coming back up through the recursion
            total_materials[deep_part] = (
                total_materials.get(deep_part, 0) + deep_amount * shallow_amount
            )
    return total_materials


def get_materials_pretty(item) -> str:
    output = []
    output.append(" [ MATERIALS ] ".center(64, "="))
    material_dict = get_materials(item)
    for material, amount in material_dict.items():
        stack, single = divmod(amount, 64)
        stacks_str = f"{stack} stacks + {single}"
        # print(material.ljust(32), f"{stack} stacks + {single}".ljust(24), f"({amount})")
        output.append(f"{material:<32} {stacks_str:<24} ({amount})")
    return "\n".join(output)


def main() -> None:
    item = input("What item would you like the components for?\n")
    print(get_materials_pretty(item))


if __name__ == "__main__":
    main()
