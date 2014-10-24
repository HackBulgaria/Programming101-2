# Music Library

We are going to make a music library program. __DONT FORGET TO USE TDD!__

## Song class
We need a song class with the following fields
- title
- artist 
- album
- rating
- length
- bitrate

You can rate different songs so every song must have a ``rate()`` function, that takes an integer between 0 and 5. If the value is different you must throw an error.

## Playlist class

The playlist class holds an collection of songs. You can name your palylists.

We will need the following functions for our playlist class.

### add_song(song)
This function takes only one argument. An instance of type song.

### remove_song(song_name)
This function takes only one argument that is the songs name. You have to find every song with this name and remove it from the playlist. 

### total_length()
This function takes no arguments. It sumes the lenght of all songs in the playlist.

### remove_disrated(rating)
This function takes one argument that is a number between 0 and 5. It removes all the songs that are below the given rating.

### remove_bad_quality()
It removes all the songs that are with a low bitrate.

### show_artists()
This function takes no arguments. It returns a list of all artists in the current playlist. __Artists must not duplicate!__

### __str__()
Redefine this function to return all songs with their artist and title and time.

__Example:__
```
ACDC Hells Bells - 05:09
ACDC Baby, Please Don't Go - 03:51
```

### save() and load() playlists
It is time to save our playlist on the file system. We are going to use json files for that.

Look at the python's documentation to see how python works with jsons: https://docs.python.org/3.3/library/json.html

__save(file_name)__ function takes only one argument. That is the file in witch we must write all the information for the current palylist.

__load(file_name)__ function takes one argument, too. That is the file from witch we must create a new playlist.

At the end of these two functions we should be able to save the state of our program on the hard drive.

## MusicCrawler
MusicCrower is class that makes playlists and songs from a real files on your file system. Every .mp3 and .ogg file have tags that describe it. Tags hold information about the title, artist, album etc. Our task is to craw a directory full of .mp3 or .ogg files and to make a new playlist from that directory by reading the file's tags.

__We recommend you this third party library for reading audio metadata.http://mutagen.readthedocs.org/en/latest/#__

Example:
```python
>>> a = MusicCrawler("/home/ivaylo/Music/")
>>> playlist = a.generate_playlist()
```

As you see the constructor takes only one argument that is the path of the directory from which you should read all the .mp3 files.

generate_playlist() function craws all the files and returns a new playlist full of songs.

## MusicPlayer
If you want to make this program usable you should implement an console interface for it. __You don't have to test this class!__ Implement this in the way you like it. Make it as user friendly as console can be. 

This class should only parse an user commands and call methods from the above classes.
