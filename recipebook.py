"""
Here, I've provided an example set of recipe data, some RefinedStorage 
storage parts. The entires within this recipe book 
follows a fairly simple format:

```py
resultant_product:
    { ingredient_1: amount_1,
      ingredient_2, amount_2,
      ...
    }
```

The amount is always in terms of a single output product, e.g. 1 oak log 
produces 4 planks, therefore a plank requires 0.25 logs
"""
from numbers import Number


recipebook: dict[str, dict[str, Number]] = {
    "silicon": {
        "quartz": 1,
    },
    "quartz enriched iron": {
        "iron ingot": 0.75,
        "quartz": 0.25,
    },
    "basic processor": {
        "processor binding": 1,
        "silicon": 1,
        "redstone": 1,
        "iron ingot": 1,
    },
    "improved processor": {
        "processor binding": 1,
        "silicon": 1,
        "redstone": 1,
        "gold ingot": 1,
    },
    "advanced processor": {
        "processor binding": 1,
        "silicon": 1,
        "redstone": 1,
        "diamond": 1,
    },
    "1k storage part": {
        "redstone dust": 1,
        "glass": 3,
        "silicon": 4,
        "quartz enriched iron": 1,
    },
    "4k storage part": {
        "redstone dust": 1,
        "1k storage part": 3,
        "basic processor": 4,
        "quartz enriched iron": 1,
    },
    "16k storage part": {
        "redstone dust": 1,
        "4k storage part": 3,
        "improved processor": 4,
        "quartz enriched iron": 1,
    },
    "64k storage part": {
        "redstone dust": 1,
        "16k storage part": 3,
        "advanced processor": 4,
        "quartz enriched iron": 1,
    },
    "256k storage part": {
        "redstone dust": 1,
        "64k storage part": 3,
        "advanced processor": 4,
        "quartz enriched iron": 1,
    },
}
