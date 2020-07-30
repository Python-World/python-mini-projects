#!/usr/bin/env python
import os

# Using os module to change the file/folder's name
projects_old = os.listdir("../projects")
projects_new = []

# renaming each projects as per repo standard guidelines
for project in projects_old:
    name_old = project.lower()
    name = ""
    n = 0
    for c in name_old:
        if ord(c) in range(97, 123) or c == ".":
            name += c
            n = 1
        elif n == 1:
            name += " "
            n += 1
        else:
            pass

    name_new = ""
    for word in name.split():
        if word in [
            "write",
            "create",
            "script",
            "a",
        ]:  # the list can be configured as per future requirement
            pass
        else:
            name_new = " ".join([f"{name_new}", f"{word}"]).strip()

    if name_new.split()[0] in [
        "to",
        " ",
    ]:  # this list will provide extra truncation at statring word of name
        name_new = " ".join(name_new.split()[1:]).strip()

    projects_new.append(name_new)

for i in range(len(projects_new)):
    old_name = f"../projects/{projects_old[i]}"
    new_name = f"../projects/{projects_new[i]}"
    os.rename(old_name, new_name)
