#!/usr/bin/env python

# import os
import requests
from bs4 import BeautifulSoup
import json
import time
from random import uniform

# global variables
project_details = []
lines_to_write = []

# Get the update list of projects merged in the repo


def get_project_list():

    projects = requests.get(
        "https://github.com/chavarera/\
        python-mini-projects/tree/master/projects"
    )
    soup = BeautifulSoup(projects.content, "lxml")
    container = soup.find("div", attrs={"class": "js-details-container Details"})
    # print(len(container))
    global project_names
    project_names = [
        x.text.strip()
        for x in container.find_all("div", attrs={"role": "rowheader"})[1:]
    ]
    project_names.remove("WishList App Using Django")


# Alternatively we can get this list from our folder as well
# but that is error prone
# project_names = os.listdir("../../python-mini-projects/projects")

# Get contribution details of each project
def get_contribution_details():
    i = 1
    for project_name in project_names:

        try:

            project_path = "projects/" + "%20".join(project_name.split())
            api_url = f"https://api.github.com/repos/chavarera/\
            python-mini-projects/commits?path={project_path}"

            r = requests.get(api_url)
            d = json.loads(r.text)

            project_url = f"https://github.com/chavarera/\
            python-mini-projects/tree/master/{project_path}"
            author_name = d[len(d) - 1]["commit"]["author"]["name"]
            author_github = d[len(d) - 1]["author"]["html_url"]
            # project_detail={'name': project_name, 'url': project_url,
            # 'author': author_name, 'author_github': author_github }
            # project_details.append(project_detail)
            project_details = " | ".join(
                [
                    f"{i}",
                    f"[{project_name}]({project_url})",
                    f"[{author_name}]({author_github})\n",
                ]
            )
            lines_to_write.append(project_details)
        except Exception as e:
            print(f"Failed update for : {project_name}", e, sep="\n")
        i += 1

        # giving a random delay for api call
        time.sleep(uniform(0, 2))


# Write the contributions in readme
def update_readme():
    with open("contributions.md", "w") as fw:
        fw.write(
            "Thanks goes to these wonderful people\n\
            Sr no | Project Name | Author\n--- | --- | ---\n"
        )
        fw.writelines(lines_to_write)


def main():
    get_project_list()
    get_contribution_details()
    update_readme()


if __name__ == "__main__":
    main()
