episode_schema = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "integer"
    },
    "name": {
      "type": "string"
    },
    "air_date": {
      "type": "string"
    },
    "episode": {
      "type": "string"
    },
    "characters": {
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
    "air_date",
    "episode",
    "characters",
    "url",
    "created"
  ]
}

