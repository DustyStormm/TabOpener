import webbrowser
import sys


def openBrowser(url):
    chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open_new(url)


print("Enter your URLs | Press Ctrl + Z and enter after")
contents = []
while True:
    try:
        line = input()
    except EOFError:
        break
    contents.append(line)

for item in contents:
    string = ""
    openBrowser(string.join(item))
