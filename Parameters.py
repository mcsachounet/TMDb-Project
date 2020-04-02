api_key = 'your_api_key'  #please input a valid imdb api-key

lower_range_release = '1950-01-01'            # format date : YYYY-MM-DD ;
upper_range_release = '2020-03-26'            # format date : YYYY-MM-DD

genre1= 'Drama'                        # Input  genres : "Action"  "Adventure" "Animation" "Comedy" "Crime" "Documentary"
genre2 = 'Comedy'                       #"Drama" "Family" "Fantasy" "History" "Horror" "Music" "Mystery" "Romance"
genre3 = ''                            #"Science Fiction" "TV Movie""Thriller" "War" "Western"

runtime_max=''                          # number in minutes

original_language = 'French'            # input a valid language (with the first letter in uppercase : for
                                        # exemple 'Japanese'

popularity = 4                          #input a popularity from 0 to 8 (0 will select all the less popular
                                        # movie(s) from the list ; 8 will select all the more popular one(s)
                                        #from the list

csv_filepath = "D:\Desktop\Movie\\mymoviefiles.csv"  #input the destination file
                                                     #do not forget to put a \\ before the final file
                                                     # example : D:\Desktop\Movie\\mymoviefiles.csv

