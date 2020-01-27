# Sych WhatsApp

[![license](https://img.shields.io/github/license/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)
[![GitHub repo size in bytes](https://img.shields.io/github/repo-size/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp)
[![GitHub last commit](https://img.shields.io/github/last-commit/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)
[![GitHub issues](https://img.shields.io/github/issues/CNajm/SYCH-WhatsApp.svg)](https://github.com/CNajm/SYCH-WhatsApp/)

## About
Sych is a python library for automating [WhatsApp web](https://www.whatsapp.com).

**note: this codebase is outdated as of 2020**
last actual commit may 15, 2018

## How
[Selenium.](http://www.seleniumhq.org)

This implementation **does not** involve direct calls to WhatsApp servers, making it safer to use than those that do.

## Examples
The following examples call the library core directly, see [cb01.py](https://github.com/CNajm/Sych-WhatsApp/blob/023b99fc5539428a4b7130d6061baeeb8dd2aed3/Sych/cb01.py#L61) for a chat-bot example.

**Sending a message with an emoji:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
whatsapp.send_message("Recipient", ":heart: Good!")  
```
**Result:** <br>
![Image](https://raw.githubusercontent.com/CNajm/SYCH-WhatsApp/master/Screenshot%20(747).png)

**Getting a contact's status message**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.get_status("Name"))
```

**Getting a contact's last seen datetime**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
print(whatsapp.get_last_seen("Name"))
```

**Getting the number of members in a group:**

```python
from whatsapp import WhatsApp
whatsapp = WhatsApp(10)
result = whatsapp.participants_for_group("group")
```

## Running
1. Clone `git clone https://github.com/CNajm/Sych-WhatsApp.git`
2. Navigate to `cd Sych-WhatsApp`
3. Install dependencies `pip install -r requirements.txt`
4. [Download the chrome webdriver](https://sites.google.com/a/chromium.org/chromedriver/)
5. Extract the chromedriver to `Sych-WhatsApp/Sych`

You can now use the library core as shown in the above screenshots.

To run the bot framework:
1. Perform above steps
2. Edit `cb01.py`: Change the value of `group` to whatever contact/group you wish to listen on.
3. Run `python3 cb01.py`

### Contributions
Branch your changes and pull request.
([Step by step guide if this is new to you](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/))

Do submit bugs and suggestions to the [Issues tab](https://github.com/CNajm/Sych-WhatsApp/issues), 1 issue = 1 cookie.
