import json
import logging
import os
import time

from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import Formatter
from youtube_transcript_api.formatters import JSONFormatter
from youtube_transcript_api.formatters import TextFormatter
from youtube_transcript_api.formatters import WebVTTFormatter
logger = logging.getLogger()

def fetch_transcript_by_id(video_id):
    # retrieve the available transcripts
    return YouTubeTranscriptApi.list_transcripts(video_id)

def write_transcripts_to_json(transcript_list, output_path):
    # return list of json filenames (full path)
    json_output_path = os.path.join(output_path, "json_input_for_sentiment",  str(time.time()))
    os.makedirs(json_output_path)
    logger.info("Going to write json for sentiment analysis input in path:  " + json_output_path)
    return [write_to_json_file1(transcript.video_id, transcript.fetch(), output_path) for transcript in transcript_list]

def write_to_json_file(video_id):
    # Must be a single transcript.
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    formatter = JSONFormatter()

    # .format_transcript(transcript) turns the transcript into a JSON string.
    json_formatted = formatter.format_transcript(transcript)

    # Now we can write it out to a file.
    with open('transcript_video_' + video_id + '.json', 'w', encoding='utf-8') as json_file:
        json_file.write(json_formatted)
    # Now should have a new JSON file that you can easily read back into Python.


def write_to_json_file1(video_id, transcript, output_path):
    formatter = JSONFormatter()

    # .format_transcript(transcript) turns the transcript into a JSON string.
    json_formatted = formatter.format_transcript(transcript)
    json_transcript = json.loads(json_formatted)
    # arr_json = {str(t['start']): {'Content': t['text']} for t in json_transcript}
    arr_json = {str(t['start']): {'Content': t['text'], 'Sentiment': ''} for t in json_transcript}

    # Now we can write it out to a file.
    merged_json_filename = output_path + '/' + video_id + '.json'

    with open(merged_json_filename, 'w', encoding='utf-8') as json_file:
        json_file.write(json.dumps(arr_json))
    # Now should have a new JSON file that you can easily read back into Python.
    logging.info("json file: " + merged_json_filename)
    return merged_json_filename

def print_transcript(srt):
    text_list = []
    for i in srt:
        text_list.append(i['text'])

    text = ' '.join(text_list)
    print(text)

def appeand_all_transcript_text(srt):
    text_list = []
    for i in srt:
        text_list.append(i['text'])

    text = ' '.join(text_list)
    return text

def print_all_transcripts(video_ids):
    transcript_list, unretrievable_videos = YouTubeTranscriptApi.get_transcripts(video_ids, continue_after_error=True)
    for video_id in video_ids:
        write_to_json_file(video_id)
        if video_id in transcript_list.keys():
            print("\nvideo_id = ", video_id)

            srt = transcript_list.get(video_id)
            print_transcript(srt)


def write_transcript_to_json(video_id):
    print("\nvideo_id = ", video_id)
    srt = YouTubeTranscriptApi.get_transcript(video_id)
    write_to_json_file1(video_id, srt)


videoListName = "youtubeVideoIDlist.txt"

with open(videoListName) as f:
    video_ids = f.read().splitlines()
    print_all_transcripts(video_ids)