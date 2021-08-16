# auto-subtitle-renamer
[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate?hosted_button_id=86XUMMWCBSTZY)  
**A small project that renames the subtitle files to match the video files.**  
So if you have a 'hello world s02e04.mkv' and a 'hello world s02e04 webrip.srt' in your directory, the program will rename the 'hello world s02e04 webrip.srt' to 'hello world s02e04.srt'  
Donwload: [here](https://github.com/matheusbucater/auto-subtitle-renamer/releases)  
  
**If you want to support this project, feel free to donate using the button on the top or the QR CODE bellow**  
  
![alt text](https://github.com/matheusbucater/auto-subtitle-renamer/blob/master/resources/QR%20Code.png)

  
**Important Stuff**  
In order to the program to work, your files **must be** in an individual folder separated by seasons and the files **must be** in alphanumerical order.  
The User Interface that I made does **NOT** validate the given directory, so be aware of that. I actually wanted to use an askDirectory Dialog from tkinter but I had a hard time trying to use the directory entry but I'll probably give an other shot soon enough.  
If you are using the exe file without User Interface place the file inside your videos/subtitles folder and then execute it.  
On commit 'asr no ui with tests' I've added automated tests that will create an addiotional folder 'tests' inside your current directory.  
You can delete this folder if you want to.
