#! python3
# charmover.py - This program extracts/moves files from its mugen
# download folder to your mugen chars/stages folder.

import os
import patoolib
import re
import shutil
join = os.path.join
exists = os.path.exists
listdir = os.listdir
def fileidentify():
    parent_folder = os.getcwd()
    extract_dir = join(parent_folder, 'Extracted')
    charregex = re.compile(r'.*\.(?:cns|cmd|c)$')
    stageregex = re.compile(r'.*\.(?:def|sff)$')
    musicregex = re.compile(r'.*\.(?:ogg|mp3)$')
    archiveregex = re.compile(r'.*\.(?:rar|7z|zip)$')
    if not exists(extract_dir):
        os.mkdir(extract_dir)
    if os.path.exists(join(parent_folder, 'dlpath.txt')):
        with open(join(parent_folder, 'dlpath.txt')) as dlpath:
            downloads_folder = dlpath.read()
    else:
        while True:
            print('Please input a path to the folder you wish to use for MUGEN downloads. Default is inside this '
            'program\'s root folder.')
            r = input('> ')
            if r == '':
                downloads_folder = join(parent_folder, 'Downloads')
                if not exists(downloads_folder):
                    os.mkdir(join(parent_folder, 'Downloads'))
                with open(join(parent_folder, 'dlpath.txt'), 'w') as dlpath:
                    dlpath.write(downloads_folder)
                print(f'The downloads folder is now located at {downloads_folder}')
                break
            else:
                if os.path.isdir(r):
                    downloads_folder = r
                    with open(join(parent_folder, 'dlpath.txt'), 'w') as pathfile:
                        pathfile.write(downloads_folder)
                    print(f'The downloads folder is now located at {downloads_folder}')
                    break
                else:
                    print('It seems that path is not a valid directory.')
    if os.path.exists(os.path.join(os.getcwd(), 'mugenpath.txt')):
        with open(os.path.join(os.getcwd(), 'mugenpath.txt')) as m:
            mugenroot = m.read()
    else:
        while True:
            print('Please input the path to your MUGEN root folder.')
            mugenroot = input('> ').strip('\"')
            if os.path.exists(os.path.join(mugenroot, 'chars')):
                with open(os.path.join(os.getcwd(), 'mugenpath.txt'), 'w') as m:
                    m.write(mugenroot)
                break
            else:
                print('It seems that directory is invalid.')
    character_dir = join(mugenroot, 'chars')
    stage_dir = join(mugenroot, 'stages')
    sound_dir = join(mugenroot, 'sound')
    for outer_file in listdir(downloads_folder):
        if exists(extract_dir):
            shutil.rmtree(extract_dir)
        if not exists(extract_dir):
            os.mkdir(extract_dir)
        archive = False
        char_evidence = 0
        stage_evidence = 0
        path_to_outer_file = join(downloads_folder, outer_file)
        if archiveregex.findall(outer_file) != []:
            archive = True
        if os.path.isdir(path_to_outer_file):
            for inner_file in listdir(path_to_outer_file):
                if os.path.isdir(join(path_to_outer_file, inner_file)):
                    for innerer_file in listdir(join(path_to_outer_file, inner_file)):
                        if charregex.findall(innerer_file) != []:
                            char_evidence += 1
                        if stageregex.findall(innerer_file) != []:
                            stage_evidence += 1
                else:
                    if charregex.findall(inner_file) != []:
                        char_evidence += 1
                    if stageregex.findall(inner_file) != []:
                        stage_evidence += 1
            if char_evidence >= 1:
                if exists(join(character_dir, outer_file)):
                    shutil.rmtree(join(character_dir, outer_file))
                os.rename(path_to_outer_file, join(character_dir, outer_file))
            if char_evidence == 0 and stage_evidence >= 1:
                for item in listdir(path_to_outer_file):
                    if exists(join(stage_dir, item)):
                        os.remove(join(stage_dir, item))
                    os.rename(join(path_to_outer_file, item), join(stage_dir, item))
                os.rmdir(path_to_outer_file)
        if archive:
            if os.path.getsize(path_to_outer_file) > 314572800:
                continue
            patoolib.extract_archive(path_to_outer_file, outdir=extract_dir)
            filecount = 0
            for extracted_item in os.listdir(extract_dir):
                if os.path.isfile(join(extract_dir, extracted_item)):
                    filecount += 1
            if filecount <= 1:
                for extracted_item in os.listdir(extract_dir):
                    if os.path.isdir(join(extract_dir, extracted_item)):
                        for item in listdir(join(extract_dir, extracted_item)):
                            if charregex.findall(item) != []:
                                char_evidence += 1
                            if stageregex.findall(item) != []:
                                stage_evidence += 1
                if char_evidence >= 1:
                    for extracted_item in listdir(extract_dir):
                        if exists(join(character_dir, extracted_item)):
                            shutil.rmtree(join(character_dir, extracted_item))
                        os.rename(join(extract_dir, extracted_item), join(character_dir, extracted_item))
                    for retry in range(100):
                        try:
                            os.remove(path_to_outer_file)
                            break
                        except:
                            pass
                if char_evidence == 0 and stage_evidence >= 1:
                    for extracted_item in listdir(extract_dir):
                        if os.path.isdir(join(extract_dir, extracted_item)):
                            for inner_item in listdir(join(extract_dir, extracted_item)):
                                if exists(join(stage_dir, inner_item)):
                                    os.remove(join(stage_dir, inner_item))
                                os.rename(join(extract_dir, extracted_item, inner_item), join(stage_dir, inner_item))
                            os.rmdir(join(extract_dir, extracted_item))
                        else:
                            if exists(join(stage_dir, extracted_item)):
                                os.remove(join(stage_dir, extracted_item))
                            os.rename(join(extract_dir, extracted_item), join(stage_dir, extracted_item))
                        for retry in range(100):
                            try:
                                os.rmdir(join(extract_dir, extracted_item))
                                break
                            except:
                                pass
                            try:
                                os.remove(join(extract_dir, extracted_item))
                            except:
                                pass
                    for retry in range(100):
                        try:
                            os.remove(path_to_outer_file)
                            break
                        except:
                            pass
            else:
                for extracted_item in listdir(extract_dir):
                    if os.path.isdir(join(extract_dir, extracted_item)):
                        for item in listdir(join(extract_dir, extracted_item)):
                            if charregex.findall(item) != []:
                                char_evidence += 1
                            if stageregex.findall(item) != []:
                                stage_evidence += 1
                    else:
                        if charregex.findall(extracted_item) != []:
                            char_evidence += 1
                        if stageregex.findall(extracted_item) != []:
                            stage_evidence += 1
                if char_evidence >= 1:
                    if outer_file[-3:] == '.7z':
                        newdirname = outer_file[:-3]
                        newdir = os.path.join(character_dir, newdirname)
                        if not os.path.exists(newdir):
                            os.mkdir(newdir)
                        for item in os.listdir(extract_dir):
                            if exists(join(newdir, item)):
                                os.remove(join(newdir, item))
                            os.rename(os.path.join(extract_dir, item), os.path.join(newdir, item))
                    else:
                        newdirname = outer_file[:-4]
                        newdir = os.path.join(character_dir, newdirname)
                        if not os.path.exists(newdir):
                            os.mkdir(newdir)
                        for item in os.listdir(extract_dir):
                            if exists(join(newdir, item)):
                                os.remove(join(newdir, item))
                            os.rename(os.path.join(extract_dir, item), os.path.join(newdir, item))
                    for retry in range(100):
                        try:
                            os.remove(path_to_outer_file)
                            break
                        except:
                            pass
                if char_evidence == 0 and stage_evidence >= 1:
                    for item in listdir(extract_dir):
                        if exists(join(stage_dir, item)):
                            os.remove(join(stage_dir, item))
                        os.rename(join(extract_dir, item), join(stage_dir, item))
                    for retry in range(100):
                        try:
                            os.remove(path_to_outer_file)
                            break
                        except:
                            pass
    for item in listdir(stage_dir):
        if musicregex.findall(str(item)) != []:
            if exists(join(sound_dir, item)):
                os.remove(join(sound_dir, item))
            os.rename(os.path.join(stage_dir, item), os.path.join(sound_dir, item))
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


fileidentify()
