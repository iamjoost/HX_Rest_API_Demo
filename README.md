# HyperFlex REST API Examples

HyperFlex REST APIs are fun, but where to begin.

Here are some start example scripts.


## Getting Started

Download the scripts. Install the required pips and try it.


### Installing

The files should be in one directory. hxdef.py has some functions defined in it.
Install the required files with:

```
pip install -r requirements.txt


python ListDatastore.py -h
usage: ListDataStore.py [-h] [--hxip HXIP] [--hxpasswd HXPASSWD] [--hxuser HXUSER]

HyperFlex List Datastores.

optional arguments:
  -h, --help           show this help message and exit
  --hxip HXIP          HyperFlex ip
  --hxpasswd HXPASSWD  HyperFlex Cluster Password
  --hxuser HXUSER      hx user name
```


## hxdef.py

In this file there are some functions that all scripts are using. You can put all scripts together if you like,
but I liked it this way.

### Scripts

GetAccessToken.py will get you the access token for the python scripts.

ListDataStore.py will show all datastores on a HyperFlex cluster

CreateDatastore.py will create a datastore on a HyperFlex cluster

DeleteDatastore.py will delete a datastore on a HyperFlex cluster.


## Authors

* **Joost van der Made** - [IAmJoost.com](https://iamjoost.com)