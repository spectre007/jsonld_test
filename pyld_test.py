import json

from pyld import jsonld

doc = {
    # "ctc:DFT": {"functionalName": "PBE", "modelID": 777, "hasExactExchange": False},
    "Alex": {
        "@type": "https://schema.org/Person",
        "name": "Alexander",
        "height": "1.80 m",
    },
}

context = {
    # "ctc": "https://raw.githubusercontent.com/spectre007/jsonld_test/master/ctc_test.jsonld",
    "Person": "https://schema.org/Person"
}

compacted = jsonld.compact(doc, context)

print(json.dumps(compacted, indent=2))

flattened = jsonld.flatten(doc)
print("Flattened:\n", flattened)
