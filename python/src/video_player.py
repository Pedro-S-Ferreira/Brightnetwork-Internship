"""A video player class."""

from .video_library import VideoLibrary
from random import randint



class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.playing = ""
        self.paused = False

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        print("Here's a list of all available videos:")

        for video in self._video_library.get_all_videos():
            temp_tags = "["
            for count, tag in enumerate(video.tags):
                temp_tags += str(tag)
                if not count == len(video.tags) - 1:
                    temp_tags += " "
            temp_tags += "]"

            print(str(video.title) + " (" + str(video.video_id) + ") " + temp_tags)

    def play_video(self, video_id):
        for video in self._video_library.get_all_videos(): #Checking if the video_id is valid
            if video_id == video.video_id:
                if self.playing:
                    print("Stopping video:", self.playing.title)
                print("Playing video:", video.title)
                self.playing = video
                return

        print("Cannot play video: Video does not exist")

    def stop_video(self):
        if self.playing:
            print("Stopping video:", self.playing.title)
            self.playing = ""
            self.paused = False
        else:
            print("Cannot stop video: No video is currently playing")

    def play_random_video(self):
        video_num = randint(0, 4)
        if self.playing:
            print("Stopping video:", self.playing.title)
        print("Playing video:", self._video_library.get_all_videos()[video_num].title)
        self.playing = self._video_library.get_all_videos()[video_num]

    def pause_video(self):
        if self.playing:
            if not self.paused:
                self.paused = True
                print("Pausing video:", self.playing.title)
            else:
                print("Video already paused:", self.playing.title)
        else:
            print("Cannot pause video: No video is currently playing")

    def continue_video(self):
        if self.playing:
            if self.paused:
                print("Continuing video:", self.playing.title)
                self.paused = False
            else:
                print("Cannot continue video: Video is not paused")
        else:
            print("Cannot continue video: No video is currently playing")


    def show_playing(self):
        if self.playing:

            temp_tags = "["
            for count, tag in enumerate(self.playing.tags):
                temp_tags += str(tag)
                if not count == len(self.playing.tags) - 1:
                    temp_tags += " "
            temp_tags += "]"
            final_string = ""
            final_string += self.playing.title + " (" + self.playing.video_id + ") " + temp_tags
            if not self.paused: 

                print("Currently playing:", final_string)
            else:
                print("Currently playing:", final_string, "- PAUSED")
        else:
            print("No video is currently playing")


    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

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
