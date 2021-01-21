import webbrowser


url="https://www.barcodelookup.com/045941410259"
def open_browser():
    webbrowser.get("chrome").open(url)



if __name__=='__main__':
    open_browser()
