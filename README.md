<img src="./images/logo.sample.png" alt="Logo of the project" align="right">

# Microsoft SharePoint Crawler; [![Build Status](https://img.shields.io/travis/npm/npm/latest.svg?style=flat-square)](https://travis-ci.org/npm/npm) [![npm](https://img.shields.io/npm/v/npm.svg?style=flat-square)](https://www.npmjs.com/package/npm) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com) [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
> A Web crawler to find broken links in your SharePoint

while working for a solution to validate if the links in Microsoft SharePoint 2016 are missing or broken, I came up with this idea to navigate and check if all the hyperlinks are correct and/or not broken (404). This solution works in the same direction to achieve this objective.

## Installing / Getting started

Before you implement it anywhere, below are the package details I have used and their basic responsiblities in the project. 
## Developing

### Built With
```python
import requests #v2.27.1
from bs4 import BeautifulSoup #v4.10.0
import pandas as pd #v1.4.1
import validators #v0.18.2
import logging #in-built
logging.basicConfig(level=logging.DEBUG)
from urllib.parse import urlsplit #v1.26.8
from requests_ntlm import HttpNtlmAuth #v1.1.0

```

### Prerequisites
What is needed to set up the dev environment. For instance, global dependencies or any other tools. include download links.


### Setting up Dev

Here's a brief intro about what a developer must do in order to start developing
the project further:

```shell
git clone https://github.com/your/your-project.git
cd your-project/
packagemanager install
```
## Versioning

1.0.0-alpha; This is the initial version and can be modified/enhanced based on usage requirements. Please advise if there is any enhancement I can make for future releases.
