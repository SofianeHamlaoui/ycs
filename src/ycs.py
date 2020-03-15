#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from sys import argv
import googleapiclient.discovery
#import json

#def get_authentication():
#    CLIENT_SECRETS_FILE = "client_secret.json"
#    SCOPE = ['https://www.googleapis.com/auth/youtube.force-ssl']
#    API_SERVICE_NAME = "youtube"
#    API_VERSION = "v3"
#    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS_FILE, SCOPE)
#    credentials = None
#    if os.path.exists('token.pickle'):
#        with open('token.pickle', 'rb') as token:
#            credentials = pickle.load(token)
#    #  Check if the credentials are invalid or do not exist
#    if not credentials or not credentials.valid:
#        # Check if the credentials have expired
#        if credentials and credentials.expired and credentials.refresh_token:
#            credentials.refresh(Request())
#        else:
#            flow = InstalledAppFlow.from_client_secrets_file(
#                CLIENT_SECRETS_FILE, SCOPE)
#            credentials = flow.run_console()
#        # Save the credentials for the next run
#        with open('token.pickle', 'wb') as token:
#            pickle.dump(credentials, token)
#    return build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
#
#get_authentication()

def extract_comments(video_id, youtube_api_key=None, max_response=0):
    threads = []
    comments =[]
    if youtube_api_key is None:
        print("""\033[0;31mYou have to give a Youtube Data API key")
            See how to get one there : 'https://www.youtube.com/watch?v=pP4zvduVAqo' \033[0m""")
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=youtube_api_key)

    request = youtube.commentThreads().list(
        part="replies,snippet",
        maxResults=100,
        textFormat="plainText",
        videoId=video_id
    ).execute()
    items = request['items']
    for item in request['items']:
        threads.append(item)
        comment = item["snippet"]["topLevelComment"]
        text = comment["snippet"]["textDisplay"]
        comments.append(text)
    return(comments)


def get_author(video_id, youtube_api_key=None, max_response=0):
    threads = []
    comments =[]
    authorDisplayName = []
    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=youtube_api_key)

    request = youtube.commentThreads().list(
        part="replies,snippet",
        maxResults=100,
        textFormat="plainText",
        videoId=video_id
    ).execute()
    items = request['items']
    for item in request['items']:
        threads.append(item)
        comment = item["snippet"]["topLevelComment"]
        text = comment["snippet"]["authorDisplayName"]
        authorDisplayName.append(text)
    return(authorDisplayName)

def get_api_from_file(file_name='./api.key'):
    if not os.path.isfile(file_name):
        if os.path.isfile('./api.key'):
            file_name = './api.key'
        elif os.path.isfile('./src/api.key'):
            file_name = './src/api.key'
        else:
            print("The file "+file_name+" can't be found.")
            print("Please check the location of the file to get the API Key")
            exit(1)

    file = open(file_name, 'r')
    return file.readline()[:-1]

if __name__ == "__main__":
    if(len(sys.argv) == 1):
        print("""
            \033[0;32mUsage : python3 ycs.py \033[1;33mYOUTUBE_URL\033[0m""")
        exit()
    api_key = get_api_from_file()
    vid_id = (" ".join(sys.argv[1:]).replace('https://www.youtube.com/watch?v=', '')).rstrip('\n')
    authorDisplayName = get_author(vid_id, api_key)
    comments = extract_comments(vid_id, api_key)
    resu = list(map(lambda x, y: "\033[1;33m"+x+"\033[0m" + ' commented : \033[0;34m' +y+"\033[0m\n", authorDisplayName, comments))
    #resu_si = list(map(lambda x, y: x+' commented : ' +y +'\n', authorDisplayName, comments))
    if(len(sys.argv) == 2):
        print(*resu, sep = "\n")
#    #print(json.dumps(comments, indent=4, sort_keys=True))
#    #print(str(len(comments)) + " Comments extracted.")