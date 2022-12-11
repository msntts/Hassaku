from platform import system
from .screen.screen_util import ScreenUtil
from .screen.impl.windows_screen_util import WindowsScreenUtil
from .keys.key_util import KeyUtil
from .keys.impl.windows_key_util import WindowsKeyUtil


class PlatformUtil:
    def __init__(self, base_dir: str):
        os_type = system()

        if os_type == "Windows":
            self.__screen: ScreenUtil = WindowsScreenUtil(base_dir)
            self.__keys: KeyUtil = WindowsKeyUtil()
        elif os_type == "Darwin":
            raise NotImplementedError()
        elif os_type == "Linux":
            raise NotImplementedError()

    def activate_window(self, title: str) -> bool:
        """指定したタイトルのウィンドウをアクティブにする

        Args:
            title (str): アクティブにするウィンドウのタイトル

        Returns:
            bool: 成功時 True、失敗時 False
        """
        return self.__screen.activate_window(title)

    def capture_window(self, title: str) -> str:
        """指定したタイトルのウィンドウをキャプチャし、ファイルに保存する

        Args:
            title (str): キャプチャするウィンドウのタイトル

        Returns:
            str: キャプチャ成功時: キャプチャ画像パス、失敗時: None
        """
        return self.__screen.capture_window(title)

    def send_keys(self, keys: str):
        """キーを送信する。keysの仕様はmicrosoftのSendKeysに準拠。
        https://learn.microsoft.com/ja-jp/dotnet/api/system.windows.forms.sendkeys?view=windowsdesktop-7.0

        Args:
            keys (str): 入力するキー
        """
        return self.__keys.send_keys(keys)
