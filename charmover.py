#! python3
# charmover.py - This program extracts/moves files from my mugen character
# and stage download folders to my mugen chars/stages folder.

import os, subprocess, patoolib, zipfile, re


def charmover():
    downloaddir = 'C:\\users\\jtoat\\downloads\\MUGEN stuff\\'
    chardir = downloaddir + 'MUGEN chars\\'
    charfiles = os.listdir(chardir)
    chardest = 'C:\\Games\\M.I.C.A Final Version Edition 1.1b1\\chars\\'
    extractdir = downloaddir + 'Extracted_Files\\'
    tally = 0
    for char in charfiles:
        pathtochar = os.path.join(chardir, char)
        if os.path.isfile(pathtochar):
            patoolib.extract_archive(pathtochar, outdir=extractdir)
            if len(os.listdir(extractdir)) == 1:
                tally += 1
                for file in os.listdir(extractdir):
                    os.rename(extractdir + file, chardest + file)
            else:
                if char[-3:] == '.7z':
                    os.mkdir(chardir + char[0:-3])
                    newdirname = char[:-3]
                    newdir = chardir + newdirname + '\\'
                else:
                    os.mkdir(chardir + char[:-4])
                    newdirname = char[:-4]
                    newdir = chardir + newdirname + '\\'
                for file in os.listdir(extractdir):
                    os.rename(extractdir + file, newdir + file)
                os.rename(newdir, chardest + newdirname)
                tally += 1
            os.remove(pathtochar)
        else:
            tally += 1
            os.rename(pathtochar, chardest + char)
    print('\nCharacter transfer complete. {} characters were moved.'.format(tally))


def stagemover():
    downloaddir = 'C:\\users\\jtoat\\downloads\\MUGEN stuff\\'
    stagedir = downloaddir + 'Mugen stages\\'
    stagefiles = os.listdir(stagedir)
    stagedest = 'C:\\Games\\M.I.C.A Final Version Edition 1.1b1\\stages\\'
    sounddest = 'C:\\Games\\M.I.C.A Final Version Edition 1.1b1\\sound\\'
    stagecontents = os.listdir(stagedest)
    includedsoundcontents = os.listdir(stagedest + 'sound')
    musicRegex = re.compile(r'.*\.(?:ogg|mp3)')
    tally = 0
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
    print('Stage transfer complete. {} stages were moved.'.format(tally))


charmover()
stagemover()
os.startfile(r'C:\Games\M.I.C.A Final Version Edition 1.1b1\VSelect.exe')
