# PythonSDK
An SDK for interacting with the IP Street API in Python

## Usage

1. Instantiate a Client

```python
client = client.Client(apikey=apikey, api_version=api_version)
```

2. Instantiate a Query
```python
query = query.PatentData()
```

3. Add Parameters to your Query
```python
query.add_keywords('battery')
```
4. Send you Query with the Client
```python
results = client.send(query)
```
