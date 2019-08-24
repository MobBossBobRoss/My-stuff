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
    if os.path.exists('./path.txt'):
        with open('./path.txt', 'r') as m:
            mugenroot = m.read()
    else:
        while True:
            print('Please input the path to your MUGEN root folder.')
            mugenroot = input('> ')
            if os.path.exists(os.path.join(mugenroot, 'chars')):
                with open('./path.txt', 'w') as m:
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
            if len(os.listdir(extractdir)) == 1:
                tally += 1
                for file in os.listdir(extractdir):
                    os.rename(os.path.join(extractdir, file), os.path.join(chardest, file))
            else:
                if char[-3:] == '.7z':
                    os.mkdir(os.path.join(chardir, char[:-3]))
                    newdirname = char[:-3]
                    newdir = os.path.join(newdir, newdirname)
                else:
                    os.mkdir(os.path.join(chardir, char[:-4]))
                    newdirname = char[:-4]
                    newdir = os.path.join(newdir, newdirname)
                for file in os.listdir(extractdir):
                    os.rename(os.path.join(extractdir, file), os.path.join(newdir, file))
                os.rename(newdir, os.path.join(chardest, newdirname))
                tally += 1
            os.remove(pathtochar)
        else:
            tally += 1
            os.rename(pathtochar, os.path.join(chardest, char))
    print(f'\nCharacter transfer complete. {tally} characters were moved.')


def stagemover():
    downloaddir = os.getcwd()
    if not os.path.exists(os.path.join(downloaddir, 'Mugen stages')):
        os.mkdir(os.path.join(downloaddir, 'MUGEN stages'))
    stagedir = os.path.join(downloaddir, 'MUGEN stages')
    stagefiles = os.listdir(stagedir)
    if os.path.exists('./path.txt'):
        with open('./path.txt', 'r') as m:
            mugenroot = m.read()
    else:
        while True:
            print('Please input the path to your MUGEN root folder.')
            mugenroot = input('> ')
            if os.path.exists(os.path.join(mugenroot, 'stages')):
                with open('./path.txt', 'w') as m:
                    m.write(mugenroot)
                break
            else:
                print('It seems that directory is invalid.')
    stagedest = os.path.join(mugenroot, 'stages')
    sounddest = os.path.join(mugenroot, 'sound')
    stagecontents = os.listdir(stagedest)
    includedsoundcontents = os.listdir(os.path.join(stagedest, 'sound'))
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
    print(f'Stage transfer complete. {tally} stages were moved.\n')
    while True:
        print('Would you like to run VSelect? y/n')
        r = input('> ')
        if r.lower() == 'y':
            if os.path.exists(os.path.join(mugenroot, 'VSelect.exe')):
                os.startfile(os.path.join(mugenroot, 'VSelect.exe'))
                break
            else:
                print('VSelect could not be found. Please make sure that VSelect.exe is inside your root MUGEN folder.')
                input('> ')
                break


charmover()
stagemover()

