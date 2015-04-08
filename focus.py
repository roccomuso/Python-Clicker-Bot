import win32com.client
import win32gui

current = win32gui.GetForegroundWindow()

shell = win32com.client.Dispatch("WScript.Shell")

