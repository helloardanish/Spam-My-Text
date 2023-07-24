from cx_Freeze import setup, Executable

# Specify your application's main script or entry point here
main_script = "Main.py"

# Other options for cx_Freeze go here
# ...

# Create the executable
executables = [Executable(main_script)]

# Build the setup
setup(
    name="Type It Again",
    version="1.0",
    description="A software to type same thing again and again wherever you want.",
    executables=executables,
    # Add other options if necessary
)


'''

http://www.jrsoftware.org/isinfo.php

pip install pyinstaller

pyinstaller --onefile your_script.py

https://nsis.sourceforge.io/Download

'''