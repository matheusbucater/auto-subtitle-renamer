from gooey import GooeyParser, Gooey
from argparse import ArgumentParser
import auto_subtitle_renamer as asr
import os
import sys

@Gooey(
	advanced=True,
    program_name="Auto Subtitle Renamer",
    
)
def main():

	parser = GooeyParser(description='Make sure all of your video files and subtitle files are ordered by season/episode')
	parser.add_argument('--folder', required=True, metavar='Folder', help='Choose the folder that contains your files', widget='DirChooser')
	parser.add_argument('--enable_tests', default=False, action="store_true", required=False, metavar='Enable Tests', help='The program will create or use your chosen a test folder', widget='BlockCheckbox')
	parser.add_argument('--tests_folder', required=False, metavar='Tests Folder', help='Choose the directory that the tests folder will be created\n(its not necessary to specify a directory, you can leave this blank)', widget='DirChooser')

	args = parser.parse_args()
	
	directory = vars(args)['folder']
	tests_directory = vars(args)['tests_folder']
	isTestsEnabled = vars(args)['enable_tests']

	print('\nDirectory: ', directory)
	if os.path.exists(directory) == True:
		if isTestsEnabled == True:
			if tests_directory is None:
				print('\nTest Directory: default')
				tests_directory = os.path.join(directory, 'tests')
				asr.checkIfTestFolderExists(tests_directory)
				print('\nTest Directory: default ---> ', tests_directory)
			elif os.path.exists(tests_directory) == True:
				print('\nTest Directory: ', tests_directory)
				raise Exception('The chosen test directory doesnt exist')
			asr.validationAuxFunction(tests_directory)
		print('\nRunning program:')
		asr.main(directory)
		print('\nCongrats... All subtitles were renamed!')
		print('\n(you can delete the tests folder now)')
	else:
		raise Exception('The chosen  directory doesnt exist')
main()