# Wallpaper-Changer
Wallpaper Changer for Windows using the r/Wallpaper subreddit

YOU DO NOT NEED PYTHON TO RUN THIS PROGRAMM

If you own python you can download the non-compiled version from the "python" branch

If you want to compile it yourself you can download the code from the "code" branch

If you want a more compact version and don't need a UI you can download the program from the "noui_main" branch

This app uses the reddit api for Python.\
The reddit api has limits.\
The app already had a configured ".client" file with a throwaway client id and client secret so you don't have to create your own reddit app.\
If it is used to often it may be slow.\
If possible create a reddit app at https://ssl.reddit.com/prefs/apps/ on your reddit account and replace the default id and secret in the ".client" file with your own.



To do so:
<pre>
1. Click on "Create App" and fill in the blanks.
2. Select the "script" radio button.
    The "about url" is just information.
    The "redirect uri" isn't important and can be something like http://localhost.
Under the name of the app it should say "personal use script".
Underneath you should find your client id.
Put the client id in the first line of a file titled ".client" in the same directory as "Changer.exe".
You should find the client secret as "secret".
Put the client secret in the second line of the ".client" file.
You're good to go!
</pre>
