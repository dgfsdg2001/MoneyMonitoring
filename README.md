
# Example unittest org
python.exe -m unittest discover -s "account_book/test" -p "test_*.py"

# Checkcode
pycodestyle --show-soruce account_book

```
-------------------------------
| toolbar                     |
------------------------------|
| layout Top                  |
-------------------------------
| layout left  | layout right |
|              |              |
-------------------------------
```

# Jupyter notebook
```powershell
# Choice the preferred version of Python
Set-Variable -Name "python-dir" -Value "${HOME}\AppData\Local\Programs\Python\Python38"

# Upgrade pip, install virtulenv, and create a virtual environment called `venv`.
Set-Variable -Name "command" -Value "${python-dir}\python.exe -m pip install --upgrade pip; ${python-dir}\Scripts\pip3.8.exe install virtualenv; ${python-dir}\Scripts\virtualenv.exe --python ${python-dir}\python.exe venv;"
powershell.exe -Command ${command}
```
 - Activate the venv
```powershell
# Activate the venv
.\venv\Scripts\activate.ps1
```
 - (Optional) Install and run [jupyter notebook](https://github.com/jupyter/notebook/blob/master/README.md).
```powershell
pip install notebook
jupyter notebook
# After run the above command, copy the URL shown on the commnad prompt and open it in a web browser.
#
#    To access the notebook, open this file in a browser:
#        file:///C:/Users/<User>/AppData/Roaming/jupyter/runtime/nbserver-22204-open.html
#    Or copy and paste one of these URLs:
#        http://localhost:8888/?token=79e5bb30e2c5da887ceac917873b62337f1c900eb260f020
#     or http://127.0.0.1:8888/?token=79e5bb30e2c5da887ceac917873b62337f1c900eb260f020
#
```