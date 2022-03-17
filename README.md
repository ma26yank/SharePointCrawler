

# Microsoft SharePoint Crawler;  [![GitHub license](https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square)](https://github.com/your/your-project/blob/master/LICENSE)
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

## Versioning

1.0.0-alpha; This is the initial version and can be modified/enhanced based on usage requirements. Please advise if there is any enhancement I can make for future releases.
