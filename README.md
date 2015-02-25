Europa Universalis 4™ multiplayer timesaver
===========================================

> Are you fucking tired to wait an entire geological age before downloading the savegame of an existing Europa Universalis 4 game? **I was**. So I decided to use the power of DropBox™ to help the host sharing the compressed savegames with the clients. **Automatically**.

This simple tool aims to resolve the problem that every unlucky player that has a shitty internet connection will find playing this wonderful game: **the startup time**.

Using a shared directory on DropBox™ the savegame is shared between the players by the host without have to rely on the host upload bandwith.

Note that apparently without any reason Europa Universalis 4™ upload the expanded state of the game instead of the compressed one. Using this tool you can just use the compressed savegame and you are automatically synced with the game.

Both the host and the clients have to use the fucking-time-saver.py script. The host will specify his savegame folder as the source and the DropBox™ shared folder as the destination. The clients will specify the DropBox™ shared folder as the source and the savegame folder as the destination.

Host and clients have to choose a pattern to use for the savegame file names: good examples are *shared_\*.eu4* and *autosave\*.eu4* that will share all the savegames with *shared_* as the first part of the name and all the autosaves.

Usage
-----

    usage: fucking-time-saver.py [-h] SOURCE DESTINATION PATTERN [PATTERN ...]

    Synchronyzes Europa Universalis 4™ multiplayer savegames in local directories
    using the DropBox™

    positional arguments:
      SOURCE       the source directory to monitorize
      DESTINATION  the directory in which savegames should be copied
      PATTERN      file patterns to be monitored (ie. shared_*.eu4)

    optional arguments:
      -h, --help   show this help message and exit

TODO:
-----
 * Add decent usage documentation
 * Add installation documentation
 * Add [PyInstaller](https://github.com/pyinstaller/pyinstaller/wiki)-powered binary version for the **poor Windows™ users** that does not have neither python or pip
 * **Play Europa Universalis 4™ for thousands of hours**
