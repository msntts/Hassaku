from tempfile import TemporaryDirectory
from platforms.platform_util import PlatformUtil
from os import getcwd
from os.path import join, isdir
from glob import glob
from re import search
from cv2 import imread, matchTemplate, TM_CCOEFF_NORMED
from numpy import where


class Hassaku:
    __ALLOW_IMG_EXT_PTTN = "\\.(png|bmp|PNG|BMP)"

    def __init__(self, base_dir: str = ""):
        """コンストラクタ

        Args:
            base_dir (str, optional): キャプチャ画像を保存するディレクトリ。省略した場合はテンポラリディレクトリにキャプチャ画像を保存する。
        """
        self.__use_tmp_dir = base_dir == ""

        if self.__use_tmp_dir:
            self.__base_dir = TemporaryDirectory()
            self.__plt_utl = PlatformUtil(self.__base_dir.name)
        else:
            self.__base_dir = base_dir

        self.__res_dr = join(getcwd(), "resources")

    def __del__(self):
        if self.__use_tmp_dir:
            del self.__base_dir

    def send_keys_to_window(self, keys: str, title: str = "") -> bool:
        """ウィンドウにキーを送信する

        Args:
            keys (str): 送信するキー
            title (str, optional): 設定があった場合、タイトルと一致するウィンドウをアクティブにしてキーを送信。
                                   指定がない場合は、現在のアクティブウィンドウにキーを送信。

        Returns:
            bool: 成功時 True、失敗時 False
        """
        succeeded: bool = True

        if title != "":
            succeeded = self.__plt_utl.activate_window(title)

        # アクティブ化できた
        if succeeded:
            try:
                self.__plt_utl.send_keys(keys)
            except:
                succeeded = False

        return succeeded

    def find_image_from_window(
        self, window_title: str, img_name: str, threshold=0.9
    ) -> list:
        """指定したタイトルのウィンドウから画像一致する座標を取得する。

        Args:
            window_title (str): 対象画面のタイトル
            img_name (str): 検索する画像の名前。resources直下のファイル(拡張子なし)orディレクトリ名。
                            ディレクトリ名を指定した場合、配下にある全png/bmpファイルを使って検索する。
            threshold (float, optional): 相似率の下限。省略した場合は0.9を使用。非可逆圧縮のノイズを無視したりするのに使用。

        Returns:
            list: 画像一致した座標(tuple)のリスト。tupleは(左上x座標, 左上y座標, 右下x座標, 右下y座標)
        """
        capture_path = self.__plt_utl.capture_window(window_title)

        if capture_path is not None:
            capture_img = imread(capture_path)
            rects = []

            for finding_img_path in self.__get_finding_images_path(img_name):
                finding_img = imread(finding_img_path)

                matches = matchTemplate(capture_img, finding_img, TM_CCOEFF_NORMED)

                for (y, x) in zip(*where(matches >= threshold)):
                    (h, w, _) = finding_img.shape
                    rects.append((x, y, x + w, y + h))

                return rects
        else:
            return []

    def __get_finding_images_path(self, img_name: str) -> list:
        # resource直下にあるファイルの場合
        for path in glob(join(self.__res_dr, "**"), recursive=False):
            print(path)
            if not isdir(path) and search(img_name + self.__ALLOW_IMG_EXT_PTTN, path):
                # 1つしか見つからないはず
                return [path]

        images_path = []
        # ここに来たということはファイルではなかった
        # フォルダの場合、img_nameフォルダ以下にある全ての画像パスを返す
        for path in glob(join(self.__res_dr, img_name, "**"), recursive=True):
            if search(self.__ALLOW_IMG_EXT_PTTN, path):
                images_path.append(path)

        return images_path
