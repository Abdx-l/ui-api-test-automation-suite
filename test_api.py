import requests
from jsonschema import validate
SCHEMA={"type":"object","required":["id","name","coverage"],"properties":{"id":{"type":"integer"},"name":{"type":"string"},"coverage":{"type":"number","exclusiveMinimum":0}}}
def create(api,name="sample"):
 session,url=api;r=session.post(url+"/policies",json={"name":name,"coverage":1000},timeout=5);assert r.status_code==201;validate(r.json(),SCHEMA);return r.json()["id"]
def test_crud(api):
 session,url=api;id=create(api);assert session.get(f"{url}/policies/{id}",timeout=5).json()["name"]=="sample";assert session.delete(f"{url}/policies/{id}",timeout=5).status_code==204;assert session.get(f"{url}/policies/{id}",timeout=5).status_code==404
def test_auth(base_url):assert requests.get(base_url+"/policies",timeout=5).status_code==401
def test_validation(api):
 session,url=api;assert session.post(url+"/policies",json={"name":"","coverage":-1},timeout=5).status_code in (400,422)
def test_pagination(api):
 session,url=api
 for i in range(3):create(api,f"page-{i}")
 first=session.get(url+"/policies?page=0&size=1",timeout=5).json();second=session.get(url+"/policies?page=1&size=1",timeout=5).json();assert len(first)==len(second)==1;assert first[0]["id"]<second[0]["id"]
def test_missing(api):
 session,url=api;assert session.get(url+"/policies/9999999",timeout=5).status_code==404
