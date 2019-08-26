#! python3
# charmover.py - This program extracts/moves files from its mugen character
# and stage download folders to your mugen chars/stages folder.

import os
import patoolib
import re


def charmover():
    downloaddir = os.getcwd()
    if not os.path.exists(os.path.join(downloaddir, 'Mugen chars')):
        os.mkdir(os.path.join(downloaddir, 'MUGEN chars'))
    chardir = os.path.join(downloaddir, 'MUGEN chars')
    charfiles = os.listdir(chardir)
    if os.path.exists(os.path.join(os.getcwd(), 'path.txt')):
        with open(os.path.join(os.getcwd(), 'path.txt')) as m:
            mugenroot = m.read()
    else:
        while True:
            print('Please input the path to your MUGEN root folder.')
            mugenroot = input('> ').strip('\"')
            if os.path.exists(os.path.join(mugenroot, 'chars')):
                with open(os.path.join(os.getcwd(), 'path.txt'), 'w') as m:
                    m.write(mugenroot)
                break
            else:
                print('It seems that directory is invalid.')
    chardest = os.path.join(mugenroot, 'chars')
    if not os.path.exists(os.path.join(downloaddir, 'Extracted Files')):
        os.mkdir(os.path.join(downloaddir, 'Extracted Files'))
    extractdir = os.path.join(downloaddir, 'Extracted Files')
    tally = 0
    for char in charfiles:
        pathtochar = os.path.join(chardir, char)
        if os.path.isfile(pathtochar):
            patoolib.extract_archive(pathtochar, outdir=extractdir)
            filecount = 0
            for item in os.listdir(extractdir):
                if os.path.isfile(os.path.join(extractdir, item)):
                    filecount += 1
            if filecount <= 1:
                for item in os.listdir(extractdir):
                    os.rename(os.path.join(extractdir, item), os.path.join(chardest, item))
                    tally += 1
            else:
                if char[-3:] == '.7z':
                    newdirname = char[:-3]
                    newdir = os.path.join(chardest, newdirname)
                    if not os.path.exists(newdir):
                        os.mkdir(os.path.join(chardest, char[:-3]))
                    for item in os.listdir(extractdir):
                        os.rename(os.path.join(extractdir, item), os.path.join(newdir, item))
                        tally += 1
                else:
                    newdirname = char[:-4]
                    newdir = os.path.join(chardest, newdirname)
                    if not os.path.exists(newdir):
                        os.mkdir(os.path.join(chardest, char[:-4]))
                    for item in os.listdir(extractdir):
                        os.rename(os.path.join(extractdir, item), os.path.join(newdir, item))
                        tally += 1
            os.remove(pathtochar)
        else:
            os.rename(pathtochar, os.path.join(chardest, char))
            tally += 1
    print(f'\nCharacter transfer complete. {tally} files were moved.')


def stagemover():
    downloaddir = os.getcwd()
    if not os.path.exists(os.path.join(downloaddir, 'Mugen stages')):
        os.mkdir(os.path.join(downloaddir, 'MUGEN stages'))
    stagedir = os.path.join(downloaddir, 'MUGEN stages')
    stagefiles = os.listdir(stagedir)
    if os.path.exists(os.path.join(os.getcwd(), 'path.txt')):
        with open(os.path.join(os.getcwd(), 'path.txt')) as m:
            mugenroot = m.read()
    else:
        while True:
            print('Please input the path to your MUGEN root folder.')
            mugenroot = input('> ').strip('\"')
            if os.path.exists(os.path.join(mugenroot, 'stages')):
                with open(os.path.join(os.getcwd(), 'path.txt'), 'w') as m:
                    m.write(mugenroot)
                break
            else:
                print('It seems that directory is invalid.')
    stagedest = os.path.join(mugenroot, 'stages')
    sounddest = os.path.join(mugenroot, 'sound')
    includedsound = os.path.join(stagedir, 'sound')
    extractdir = os.path.join(downloaddir, 'Extracted Files')
    musicRegex = re.compile(r'.*\.(?:ogg|mp3)')
    tally = 0
    for stage in stagefiles:
        tally += 1
        pathtostage = os.path.join(stagedir, stage)
        if os.path.isfile(pathtostage):
            patoolib.extract_archive(pathtostage, outdir=extractdir)
            extractedstage = os.listdir(extractdir)
            for item in extractedstage:
                if os.path.isfile(os.path.join(extractdir, item)):
                    os.rename(os.path.join(extractdir, item), os.path.join(stagedest, item))
                else:
                    extractedfolder = os.listdir(os.path.join(extractdir, item))
                    for file in extractedfolder:
                        os.rename(os.path.join(extractdir, item, file), os.path.join(stagedest, file))
                    os.rmdir(os.path.join(extractdir, item))
            os.remove(pathtostage)
        else:
            stagefolder = os.listdir(pathtostage)
            for item in stagefolder:
                os.rename(os.path.join(pathtostage, item), os.path.join(stagedest, item))
            os.rmdir(pathtostage)
        if os.path.exists(includedsound):
            includedsoundcontents = os.listdir(includedsound)
            for item in includedsoundcontents:
                os.rename(os.path.join(includedsound, item), os.path.join(sounddest, item))
            os.rmdir(includedsound)
    stagecontents = os.listdir(stagedest)
    for item in stagecontents:
        if musicRegex.findall(str(item)) != []:
            os.rename(os.path.join(stagedest, item), os.path.join(sounddest, item))
    print(f'Stage transfer complete. {tally} files were moved.\n')
    while True:
        print('Thank you for using Fun_Police\'s Char_Mover!\nWould you like to run VSelect? y/n')
        r = input('> ')
        if r.lower() == 'y':
            if os.path.exists(os.path.join(mugenroot, 'VSelect.exe')):
                os.startfile(os.path.join(mugenroot, 'VSelect.exe'))
                break
            else:
                print('VSelect could not be found. Please make sure that VSelect.exe is inside your root MUGEN folder.')
                input('> ')
                break
        if r.lower() == 'n':
            break


charmover()
stagemover()

