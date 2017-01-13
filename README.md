# A Python Wrapper for the IP Street API
IP Street is a patent data and analytics API service.  It enables users to integrate patent data and analytical algorithms into their applications without the need to build or manage the significant infrastrucutre required to do so well.
## Usage
### Install
```python
pip install IPStreet
```
### Instantiate a Client
```python
client = client.Client(apikey=apikey, api_version=api_version)
```
### Instantiate a Query
```python
query = query.PatentData()
```
### Add Parameters to your Query
```python
query.add_keywords('battery')
query.add_owner('Tesla Motors')
```
### Send your Query with the Client
```python
results = client.send(query)
```

## Best Practices
Break large queries into smaller queries and write the to disk as they complete. If you query response is too large, your local device will run out of memory causing a parsing error.  The definition of "large queries" in this context is dependant on you local machines memory availability.
