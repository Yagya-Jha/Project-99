import os
import shutil
import time

#path = input('Enter the Location of Folder in hich you want this file to run:- ')

path = os.getcwd()

if os.path.exists(path):
    for subdir, dirs, files in os.walk(path):
        for file in files:
            if file != 'RemoveFiles.py':
                exact_path = os.path.join(path, file)
                if os.path.exists(exact_path):
                    file_status = os.stat(exact_path)
                    print (file)
                    created_on = file_status.st_ctime
                    readable_created_on = time.asctime(time.gmtime(created_on))
                    print('File was created on:- ', readable_created_on)
                    if readable_created_on > time.asctime(time.gmtime()):
                        print('file is old')
                        os.remove(exact_path)
                    else:
                        print('file is new')
                    print('\n')

        for dir in dirs:
            for subdir, dirs, files in os.walk(path+'/'+dir):
                for file in files:
                    if file != 'RemoveFiles.py':
                        exact_path = os.path.join(path, dir, file)
                        if os.path.exists(exact_path):
                            file_status = os.stat(exact_path)
                            print (file)
                            created_on = file_status.st_ctime
                            readable_created_on = time.asctime(time.gmtime(created_on))
                            print('File was created on:- ', readable_created_on)

                            if readable_created_on > time.asctime(time.gmtime()):
                                print('file is old')
                                os.remove(exact_path)
                            else:
                                print('file is new')
                            print('\n')

else:
    print("Path Dosen't exists")

print('\n')

end = input('You Can Quit Now')