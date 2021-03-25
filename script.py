import os
output_text = '<li><a href="{}">{}</a></li>\n'
container = "<ul>"

for elem in os.listdir():
  container += output_text.format(elem, elem.split(".")[0])

container += "</ul>"
with open("text.html", "w") as file:
  file.write(container)

