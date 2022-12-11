from ..key_util import KeyUtil
from win32com.client import Dispatch


class WindowsKeyUtil(KeyUtil):
    def __init__(self):
        self.__shell = Dispatch("WScript.shell")

    def send_keys(self, keys: str):
        self.__shell.SendKeys(keys)
