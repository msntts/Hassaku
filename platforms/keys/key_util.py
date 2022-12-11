from abc import ABC


class KeyUtil(ABC):
    def send_keys(self, keys: str):
        """キーを送信する。keysの仕様はmicrosoftのSendKeysに準拠。
        https://learn.microsoft.com/ja-jp/dotnet/api/system.windows.forms.sendkeys?view=windowsdesktop-7.0

        Args:
            keys (str): 入力するキー
        """
        pass
