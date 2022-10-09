docfile = open("README.md", "w")

reponame = input("Enter the name of the repository: ")

title = input("Enter the title of the document(nothing to use reponame): ")
description = input("Enter the description of the document: ")

docfile.write("<center>\n\n")
docfile.write("# " + title if title == "" else reponame + "\n")
docfile.write(description + "\n\n")

# Badges
docfile.write(f'<img src="https://img.shields.io/github/languages/top/josefilho/{reponame}?color=%237159c1&style=for-the-badge" />\n')
docfile.write(f'<img src="https://img.shields.io/github/repo-size/josefilho/{reponame}?color=%237159c1&style=for-the-badge" />\n')
docfile.write(f'<img src="https://img.shields.io/badge/Made%20By-NullByte-%237159c1?style=for-the-badge" />\n\n')

choice = True
while choice:
  topicname = input("Enter the name of the topic: ")
  docfile.write(f"## {topicname}\n")
  topicdescription = input(f"Enter the description of the {topicname}: ")
  while True:
    subchoice = input("Do you want to add a subtopic? (y/n): ")
    if subchoice == "y" or subchoice == "Y" or subchoice == '':
      subtopicname = input("Enter the name of the subtopic: ")
      docfile.write(f"### {subtopicname}\n")
      subtopicdescription = input(f"Enter the text of the {subtopicname}: ")
      docfile.write(f"{subtopicdescription}\n\n")
    else:
      break
  choice = input("Do you want to add another topic? (y/n): ")
  if choice == "y":
    choice = True
  else:
    choice = False


docfile.write("</center>\n")
docfile.close()
