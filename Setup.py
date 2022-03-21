import sys
from cx_Freeze import setup, Executable


# Dependencies are automatically detected, but it might need fine tuning.
# "packages": ["os"] is used as example only
build_exe_options = {"packages": ["os","pyautogui","datetime","zipfile","PyQt5","json","tkinter","shutil","reportlab","PIL","subprocess"]}

# base="Win32GUI" should be used only for Windows GUI app
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="PyRelator",
    version="1.0",
    description="PyRelator",
    options={"build_exe": build_exe_options},
    executables=[Executable("PyRelator.py", base=base, icon=r"C:\Users\gabriel.azevedo\Desktop\PyRelator\Images\Icon.ico")],
)
