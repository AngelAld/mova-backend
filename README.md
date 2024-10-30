# Prompt

tengo 3 apis que devuelven los siguientes datos:

```json
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100&search=string",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100&search=string",
  "results": [
    {
      "id": 0,
      "nombre": "string"
    }
  ]
}

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100&search=string",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100&search=string",
  "results": [
    {
      "id": 0,
      "nombre": "string",
      "nombre_completo": "string"
    }
  ]
}

{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100&search=string",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100&search=string",
  "results": [
    {
      "id": 0,
      "nombre": "string",
      "nombre_completo": "string"
    }
  ]
}
```
