#! python3
# charmover.py - This program extracts/moves files from my mugen character
# and stage download folders to my mugen chars/stages folder.

import os, subprocess, patoolib, zipfile, re

chardir = 'C:\\users\\jtoat\\downloads\\Mugen chars'
stagedir = 'C:\\users\\jtoat\\downloads\\Mugen stages'
charfiles = os.listdir(chardir)
stagefiles = os.listdir(stagedir)
chardest = 'C:\\Games\\M.I.C.A Final Version Edition 1.1b1\\chars\\'
stagedest = 'C:\\Games\\M.I.C.A Final Version Edition 1.1b1\\stages\\'
sounddest = 'C:\\Games\\M.I.C.A Final Version Edition 1.1b1\\sound\\'
stagecontents = os.listdir(stagedest)
includedsoundcontents = os.listdir(stagedest + 'sound')
musicRegex = re.compile(r'.*\.(?:ogg|mp3)')
tally = 0

for char in charfiles:
    tally += 1
    pathtochar = os.path.join(chardir, char)
    if os.path.isfile(pathtochar):
        patoolib.extract_archive(pathtochar, outdir=chardest)
        os.remove(pathtochar)
    else:
        os.rename(pathtochar, chardest + char)

for stage in stagefiles:
    tally += 1
    pathtostage = os.path.join(stagedir, stage)
    if os.path.isfile(pathtostage):
        patoolib.extract_archive(pathtostage, outdir=stagedest)
    else:
        os.rename(pathtostage, stagedest + stage)
        os.remove(pathtostage)

for item in stagecontents:
    if musicRegex.findall(str(item)) != []:
        os.rename(os.path.join(stagedest, item), sounddest + str(item))

for item in includedsoundcontents:
    if musicRegex.findall(str(item)) != []:
        os.rename(os.path.join(stagedest + 'sound\\', item), sounddest + str(item))

print('\nFile transfer completed. ' + str(tally) + ' files were moved.')

os.startfile(r'C:\Games\M.I.C.A Final Version Edition 1.1b1\VSelect.exe')
