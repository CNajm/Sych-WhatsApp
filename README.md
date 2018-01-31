# Sych WhatsApp

[![license](https://img.shields.io/github/license/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp)
[![GitHub last commit](https://img.shields.io/github/last-commit/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)
[![GitHub issues](https://img.shields.io/github/issues/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)

## About
This is a reverse-engineered automation library for the [WhatsApp](https://www.whatsapp.com) mobile messenger designed for ease of use and readability made using Python3.

## How
[Selenium](http://www.seleniumhq.org) is used to crawl and extract information from the WhatsApp-Web interface while maintaining a degree of regular human behavior. This live data and metadata can be used to create helpful bots or assistants without compromising server resources or inconveniencing any end-users, but rather improving their overall experience.

This implementation does **not** involve direct http calls to WhatsApp servers.

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

## Running
1. Clone `git clone https://github.com/CNajm/Sych-WhatsApp.git`
2. Navigate to `cd Sych-WhatsApp`
3. Install dependencies, make a virtualenv if you wish beforehand `pip install -r requirements.txt`
4. [Download the chrome webdriver <-- Click](https://sites.google.com/a/chromium.org/chromedriver/)
5. Extract the chromedriver to the same folder as whatsapp.py `Sych-WhatsApp/Sych`

You can now use the library core as shown in the screenshots above.

To run the bot framework which extends the core:
1. Do above steps
2. Edit `cb01.py`
3. Change the value of `group` to whatever contact/group you wish to run on.
4. Save and run with `python3 cb01.py`

## Contributions are welcome :heart:
Fork, make branch and pull request.

[Step by step beginner guide](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/)

Please submit any bugs or suggestions to the Issues tab found above.
## License
MIT
