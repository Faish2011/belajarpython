# import webview

# window = webview.create_window (
# title = 'Simple browser',
# html = "<h1>Hello</h1>"
# )

# webview.start ()


# import webview

# with open ('web/index.html', 'r') as file:
#     window = webview.create_window (
#         title = 'Simple browser',
#         html = file.read ()
#     )

# webview.start ()

import webview
window = webview.create_window (
    title = 'Simple browser',
    url = "https://wiki.warthunder.com/ground"
)


webview.start ()











