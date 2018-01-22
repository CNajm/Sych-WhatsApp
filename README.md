# Sych WhatsApp

[![license](https://img.shields.io/github/license/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp)
[![GitHub last commit](https://img.shields.io/github/last-commit/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)
[![GitHub issues](https://img.shields.io/github/issues/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)

## About
This is a reverse-engineered hook for the [WhatsApp](https://www.whatsapp.com) mobile messenger made using Python3.

## How
We use [Selenium](http://www.seleniumhq.org) to crawl and extract information from the WhatsApp-Web interface while maintaining a degree of regular human behavior. This live data and metadata can be used to create helpful bots or assistants without compromising server resources or inconveniencing any end-users, but rather improving their overall experience.  

Please submit any bugs or suggestions to the Issues tab found above.  

## Examples
The following use the library core directly, see source for a chat bot implementation example.

**Sending a message with an emoji:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
whatsapp.send_message("Recipient", ":heart: Good!")  
```
**Result:** <br>
![Image](https://raw.githubusercontent.com/CNajm/SYCH-WhatsApp/master/Screenshot%20(747).png)

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
MIT
