#!/usr/bin/python
import sys
import re
import os

first_capital = re.compile('^[a-z]')
extensions = [".jpg", ".gif", ".png", ".JPG", ".GIF", ".PNG", ".txt", ".ico"]
prefixes = ["Category:", "Category_talk:", "Portal:", "Wikipedia:",
            "Wikipedia_talk:", "Media:", "Special:", "Talk:", "User:",
            "User_talk:", "Project:", "Project_talk:", "File:", "File_talk:",
            "MediaWiki:", "MediaWiki_talk:", "Template:", "Template_talk:",
            "Help:", "Help_talk:"]
boilerplate_articles = ['404_error/' , 'Main_Page',  'Hypertext_Transfer_Protocol', 'Search']

for line in sys.stdin:
    line = line.strip()
    page = line.split()

    # select only en pages
    if (page[0]=="en"):

        # filter out special pages
        pref_found = False
        for prefix in prefixes:
            if (prefix == page[1][:len(prefix)]):
                pref_found = True
                break
        if not pref_found:

            # check if first letter not lowercase
            if not first_capital.match(page[1]):

                # remove files with extensions
                if page[1][-4:] not in extensions:

                    # remove boilerplate_articles
                    if page[1] not in boilerplate_articles:
                        filename = os.environ["mapreduce_map_input_file"]
                        page[1] = filename[-18:-10]+page[1]
                        print('{}\t{}'.format(page[1], page[2]))
