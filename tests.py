import os
import sys
import random

POSSIBLE_VIDEOS_EXTENSIONS = ['.mkv', '.mp4', '.wmv', '.mov', '.avi']
POSSIBLE_SUBTITLES_EXTENSIONS = ['.srt', '.ass', '.ssa', '.srt', '.ssa']


def createTestFiles(n, test_directory):
	for i in range(n):
		open(os.path.join(test_directory, str(i) + 'test' + POSSIBLE_VIDEOS_EXTENSIONS[random.randint(0, 4)]), 'w').close()
		f = open(os.path.join(test_directory, 'testsub' + str((i+1)) + POSSIBLE_SUBTITLES_EXTENSIONS[random.randint(0, 4)]), 'w')
		f.write(str(i))
		f.close()

def deleteTestFiles(test_directory):
	files = os.listdir(test_directory)
	for file in files:
		os.remove(os.path.join(test_directory, file))

def validateTests(n, test_directory):
	i=0
	files = os.listdir(test_directory)
	for file in files:
		f = open(os.path.join(test_directory, file), 'r')
		if f.read() == file[0]:
			i = i + 1
	if i != n:
		raise Exception('Something went wrong.\nTotal No. of Tests: ', n, '\nSccessful tests: ', i, ' | Unsuccessful tests: ', (n-i), '\n')
		sys.exit()
	else:
		print('All tests: OK\n')