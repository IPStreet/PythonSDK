# PythonSDK
An SDK for interacting with the IP Street API in Python

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
```
### Send you Query with the Client
```python
results = client.send(query)
```
