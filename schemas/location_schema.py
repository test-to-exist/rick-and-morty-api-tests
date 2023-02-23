location_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "dimension": {
            "type": "string"
        },
        "residents": {
            "type": "array",
            "items": [
                {
                    "type": "string"
                }
            ]
        },
        "url": {
            "type": "string"
        },
        "created": {
            "type": "string"
        }
    },
    "required": [
        "id",
        "name",
        "type",
        "dimension",
        "residents",
        "url",
        "created"
    ]
}

