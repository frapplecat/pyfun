![pyfun hangman heading](#)

<br>
<br>
<br>

**TABLE OF CONTENTS**

- [**ABOUT PYFUN HANGMAN**](#about-pyfun-hangman)
- [**LOGIC CHART**](#logic-chart)
- [**USER STORIES**](#user-stories)
- [**INTRO SCREEN**](#intro-screen)
- [**ENTER NAME**](#enter-name)
- [**LET'S PLAY HANGMAN**](#let-s-play-hangman)
- [**INCORRECT GUESS**](#incorrect-guess)
- [**ALREADY GUESSED**](#already-guessed)
- [**INVALID GUESS**](#invalid-guess)
- [**CORRECT GUESS**](#correct-guess)
- [**WIN AND RELOAD**](#win-and-reload)
- [**LOSE AND RELOAD**](#lose-and-reload)
- [**FUTURE FEATURES**](#future-features)
- [**LANGUAGES USED**](#languages-used)
- [**RESOURCES**](#resources)
- [**MANUAL TESTING**](#manual-testing)
- [**AM I RESPONSIVE**](#am-i-responsive)
- [**VALIDATION**](#validation)
- [**BUGS**](#bugs)
- [**KNOWN ISSUES**](#known-issues)
- [**DEPLOYMENT**](#deployment)
- [**HOW TO FORK**](#how-to-fork)
- [**HOW TO CLONE**](#how-to-clone)
- [**VERSION CONTROL**](#version-control)
- [**CREDITS**](#credits)
- [**ACKNOWLEDGEMENTS**](#--acknowledgements)

<br>
<br>
<br>

# **ABOUT PYFUN HANGMAN**

This project is based on the classic pencil and paper game Hangman.
The user must guess the full word before hangman is hung. This is done by guessing a letter in the word.
If the guess is correct, it is placed in the blank spaces that make up the word but if the guess is incorrect the user loses a try and a section of the hangman is created. The word must be guessed before the user runs out of tries and the full hangman
drawing is displayed. 


<br>
<br>
<br>

# **LOGIC CHART**

![pyfun hangman logic chart](readme-images/pyfun-hangman-logic.png)

<br>
<br>
<br>


# **USER STORIES**

**Visitor Goals**

* I want to be able to play the game quickly
* I want to understand how ot play the game
* I want to be able to play the game as many times as I like


<br>
<br>
<br>

# **INTRO SCREEN**

![hangman introscreen](readme-images/pyfun-hangman-intro-screen.png)

<br>
<br>
<br>

# **ENTER NAME**

![hangman enter name](readme-images/pyfun-hangman-enter-name.png)

<br>
<br>
<br>

# **LET'S PLAY HANGMAN**

![let's play hangman](readme-images/pyfun-hangman-letsplay.png)

<br>
<br>
<br>

# **INCORRECT GUESS**

![hangman incorrect guess](readme-images/pyfun-hangman-incorrectguess.png)

<br>
<br>
<br>

# **ALREADY GUESSED**

![hangman already guessed](readme-images/pyfun-hangman-alreadyguessed.png)

<br>
<br>
<br>

# **INVALID GUESS**

![hangman invalid guess](readme-images/pyfun-hangman-notavalidguess.png)

<br>
<br>
<br>

# **CORRECT GUESS**

![hangman correct guess](readme-images/pyfun-hangman-correctguess.png)

<br>
<br>
<br>

# **WIN AND RELOAD**

![hangman winreload gif](readme-images/pyfun-hangman-youwin.png)

I hope that the user will want to play multiple times so on WIN a congratulations message will
pop-up with the option to try again.

<br>
<br>
<br>

# **LOSE AND RELOAD**

![hangman losereload gif](readme-images/pyfun-hangman-youlose.png)

I hope that the user will want to play multiple times so on LOSE a message with the answer will
print with the option to try again.

<br>
<br>
<br>

# **FUTURE FEATURES**

* Add difficulty level option
* Add a scoring system and keep track of high scores

<br>
<br>
<br>

# **LANGUAGES USED**

* Python
* Markdown

<br>
<br>
<br>

# **RESOURCES**

* **Gitpod** - to create the website and version control
* **Github** - to save and store the files for the website
* **Adobe Illustrator** - to create the logo and various headings
* **Am I Responsive** - to display the website on a range of devices
* **Texteditor.com** - for ASCII text art
* **Google Dev Tools** - for troubleshooting and testing fixes
* **CI Python Linter** - to test Python code
* **Slack, Stackoverflow, Youtube, Google, W3C Schools** - for help with troubleshooting errors
* **Coolors.co** - to check colour contrast
* **W3C Spell Checker** - to check website spelling
* **Freeconvert.com** - to compress mp4
* **Ezgif.com**- to convert compressed mp4 to gif for README
* **Record It Pro** - for screen-capturing video and converting mp4 to gif
* **GitHub Wiki TOC generator** - for generating README Table of Contents

<br>
<br>
<br>

# **MANUAL TESTING**
* I manually tested the game. I checked win, lose, play again and quit stages.
* I tested incorrect, invalid, duplicate and correct guesses.

<br>
<br>
<br>

# **AM I RESPONSIVE**
![am i responsive](readme-images/pyfun-hangman-amiresponsive.png)

<br>
<br>
<br>

# **VALIDATION**
**CI Python Linter**

![CI Python Linter validation](readme-images/pyfun-hangman-ci-pyhton-linter.png)

<br>
<br>
<br>

**PageSpeed Insights**

![pagespeed insight mobile](readme-images/pyfun-hangman-pagespeedinsights-mobile.png)
![pagespeed insight desktop](readme-images/pyfun-hangman-pagespeedinsights-desktop.png)

<br>
<br>
<br>

# **BUGS**

* **Expected** - when playing the game the classic hangman image would display as the players go through the tries.
* **Testing** - I ran the game using terminal. 
* **Result** - at certain stages the tries image wasn't displaying correctly.
* **Fix** - I had some spaces in the code that was causing the problem.

---

* **Expected** - when.
* **Testing** - I ran the game using terminal. 
* **Result** - once.
* **Fix** - I.

---

<br>
<br>
<br>

# **KNOWN ISSUES**

* 

<br>
<br>
<br>

# **DEPLOYMENT**

![deployment gif](#.gif)

* The site was deployed on Heroku<br>

* Open Heroku account.
* From the Heroku dashboard click the “Create new app” button.
* Name the app, the name has to be unique.
* Select region and click “Create app”. 
* Click on the settings tab.  
* Click “Add buildpack” here.
* Select Python then click “Save changes”.
* Select node.js and click “Save” again.
* Buildpacks must be in this order, with Python on top and node.js underneath.
* Go to the deploy section.  
* Select Github and confirm that we want to connect to Github.  
* Search for the Github repository name and once found click “connect”  
* Choose to manually deploy using the deploy branch option.  
* After creation you get an “App was successfully deployed” message  
with a button to take us to our deployed link. 


<br>
<br>
<br>

# **HOW TO FORK**

![how to fork gif](readmeimages/howtofork.gif)

* Login/signup to GitHub.
* Locate the relevant repository, for example: https://github.com/frapplecat/pyfun
* Click on the 'Fork' button in the top right corner.
* The forked version of this repo will be generated.

<br>
<br>
<br>

# **HOW TO CLONE**

![how to clone gif](#)

* On GitHub.com, navigate to the main page of the repository.
* Above the list of files, click  Code.
* Copy the URL for the repository.
* To clone the repository using HTTPS, under "HTTPS", click the clipboard icon for copying the URL.
* Open Terminal.
* Change the current working directory to the location where you want the cloned directory.
* Type git clone, and then paste the URL you copied earlier.
* $ git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY
* Press Enter to create your local clone.

<br>
<br>
<br>

# **VERSION CONTROL**

I used GITPOD for version control software. Regular git add ., git commit -m, and git push were used to add, save and push the code to the GITHUB Reop where the source code is stored.

<br>
<br>
<br>

# **CREDITS**

* I watched many youtube tutorials on hangman games but in particular **[Kiteco](https://www.youtube.com/watch?v=m4nEnsavl6w)**
* For adding color to the terminal I referenced an article on **[Geeks for Geeks](https://www.geeksforgeeks.org/print-colors-python-terminal/)**

<br>
<br>
<br>

# **ACKNOWLEDGEMENTS**

* Thanks as always to my Code Institute Mentor, Mitko Backvarov, for his support and encouragement.