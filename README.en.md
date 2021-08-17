# auto-subtitle-renamer
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?hosted_button_id=86XUMMWCBSTZY)  
**A small project that renames the subtitle files to match the video files.**  
So if you have a 'hello world s02e04.mkv' and a 'hello world sub s02e04-webrip.srt' in your directory, the program will rename the 'hello world sub s02e04-webrip.srt' to 'hello world s02e04.srt'  
Donwload: [here](https://github.com/matheusbucater/auto-subtitle-renamer/releases)  
  
**If you want to support this project, feel free to donate using the button on the top or the QR CODE bellow**  
  
![alt text](https://github.com/matheusbucater/auto-subtitle-renamer/blob/master/resources/QR%20Code.png)

  
**Important Stuff**  
In order to the program to work in any version, your files **must be** in an individual folder ordered by season/episode.  
If you're using the [v2.1](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/V2.1) UI be careful with the tests folder **THE PROGRAM WILL DELETE ALL FILES IN THE CHOSEN TEST FOLDER**.  
If you're using the [v2.0](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/v2.0) (with I don't recommend), it does **NOT** validate the given directory, so be aware of that. I had a hard time trying to use the askDirectory dialog from tkinter so I switched to gooey [v2.1](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/V2.1).  
If you are using the exe file without User Interface you have to place the file inside your videos/subtitles folder and then execute it.  
On commit 'asr no ui with tests' [v1.1](https://github.com/matheusbucater/auto-subtitle-renamer/releases/tag/v1.1) I've added automated tests that will create an addiotional folder 'tests' inside your current directory.  
You can delete this folder if you want to.
