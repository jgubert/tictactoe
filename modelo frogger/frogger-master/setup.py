from cx_Freeze import setup, Executable

setup(
    name="frogger EXECUTABLE",
    version = "1.0.0",
    description = ".py to .exe",
    executables = [Executable("frogger.py")])
