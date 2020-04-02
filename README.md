# TMDb-Project
Just a small piece of code (from an autodidact) in order to get a list of movies from TMDb depending on some string parameters you will pick (language, release date, genres, popularity).

I am using the discover request from TMDb API. This is more “friendly” than the API because you do not have to input ID filters (language,
genre) but “real life  parameters”.

# Example
Here’s an example that shows how to use the code:

First, you will need to get a TMDb API key. You can request one after registering your account on TMDb. (it will takes literally 2 minutes) https://developers.themoviedb.org/3/getting-started/introduction

After you get your API Key, you are all set! If you want to watch a North Korean horror movie tonight, but you want it relatively short, not too old, and not very popular, here is what you can input in the Sample/Parameters.py 

![Image description](https://github.com/mcsachounet/TMDb-Project/blob/master/INPUT.JPG)

You can now run the Sample/Main.py (do not forget to install the requirements).

As an output, you will have a csv spreadsheet (under your csv_filepath) with all the matching movies classifying from the best to the worst rating:

![Image description](https://github.com/mcsachounet/TMDb-Project/blob/master/OUTPUT.JPG)




