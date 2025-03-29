# Test Task

The microservice that displays information using an address on Tron Web

### Run

Configure `.env` file using template. Run `main.py`.

If you have problems with python not seeing the `src` module,
then run `python -m src.main` from the root directory.

### Endpoints

---
#### GET `/v1/address/`
Request Parameters:
+ **offset** `[int]` - starting point for the result
+ **limit** `[int]` - the maximum number of addresses to return

Response Example:
```json
[
  {
    "id": 0,
    "address": "string",
    "balance": "string",
    "bandwidth": 0,
    "energy": 0,
    "timestamp": "2025-03-28T23:31:37.239045"
  }
]
```
---
#### POST `/v1/address/`
Request Body:
```json
{
  "address": "string"
}
```

Response Example:
```json
{
  "id": 0,
  "address": "string",
  "balance": "string",
  "bandwidth": 0,
  "energy": 0,
  "timestamp": "2025-03-28T23:31:37.239045"
}
```

### Tests

You can run tests using the command `pytest -v`
