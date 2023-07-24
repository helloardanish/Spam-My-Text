from cx_Freeze import setup, Executable

#exe = Executable(script='Main.py',icon='icon.ico')
exe = Executable(script='Main.py')

setup(
    name="Spam My Text",
    version="1.0",
    description="Spam your message any times you want. Oops currently only 100 times.",
    executables=[exe]
)

'''

For macOS

python3 setup.py bdist_mac

python3 setup.py build > also


For Windows

python3 setup.py bdist_msi

'''