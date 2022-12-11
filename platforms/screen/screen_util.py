from abc import ABC
from os.path import join
from datetime import datetime


class ScreenUtil(ABC):
    def __init__(self, base_dir: str):
        """コンストラクタ

        Args:
            base_dir (str): キャプチャ画像保存先ディレクトリ
        """
        self.__base_dir = base_dir

    def activate_window(self, title: str) -> bool:
        """指定したタイトルのウィンドウをアクティブにする

        Args:
            title (str): アクティブにするウィンドウのタイトル

        Returns:
            bool: 成功時 True、失敗時 False
        """
        pass

    def capture_window(self, title: str) -> str:
        """指定したタイトルのウィンドウをキャプチャし、ファイルに保存する

        Args:
            title (str): キャプチャするウィンドウのタイトル

        Returns:
            str: キャプチャ成功時: キャプチャ画像パス、失敗時: None
        """
        pass

    def create_image_path(self) -> str:
        """画像パスを生成する。

        Returns:
            str: 画像パス。{self.__base_dir}+yyyymmdd_hhMMss.pngを出力
        """
        return join(self.__base_dir, datetime.now().strftime("%Y%m%d_%H%M%S") + ".png")
