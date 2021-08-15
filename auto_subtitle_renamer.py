import os
import sys

POSSIBLE_VIDEOS_EXTENSIONS = ['.mkv', '.mp4', '.wmv', '.mov', '.avi']
POSSIBLE_SUBTITLES_EXTENSIONS = ['.srt', '.ass', '.ssa']


def getFilesGivenAnExtension(file_list, extension):
	return [file for file in file_list if file.endswith(extension)]

def getVideoFiles(file_list):
	videos = []
	for extension in POSSIBLE_VIDEOS_EXTENSIONS:
		videos.append([video for video in file_list if video.endswith(extension)])
	return videos

def getSubtitleFiles(file_list):
	subtitles = []
	for extension in POSSIBLE_SUBTITLES_EXTENSIONS:
		subtitles.append([subtitle for subtitle in file_list if subtitle.endswith(extension)])
	return subtitles	

def joinDifferentExtensions(files):
	new_list_files = []
	for i in files:
		if i:
			for j in i:
				new_list_files.append(j)
	return new_list_files

def getVideoFileNameWithoutExtension(videos_list):
	videos_list_whithout_extension = []
	for video in videos_list:
		videos_list_whithout_extension.append(os.path.splitext(video)[0])
	return videos_list_whithout_extension

def getListWithSubtitlesExtensions(subtitles_list):
	list_with_subtitles_extensions = []
	for subtitle in subtitles_list:
		list_with_subtitles_extensions.append(os.path.splitext(subtitle)[1])
	return list_with_subtitles_extensions

def renameSubtitles(videos_without_extensions_list, subtitles_list, subtitles_extensions_list):
	videos_with_subtitles_extensions = []
	for i in range(len(videos_without_extensions_list)):
		videos_with_subtitles_extensions.append(videos_without_extensions_list[i] + subtitles_extensions_list[i])
	for i in range(len(subtitles_list)):
		os.renames(subtitles_list[i], videos_with_subtitles_extensions[i])

def main(directory):
	files_list = os.listdir(directory)

	videos = getVideoFiles(files_list)
	videos = joinDifferentExtensions(videos)

	subtitles = getSubtitleFiles(files_list)
	subtitles = joinDifferentExtensions(subtitles)

	if len(videos) != len(subtitles):
		print('A QUANTIDADE DE ARQUIVOS DE VIDEO É DIFERENTE DA QUANTIDADE DE ARQUIVOS DE LEGENDA')
		sys.exit()
		
	else:
		videos = getVideoFileNameWithoutExtension(videos)
		subtitles_extensions = getListWithSubtitlesExtensions(subtitles)

		renameSubtitles(videos, subtitles, subtitles_extensions)
