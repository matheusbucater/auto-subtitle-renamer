import os

#Here you gotta input .mkv or .mp4 or .wmv and so on
vid_type = input('Video archive extension: ')
#Here you gotta input .srt or .ass or .ssa and so on
sub_type = input('Subtitle archive extension: ')

dirpath = os.getcwd()
files_list = os.listdir(dirpath)


def GetExt(the_list, val):
	return [value for value in the_list if value.endswith(val)]

sub_list = GetExt(files_list, sub_type)
vid_list = GetExt(files_list, vid_type)


vidSub_list = []
for i in range(len(vid_list)):
	vidSub_list.append(vid_list[i].replace(vid_type, sub_type))


for i in range(len(sub_list)):
	os.renames(sub_list[i], vidSub_list[i])
