import pygetwindow as gw
import win32gui
import win32con
import ctypes

def list_windows():
    return gw.getAllWindows()

def pin_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        hwnd = window._hWnd
        win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"Window '{window_title}' pinned successfully.")
    except IndexError:
        print(f"Window '{window_title}' not found.")
    except Exception as e:
        print(f"Error pinning window '{window_title}': {str(e)}")

def unpin_window(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        hwnd = window._hWnd
        win32gui.SetWindowPos(hwnd, win32con.HWND_NOTOPMOST, 0, 0, 0, 0,
                              win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
        print(f"Window '{window_title}' unpinned successfully.")
    except IndexError:
        print(f"Window '{window_title}' not found.")
    except Exception as e:
        print(f"Error unpinning window '{window_title}': {str(e)}")

def is_window_pinned(window_title):
    try:
        window = gw.getWindowsWithTitle(window_title)[0]
        hwnd = window._hWnd
        style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
        return bool(style & win32con.WS_EX_TOPMOST)
    except IndexError:
        print(f"Window '{window_title}' not found.")
        return False
    except Exception as e:
        print(f"Error checking if window '{window_title}' is pinned: {str(e)}")
        return False

def keep_window_on_top(window_title):
    while True:
        try:
            window = gw.getWindowsWithTitle(window_title)[0]
            hwnd = window._hWnd
            if is_window_pinned(window_title):
                ctypes.windll.user32.BringWindowToTop(hwnd)
        except IndexError:
            print(f"Window '{window_title}' not found. Stopping keep_window_on_top.")
            break
        except Exception as e:
            print(f"Error in keep_window_on_top for '{window_title}': {str(e)}")
            break