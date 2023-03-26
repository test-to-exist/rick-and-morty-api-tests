character_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "status": {
            "type": "string"
        },
        "species": {
            "type": "string"
        },
        "type": {
            "type": "string"
        },
        "gender": {
            "type": "string"
        },
        "origin": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                }
            },
            "required": [
                "name",
                "url"
            ]
        },
        "location": {
            "type": "object",
            "properties": {
                "name": {
                    "type": "string"
                },
                "url": {
                    "type": "string"
                }
            },
            "required": [
                "name",
                "url"
            ]
        },
        "image": {
            "type": "string"
        },
        "episode": {
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
        "status",
        "species",
        "type",
        "gender",
        "origin",
        "location",
        "image",
        "episode",
        "url",
        "created"
    ]
}
