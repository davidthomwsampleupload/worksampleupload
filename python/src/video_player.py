"""A video player class."""

from src.video_library import VideoLibrary


class VideoPlayer:
    """A class used to represent a Video Player."""

    current = "none"
    pllst_counter = list()
    pauseyes = False

    def __init__(self):
        self._video_library = VideoLibrary()



    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""

        print("Here's a list of all available videos:")

        print(VideoLibrary.get_all_videos())

    def play_video(self, video_id):
        pauseyes = False
        if video_id in VideoLibrary.get_all_videos().url:
            position = VideoLibrary.get_all_videos().url.index(video_id)
            print("Stopping Video: ", current)
            current = VideoLibrary.get_all_videos().title[position]
            print("Playing video: ", VideoLibrary.get_all_videos().title[position])
        else:
            print("Cannot play video: Video does not exist")


    def stop_video(self):
        """Stops the current video."""
        if current in VideoLibrary.get_all_videos().title:
          print("Stopping video: ", current)
          current = "none"
        else:
          print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        """Plays a random video from the video library."""
        import random
        if current in VideoLibrary.get_all_videos().title:
            print("Stopping Video: ", current)
            randvid = random.choice(VideoLibrary.get_all_videos().title)
            current = randvid
            print("Playing video: ", randvid)


        else: randvid = random.choice(VideoLibrary.get_all_videos().title)
        current = randvid
        print("Playing video: ", randvid)


def pause_video(self):
        """Pauses the current video."""
        if current in VideoLibrary.get_all_videos().title:
          if pauseyes is True:
            print("Video already paused: ", current)
          else:
              pauseyes = True
              print("Pausing video: ", current)
        else:
          print("Cannot pause video: No video is currently playing")

def continue_video(self):
        """Resumes playing the current video."""
if current in VideoLibrary.get_all_videos().title:
    if pauseyes is True:
        pauseyes = False
        print("Continuing Video: ", current)
    else:
        print("Cannot continue video: Video is not paused")
else:
    Print("Cannot continue video: No video is currently playing")

    def show_playing(self):
        """Displays video currently playing."""
if current in VideoLibrary.get_all_videos().title:
    showpos = VideoLibrary.get_all_videos().title.index(current)
    if pauseyes is True:
      print("currently playing: ", current, "(", VideoLibrary.get_all_videos().url[showpos], ")", VideoLibrary.get_all_videos().tags[showpos] , "- PAUSED")
    else:
      print("currently playing: ", current, "(", VideoLibrary.get_all_videos().url[showpos], ")", VideoLibrary.get_all_videos().tags[showpos])
else:
  print("No video is currently playing")

def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """

        if playlist_name in pllst_counter:
            print("Cannot create playlist: A playlist with the same name already exists")
        else:
            playlist_name = list()
            pllst_counter.append(playlist_name)
            print("Successfully created new playlist: ", playlist_name)


def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        if playlist_name in pllst_counter:
            if video_id in VideoLibrary.get_all_videos().url:
                if video_id in playlist_name:
                    print("Cannot add video to ", playlist_name, ": Video already added")
                else:
                    playlist_name.append(VideoLibrary.get_all_videos().title[VideoLibrary.get_all_videos().url.index(video_id)])
                    print("Added video to ", playlist_name, ": ", VideoLibrary.get_all_videos().title[VideoLibrary.get_all_videos().url.index(video_id)])
            else:
                print("Cannot add video to ", playlist_name, ": Video does not exist")
        else:
            print("Cannot add playlist to ", playlist_name, ": Playlist does not exist")


def show_all_playlists(self):
        """Display all playlists."""
if len(pllst_counter) == 0:
    print("No playlists exist yet")
else:
    print("Showing all playlists")
    print(*pllst_counter, sep = "\n")


    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name in pllst_counter:
            if len(playlist_name) == 0:
                print("Showing playlist: ", playlist_name)
                print("No videos here yet")
            else:
                print("showing playlist: ", playlist_name)
                for x in playlist_name:
                    posx = VideoLibrary.get_all_videos().url.index(x)
                print(VideoLibrary.get_all_videos()[posx, ])
        else:
            print("Cannot show playlist ", playlist_name, ": playlist does not exist")



    def remove_from_playlist(self, playlist_name, video_id):
        vidnm = VideoLibrary.get_all_videos().title[VideoLibrary.get_all_videos().url.index(video_id)]
     if playlist_name not in pllst_counter:
         print("Cannot remove video from ", playlist_name, ": playlist does not exist")

     else:
         if video_id in VideoLibrary.get_all_videos().url:
           if vidnm in playlist_name:
             playlist_name.remove(vidnm)
             print("Removed video from ", playlist_name, ": ", vidnm)
           else:
             print("Cannot remove video from ", playlist_name, ": Video is not in playlist")
         else:
             print("Cannot remove video from ", playlist_name, ": Video does not exist")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name in pllst_counter:
            playlist_name = ()
            print("Successfully removed all videos from ", playlist_name)
        else:
            print("No playlist exists with name ", playlist_name)

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        if playlist_name not in pllst_counter:
            print("Cannot delete playlist ", playlist_name, ": Playlist does not exist")
        else:
            pllst_counter.remove(playlist_name)
            del playlist_name
        print("Deleted playlist: ", playlist_name)

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.
        Args:
            search_term: The query to be used in search.
        """

        results = list()
        for a in VideoLibrary.get_all_videos().title
          if search_term in VideoLibrary.get_all_videos().title[a]:
            results.append(VideoLibrary.get_all_videos()[a, ])
          else:
            results =  results

    order = results.title.sort()
    orderres = results
    x = len(results)
    for c in range(1, x):
        orderres[c, ] = results[results.title.index[order[c]], ]


    print("Here are the results for ", search_term)
    for b in range(1, x)
        print(b, orderres[b])

    feedbk = input("Would you like to play any of the above? If yes, specify the number of the video. If your answer is not a valid number, we will assume it's a no")
    if feedbk in range(1, x):
        current = orderres.title[feedbk]
        print("Playing video: ", orderres.title[feedbk])
    else:
        print("Invalid answer, no video will be played")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        resulttag = list()
        for d in VideoLibrary.get_all_videos().tags
            if search_term in VideoLibrary.get_all_videos().tags[d]:
                resulttag.append(VideoLibrary.get_all_videos()[d, ])
            else:
                resulttag = resulttag


    ordert = resulttag.title.sort()
    ordertag = resulttag
    y = len(resulttag)
    for e in range(1, y):
        ordertag[e,] = resulttag[resulttag.title.index[ordert[e]],]

    print("Here are the results for ", video_tag)
    for f in range(1, y)
        print(f, ordertag[f])

    feedbktg = input(
        "Would you like to play any of the above? If yes, specify the number of the video. If your answer is not a valid number, we will assume it's a no")
    if feedbktg in range(1, y):
        current = ordertag.title[feedbktg]
        print("Playing video: ", ordertag.title[feedbktg])
    else:
        print("Invalid answer, no video will be played")


    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
