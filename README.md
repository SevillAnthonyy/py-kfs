# py-kfs

Prereq: <br/>
1. Download and install the latest python version.<br/>
https://www.python.org/downloads/<br/><br/>

2. Install the following using the command line:<br/>
pip install selenium<br/>
pip install pyautogui<br/><br/>

3. Create the following folder under your C:\drive <br/>
C:\MyPythonScripts<br/><br/>

4. Add the scripts to your computer<br/>
Go to Control panel > System > Advance System Settings > Advance Tab > Environment Variables.<br/>
Under System Variables find "Path" and click on edit.<br/>
Add the following directory. "C:\MyPythonScripts"<br/><br/>

5. Download drivers and put it under "C:\MyPythonScripts"<br/>
- Firefox https://github.com/mozilla/geckodriver/releases<br/>
- Chrome https://chromedriver.chromium.org/downloads<br/>
	- Important Note: To run using chrome, both software (Chrome, Chromium) version should be the same.<br/><br/>

Developer Notes:<br/><br/>

Use IDLE<br/>
If you run your code and an error occurs in your imports. There are 2 pythons installed in in your computer.<br/>
To fix this do the following:<br/>
- install imports inside the application's directory.<br/>
- To know the path run the following commands in your IDLE:<br/>
>import sys <br/>
>for path in sys.path: print(path)<br/>
- Copy the directory and from there "pip install packagename" again.<br/>