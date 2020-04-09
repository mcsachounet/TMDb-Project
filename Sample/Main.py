import requests
import sys
import csv
import numpy as np
from Dic import *
from Parameters import *

if not api_key:
    print("Please input an api_key...")

if genre1:
    try:
        genre1 = str(list(genres.keys())[list(genres.values()).index(genre1)])
    except:
        print("Oops!  Genre1 was no valid genre.  Try again...")
        sys.exit()
else :
    print("Please input at list 1 genre")

if genre2:
    try:
        genre2 = str(list(genres.keys())[list(genres.values()).index(genre2)])
    except:
        print("Oops!  Genre2 was no valid genre.  Try again...")
        sys.exit()
else : pass

if genre3:
    try:
        genre3 = str(list(genres.keys())[list(genres.values()).index(genre3)])
    except:
        print("Oops!  Genre3 was no valid genre.  Try again...")
        sys.exit()
else : pass


if original_language:
    try:
        original_language = str(list(iso_639_dic.keys())[list(iso_639_dic.values()).index(original_language)])
    except:
        print("Oops!  That was no a valid language.  Try again...")
        sys.exit()
else : pass

if 0 <= popularity <= 8:
    decile_number = popularity
else :
    decile_number = 8

def getAPIUrl(pages_number):
    url1 = 'https://api.themoviedb.org/3/discover/movie?api_key='
    url2 = '&sort_by=vote_average.desc&include_adult=false&include_video=false&page='
    url3 ='&primary_release_date.gte='
    url4 = '&primary_release_date.lte='
    url5 = '&vote_count.gte=100&with_genres='
    url6 ='&with_runtime.lte='
    url7 = '&with_original_language='
    url= url1+api_key+url2+pages_number+url3+lower_range_release+url4+upper_range_release+url5+genre1+','+genre2+','\
         +genre3+url6+runtime_max+url7+original_language
    return url

temp_json_data = requests.get(getAPIUrl('1')).json()

def getStatus_message():
    try:
        status_message= temp_json_data['status_message']
        return status_message
    except KeyError:
        return "Missing status_message in the response data"





if temp_json_data['total_results'] != 0:
    total_pages = temp_json_data['total_pages']
    total_of_results = temp_json_data['total_results']
else :
    print("0 movie are matching with the request")
    sys.exit()

Movies_Dic = {}
for i in range(1,total_pages+1):
    if len(Movies_Dic)>=100:
        break
    else:
        pass

    json_data = requests.get(getAPIUrl(str(i))).json()
    number_of_results = len(json_data['results'])
    print(number_of_results)

    for j in range(0, number_of_results-1):
        title=json_data['results'][j]['title']
        title=str(title)
        print(title)
        popularity=json_data['results'][j]['popularity']
        popularity=float(popularity)
        Movies_Dic.update({title: popularity})
        if len(Movies_Dic) >= 100:
            break
        else:
            pass

Popularity_List = list(Movies_Dic.values())
popularity_deciles = np.percentile(Popularity_List, np.arange(10, 100, 10)) # deciles
#print(popularity_deciles)
#print(len(popularity_deciles))
#print(popularity_deciles[decile_number])

if decile_number != 8:
    for key, value in dict(Movies_Dic).items():
            if value > popularity_deciles[decile_number]:
                del Movies_Dic[key]
else : pass

print(Movies_Dic)

with open(csv_filepath, "w", encoding='UTF8', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for key, value in dict(Movies_Dic).items():
        writer.writerow([key])







