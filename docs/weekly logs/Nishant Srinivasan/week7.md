# Week 7:
## Sunday , June 25:
- started on testing for renderer.js, worked on modularizing the code but seems like it's gonna be a bit more tricky than just moving the functions to a seperate file

## Monday , June 26:
- spent so many hours using so many approaches trying to make the renderer file testable but I don’t think it’s possible
- Moving them to a seperate file and importing them into the renderer to be used
- Keeping them there
- Using require.js
- Using webpack node module
- Using jdom jest
- Alternating between import/require syntax
- everything either throws issues in the terminal when testing or in the browser or both
- tried so many different combinations of these approaches and others but it’s just not working and it doesn’t seem worth it either

## Tuesday , June 27:
- tried testing element
- first had test file in the test folder and that didn’t work when I tried to import the module because the filename and it’s directory name use dashes instead of underscores which python doesn’t like so I messed with that but then that caused PL to crash and the only way to fix it was by renaming the folder name to what it was but I saw that the element file could still operate under a different name , which means the test file would have to be within the same directory as the element in order to avoid the import errors from before
- placed the test file in a new test folder inside the element folder but then that still started complaining about “relative import with no known parent package” and could only resolve it by moving the test file to the same directory as the element ; outside of the test folder
- then started getting issues with a bunch of different packages and had to pip install, as well as the PL module being used was through docker after we launch it, so in the IDE it was complaining about that and had to download that specific file from the PL repo and put it in here and then download even more modules for that to work
- in the end still kept getting errors from a bunch of different libraries, got MemoryErrors, got errors from the unittest module that I wasn’t getting before
- don’t think this is going to work either, testing shouldn’t take this much messing around just to setup

## Wednesday , June 28:
- met with team to talk mvp, ui opinions, what's next
- I will be working on testing the autogenerator, autograder, making the mvp slides, and taking on the backedn SQLite DB for autograding
- worked on ui testing for a bit, still running into chrome binary error on drone

## Thursday , June 29:
- worked on mvp powerpoint, basically done now, just a few loose ends to tie up
- visuals and all the necessary info gathered from going through what we've done so far

## Friday , June 30:
- worked on autogenerator testing, ran into so many issues with setting up the test file and just import/export stuff was such a pain
- got a few cases covered for the autogenerate function and both tests passing before leaving town for the weekend

## Saturday , July 1:
- autogenerate() function is basically done being tested - all cases covered
- looking into why tests can only run properly either from the terminal or from the file/vscode - very weird but want to fix it so it's easier for teammates AND works on drone
- made the tests for Auotgen function into one big paramterized test
- looking into ways to make the testing output results more visual and easier to keep track of for debugging
- setting up test file and going through coverage for all functions and organizing the file in accordance with that