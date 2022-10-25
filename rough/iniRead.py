from configparser import ConfigParser

c = ConfigParser()
c.read("../ConfigurationData/config.ini")
b = c.get("base url", "URL")
print(b)

d = c.get("locators", "username_ID")
print(d)


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("../ConfigurationData/config.ini")
    return config.get(section, Key)

e = ConfigReader("locators", "password_ID")
print(e)
