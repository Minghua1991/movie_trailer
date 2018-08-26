# [Demo](https://m-zheng.github.io/movie_trailer/)


# About

This project provides a server-side script to store a list of movies, incluing movie title, poster image URL, movie trailer URL, release year, description and watch URL.
All information can be fetched from a csv file which provides an easy way to manage all movie data.

# How to run


 * Step 1: Download the repo.
 * Step 2: Unzip the repo if it's a zip file. 
 * Step 3 (optional for linux user):  
      * Open movie_trailer.py.
      * In line 217, change the first parameter of open method to the path where you want to save the html file, repo path is suggested. Such as '/home/ubuntu/workspace/movie_trailer/index.html'.
      * In line 263, change argument of the get_all_movie_data method to the 'all_movie_data.csv' file path, don't forget to add file extension. Such as '/home/ubuntu/workspace/movie_trailer/all_movie_data.csv'.
      * Save the changes in movie_trailer.py file.
 * Step 4: Run movie_trailer.py file, then the webpage will pop up automatically (Only available for python 2.7.6).


