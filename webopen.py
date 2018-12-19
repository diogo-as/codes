import webbrowser, time

total_breaks = 3
break_count = 0
url = "http://globo.com"

print("This program started on "+time.ctime())
while (break_count < total_breaks):
    time.sleep(10)
    webbrowser.open(url)
    break_count += 1
