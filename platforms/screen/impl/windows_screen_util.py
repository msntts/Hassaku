from ..screen_util import ScreenUtil
from win32gui import FindWindow, GetWindowRect, SetForegroundWindow
from ctypes import wintypes, windll, byref, sizeof
from PIL import ImageGrab
from PIL.Image import Image
from time import sleep


class WindowsScreenUtil(ScreenUtil):
    def __init__(self, dir: str):
        super().__init__(dir)

    def activate_window(self, title: str) -> bool:
        hwnd = FindWindow(None, title)

        if hwnd > 0:
            try:
                SetForegroundWindow(hwnd)
                return True
            except:
                return False
        else:
            return False

    def capture_window(self, title: str) -> str:
        hwnd = FindWindow(None, title)

        if hwnd > 0:
            # SetActiveWindow()を呼んですぐActiveにならないのでﾁｮｯﾄ待つ
            SetForegroundWindow(hwnd)
            sleep(0.5)

            # ウィンドウの枠のサイズでキャプチャ範囲がずれるので補正
            get_wnd_attr_func = windll.dwmapi.DwmGetWindowAttribute
            rect = wintypes.RECT()
            DWMWA_EXTENDED_FRAME_BOUNDS = 9
            get_wnd_attr_func(
                wintypes.HWND(hwnd),
                wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
                byref(rect),
                sizeof(rect),
            )

            image: Image = ImageGrab.grab(
                (rect.left, rect.top, rect.right, rect.bottom)
            )

            img_path: str = self.create_image_path()
            image.save(img_path)

            return img_path
        else:
            return None
