import webbrowser

# webbrowser.open("https://www.python.org/", new=1)
# help(webbrowser)
# https://docs.python.org/3.12/library/webbrowser.html

for i in range(10):
    print(1, 2, 3, 4, 5, 6, 7, 8, 9, sep=';', end='\n')

safari = webbrowser.get(using='safari')
safari.open_new("https://www.python.org/")
