import os


filelist = []
file_count = {}

def get_dict(file_path):
    for path in file_path:
        with open(path, 'rt',encoding="utf_8") as f:
            file_count[str(path).split('\\')[-1]] = [len(f.readlines()), path]
    return(sorted(file_count.items(), key=lambda item: item[1], reverse=True))

for root, dirs, files in os.walk('files'):
	for file in files:
		filelist.append(os.path.join(root,file))

with open('task_3.txt', 'a',encoding="utf_8") as task:
    data = get_dict(filelist)
    for line in data:
        task.write(str(line[0]) + '\n')
        task.write(str(line[1][0])+ '\n')
        with open(str(line[1][1]), encoding="utf_8") as wrt:
            task.write(wrt.read() + '\n\n')
print(True)