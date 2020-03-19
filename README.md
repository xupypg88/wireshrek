# WireShrek
Small tool/Sublime plugin that should help to go though the Veeam log easier
Firstly, no warranty, just a free useful tool.
Second, usage and feeback appreciated
Thirdly, any issues are reviewed only here in the Issues section, no other way for communication in regards to features or bugs
(Sorry, may be different in future)

Enjoy! :)

The project will have a package section or the installer-like feature but not now.
This baby should be carried manually to your machine and installed. Later I will add more ellegant method.
Thanks for understanding!

Installation:
1. Download the Project as Zip file to your system (This page -> Top Right -> Clone or Download -> Download ZIP)
2. Open Sublime and if you did not install any plugin before then go to Tools -> Install package control
3. In the Sublime window, when the other desirable packages are installed, pls go to the:
Preference -> Package control -> Browse Packages
4. Unzip the WireShrek folder and put the folder as is in the Packages folder you opened on the previous step.
The folder name should remain WireShrek

Restart the Sublime may be necessary.

You can simply check if it went fine by right-clicking on the log - there should be one more point in the context menu - WireShrek

# Released:
- Find to tab
The feature finds al the selected (even multiple) parts in the file and places all identical entried into a new tab. (Find all analog but economizes time)
- Put to tab
The feature cpoies the selection and places the one and all the following selections into a single tab called "dumper".
In addition, it separates all entries and adds the file path where from it was copied. Helps out when you need to put  several fragments into a single file for escalation for example or whatever.
- Close 
The feature closes even unsaved file without disturbing you with a question if you want to save it. Cancels all modifications of the file. Shortcut: Ctrl + Shift + X

# Coming
- I am SOBeR
The feature should gether information from the VMC log for the date of this log where you right-clicked.
It should show: extents and its names/IPs, numer of cores and RAM if possible, concurrent tasks, object storage.
If it will fire well, I will add the notification about obvious incorrect concurrent task setup + job IDs (names in future) that are targeted to the SOBR(s)

