import os 
import shutil

def partition(path, target_path):

  # generate new path
  filenames = os.listdir(path)
  for tpath in target_path:
    if not os.path.isdir(tpath):
      os.makedirs(tpath)

  # get filename and partition
  for name in filenames:
    num = name.split('.')[0]
    if num[-2:] == '10':
      shutil.move(path+name, target_path[0])
    elif num[-2:] == '20':
      shutil.move(path+name, target_path[1])
    elif num[-2:] == '30':
      shutil.move(path+name, target_path[2])
    elif num[-2:] == '40':
      shutil.move(path+name, target_path[3])
    elif num[-2:] == '50':
      shutil.move(path+name, target_path[4])
    elif num[-2:] == '60':
      shutil.move(path+name, target_path[5])
    elif num[-2:] == '70':
      shutil.move(path+name, target_path[6])
    elif num[-2:] == '80':
      shutil.move(path+name, target_path[7])
    elif num[-2:] == '90':
      shutil.move(path+name, target_path[8])
    elif num[-2:] == '00':
      shutil.move(path+name, target_path[9])
      print "move %s to %s successfully" % (name, target_path[9])

path = 'nba_1113_thunder_mavericks/'
target_path = []
for i in range(1,11):
  target_path.append(path+str(i))

partition(path, target_path)
