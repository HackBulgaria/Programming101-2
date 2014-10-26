# Music Library

We are going to make a music library program. __DONT FORGET TO USE TDD!__

## Song class
We need a song class with the following fields:
- title
- artist 
- album
- rating
- length
- bitrate

You can rate different songs so every song must have a ``rate()`` method, that takes an integer between 0 and 5. If the value is different you must throw an Exception.

## Playlist class

The playlist class holds a collection of songs. You can name your playlists.

We will need the following methods for our playlist class.

### add_song(song)
This method takes only one argument. An instance of class Song.

### remove_song(song_name)
This method takes only one argument that is the songs name. You have to find every song with this name and remove it from the playlist. 

### total_length()
This method takes no arguments. It sums the length of all songs in the playlist.

### remove_disrated(rating)
This method takes one argument - a number between 0 and 5. Then removes all the songs that are below the given rating.

### remove_bad_quality()
It removes all the songs that are with a low bitrate.

### show_artists()
This method takes no arguments. It returns a list of all artists in the current playlist. __Artists must not duplicate!__

### __str__()
Redefine this method to return all songs with their artist and title and time.

__Example:__
```
ACDC Hells Bells - 05:09
ACDC Baby, Please Don't Go - 03:51
```

### save() and load() playlists
It is time to save our playlist on the file system. We are going to use json files for that.

Look at the python's documentation to see how python works with jsons: https://docs.python.org/3.3/library/json.html

__save(filename)__ method takes only one argument - the filename where to export all the information from the current playlist.

__load(filename)__ method takes one argument - the filename from where to import all the information to the current playlist.

After implementing the above methods, we should be able to save the state of our program on the hard drive.

## MusicCrawler
Create a `MusicCrawler` class that creates playlists and songs objects from real files on your file system. Most of .mp3 and .ogg files have tags that describe them. Tags hold information about the title, artist, album etc. Our task is to crawl a directory full of .mp3 or .ogg files and create a new playlist by reading the files' tags.

__We recommend you [mutagen](http://mutagen.readthedocs.org/en/latest/#) to read audio metadata__

Example:
```python3
>>> crawler = MusicCrawler("/home/ivaylo/Music/")
>>> playlist = crawler.generate_playlist()
```

As you see, the constructor takes only one argument - the `path` of the directory from which you should read all the audio files.

`generate_playlist()` method craws all the files and returns a new playlist full of songs.

## MusicPlayer
If you want to make this program usable you should implement a console interface for it. __You don't have to test this class!__ Implement this in the way you like it. Make it as user friendly as a console can be. 

This class should only parse user commands and call methods from the above classes.
