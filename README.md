# SYCH WhatsApp

[![license](https://img.shields.io/github/license/CNajm/Simple-Yet-Hackable-WhatsApp-api.svg)](https://github.com/CNajm/Simple-Yet-Hackable-WhatsApp-api/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/CNajm/Simple-Yet-Hackable-WhatsApp-api.svg)](https://github.com/CNajm/Simple-Yet-Hackable-WhatsApp-api)
[![GitHub last commit](https://img.shields.io/github/last-commit/CNajm/Simple-Yet-Hackable-WhatsApp-api.svg)](https://github.com/CNajm/Simple-Yet-Hackable-WhatsApp-api/)
[![GitHub issues](https://img.shields.io/github/issues/CNajm/Simple-Yet-Hackable-WhatsApp-api.svg)](https://github.com/CNajm/Simple-Yet-Hackable-WhatsApp-api/)

## About
This is a reverse-engineered hook for the [WhatsApp](https://www.whatsapp.com) mobile messenger made using Python3.

## How
We use [Selenium](http://www.seleniumhq.org) to crawl and extract information from the WhatsApp-Web interface while maintaining a degree of regular human behavior. This live data and metadata can be used to create helpful bots or assistants without compromising server resources or inconveniencing any end-users, but rather improving their overall experience.  

Please submit any bugs or suggestions to the Issues tab found above.  

## Examples
The following use the library core directly, see source for a chatbot implementation example.

**Sending a message with an emoji:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
whatsapp.send_message("Recipient", ":heart: Good!")  
```
**Result:** <br>
![Image](https://raw.githubusercontent.com/CNajm/Simple-Yet-Hackable-WhatsApp-api/master/Screenshot%20(747).png)

**Getting the status message of a person:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.get_status("Name"))
```

**Getting last seen of a person:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.get_last_seen("Name"))
```

**Getting the no# of participants in the group:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
result = whatsapp.participants_for_group("group")
```

## License
Original code licensed to [Visweswaran Nagasivam](https://github.com/VISWESWARAN1998/Simple-Yet-Hackable-WhatsApp-api) under the Apache 2.0 license. See ORIGINALLICENSE.

MIT License
