"""Translate GUI terms in helpfiles to German 

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/nvhelp_de
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import glob

REPLACE = {
    'Allee': 'Alle',
    'context menu': 'Kontextmenü',
    ' menu': '-Menü',
    'Tree view': 'Baumansicht',
    'tree view': 'Baumansicht',
    '``Ctrl``':'``Strg``',
    '``Shift``':'``Umschalttaste``',
    }


def process_file(sourcePath, targetPath):
    with open(sourcePath, 'r', encoding='utf-8') as f:
        page = f.read()
    for term in sortedTranslations:
        if term in page:
            page = page.replace(term, translations[term])
    for r in REPLACE:
        page = page.replace(r, REPLACE[r])
    with open(targetPath, 'w', encoding='utf-8') as f:
        f.write(page)


def read_translations(filePath):
    with open(filePath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    msgid = ''
    for line in lines:
        if line.startswith('msgid'):
            msgid = line[7:].rstrip('"\n')
        elif len(msgid) > 2 and line.startswith('msgstr'):
            if not msgid in translations:
                translations[msgid] = line[8:].rstrip('"\n')


repos = ['nv_tlview']

unused = [
    '/nv_aeon2',
    '/nv_collection',
    '/nv_editor',
    '/nv_matrix',
    '/nv_templates',
    '/nv_timeline',
    '/nv_updater',
    ]

translations = {}
for repo in repos:
    read_translations(f'../{repo}/i18n/de.po')
read_translations('../novelibre/i18n/de.po')

# Sort the terms by length to minimize errors.
sortedTranslations = sorted(translations, key=len, reverse=True)

'''
links = {}
for t in translations:
    links[f"#{t.lower().replace(' ','-')}"] = f"#{translations[t].lower().replace(' ','-')}"

sortedTranslations = sorted(links, key=len, reverse=True)
translations = links

for helpFile in glob.iglob('*.rst', root_dir=f'../nvhelp-de/source'):
    process_file(f'../nvhelp-de/source/{helpFile}', f'source/{helpFile}')
'''
for repo in repos:
    for helpFile in glob.iglob('*.rst', root_dir=f'../nvhelp-de/source/{repo}'):
        process_file(f'../nvhelp-de/source/{repo}/{helpFile}', f'source/{repo}/{helpFile}')
