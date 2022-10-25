from configparser import ConfigParser


def ConfigReader(section, Key):
    config = ConfigParser()
    config.read("../ConfigurationData/config.ini")
    return config.get(section, Key)