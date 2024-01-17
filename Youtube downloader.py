#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system(' pip install pytube')


# In[5]:


import pytube

def download_youtube_video(link, resolution=None):
    """Downloads a YouTube video to a file in the specified resolution or the highest available."""

    try:
        yt = pytube.YouTube(link)

        # Get the appropriate stream
        stream = yt.streams.get_by_resolution(resolution) if resolution else yt.streams.get_highest_resolution()

        # Download the video to a file
        stream.download(output_path="\Desktop")  # Replace with your desired download path

        print("Download complete!")

    except Exception as e:
        print(f"Error downloading video: {e}")

# Example usage:
link = input("Enter the YouTube video link: ")
resolution = input("Enter the desired resolution (e.g., 720p) or leave blank for the highest: ")
download_youtube_video(link, resolution)


# In[ ]:




