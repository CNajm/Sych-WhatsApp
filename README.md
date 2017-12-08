# Simple-Yet-Hackable-WhatsApp-API  
  
  
## About
This is a reversed engineered API hook for the [WhatsApp](https://www.whatsapp.com) mobile messenger made using Python3.   

## How
We use [Selenium](http://www.seleniumhq.org) to crawl and extract information from the WhatsApp-Web interface while maintaining a degree of regular human behavior. This live data and metadata can be used to create helpful bots or assistants without compromising server resources or inconveniencing any end-users, but rather improving their overall experience.  

Please submit any bugs or suggestions to the Issues tab found above.  

**Sending a message with an emoji:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.send_message("Name",":heart: Good!"))  
```
**Result:** <br>
![Image](https://raw.githubusercontent.com/VISWESWARAN1998/Simple-Yet-Hackable-WhatsApp-api/master/Screenshot%20(747).png)

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
