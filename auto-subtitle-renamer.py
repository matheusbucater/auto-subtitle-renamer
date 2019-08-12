import os


files_list = os.listdir(os.getcwd())

vid_type = ['.mkv', '.mp4', '.wmv', '.mov', '.avi']
sub_type = ['.srt', '.ass', '.ssa']



def GetExt(the_list, val):
	return [value for value in the_list if value.endswith(val)]
	
vid_ext = '.mp4'
sub_ext = '.srt'

vid = []
for i in range(len(vid_type)):
	vid.append(GetExt(files_list, vid_type[i]))

sub = []
for i in range(len(sub_type)):
	sub.append(GetExt(files_list, sub_type[i]))

fixed_vidList = [x for x in vid if x][0]
fixed_subList = [x for x in sub if x][0]


def Something(some_list, some_ext):
	global vid_ext
	global sub_ext
	for i in range(len(some_list)):
		x = some_list[i].endswith(some_ext)
	if x == True:
		if some_list == fixed_vidList:
			for i in range(len(fixed_vidList)):
				if some_ext == vid_type[i]:
					vid_ext = some_ext

		if some_list == fixed_subList:
			for i in range(len(fixed_subList)):
				if some_ext == sub_type[i]:
					sub_ext = some_ext


def ApllySomething(some_list, some_type):
	for i in range(len(some_type)):
		Something(some_list, some_type[i])
		

ApllySomething(fixed_vidList, vid_type)
ApllySomething(fixed_subList, sub_type)


def GetExt(the_list, val):
	return [value for value in the_list if value.endswith(val)]


def main():
	sub_list = GetExt(files_list, sub_ext)
	vid_list = GetExt(files_list, vid_ext)


	vidSub_list = []
	for i in range(len(vid_list)):
		vidSub_list.append(vid_list[i].replace(vid_ext, sub_ext))

	for i in range(len(sub_list)):
		os.renames(sub_list[i], vidSub_list[i])	


main()
