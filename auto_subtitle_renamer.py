import os
import sys
import tests

POSSIBLE_VIDEOS_EXTENSIONS = ['.mkv', '.mp4', '.wmv', '.mov', '.avi']
POSSIBLE_SUBTITLES_EXTENSIONS = ['.srt', '.ass', '.ssa']
CURRENT_DIRECTORY = os.getcwd() + '/'
TESTS_DIRECTORY = #PUT YOUR TESTS DIRECTORY HERE	


def getListWithAllExtensions(file_list):
	list_with_all_extensions = []
	for file in file_list:
		list_with_all_extensions.append(os.path.splitext(file)[1])
	return list_with_all_extensions

def getTuppleWithVideoAndSubtitleExtensions(extension_list):
	aux_list = extension_list
	i = 0
	for extension in aux_list:
		if extension in POSSIBLE_VIDEOS_EXTENSIONS:
			i = i + 1
	if aux_list[i] in POSSIBLE_SUBTITLES_EXTENSIONS:
		return aux_list[:i], aux_list[i:]
	else:
		return aux_list[i:], aux_list[:i]

def getVideoFiles(file_list, videos_extensions_list):
	videos = []
	for video in file_list:
		for extension in set(videos_extensions_list):
			if video.endswith(extension):
				videos.append(video)
	return videos

def getSubtitleFiles(file_list, subtitles_extensions_list):
	subtitles = []
	for subtitle in file_list:
		for extension in set(subtitles_extensions_list):
			if subtitle.endswith(extension):
				subtitles.append(subtitle)
	return subtitles

def getVideoFileNameWithoutExtension(videos_list):
	videos_list_whithout_extension = []
	for video in videos_list:
		videos_list_whithout_extension.append(os.path.splitext(video)[0])
	return videos_list_whithout_extension


def renameSubtitles(directory, videos_without_extensions_list, subtitles_list, subtitles_extensions_list):
	videos_with_subtitles_extensions = []
	for i in range(len(videos_without_extensions_list)):
		videos_with_subtitles_extensions.append(videos_without_extensions_list[i] + subtitles_extensions_list[i])
	for i in range(len(subtitles_list)):
		os.renames(directory + subtitles_list[i], directory + videos_with_subtitles_extensions[i])

def main(directory):
	files_list = os.listdir(directory)

	extensions_files_list = getListWithAllExtensions(files_list)
	videos_extensions, subtitles_extensions = getTuppleWithVideoAndSubtitleExtensions(extensions_files_list)

	videos = getVideoFiles(files_list, videos_extensions)

	subtitles = getSubtitleFiles(files_list, subtitles_extensions)

	if len(videos) != len(subtitles):
		print('A QUANTIDADE DE ARQUIVOS DE VIDEO É DIFERENTE DA QUANTIDADE DE ARQUIVOS DE LEGENDA')
		sys.exit()
		
	else:
		videos = getVideoFileNameWithoutExtension(videos)

		renameSubtitles(directory, videos, subtitles, subtitles_extensions)
		
def validationAuxFunction(test_directory):
	tests.deleteTestFiles(test_directory)
	tests.createTestFiles(5, test_directory)
	main(test_directory)
	tests.validateTests(5, test_directory)


# validationAuxFunction(TESTS_DIRECTORY)
# main(CURRENT_DIRECTORY)