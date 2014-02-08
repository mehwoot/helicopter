from ctypes import windll
import win32api, win32con

dc= windll.user32.GetDC(0)
def getpixel(x,y):
    pix = windll.gdi32.GetPixel(dc,x,y)
    return (pix >> 16, (pix % (1 << 16)) >> 8, pix % (1 << 8))


def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,x,y,0,0)
click(10,10)

print getpixel(1920 + 850,403)
