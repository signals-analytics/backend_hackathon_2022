import argparse
import logging

from src.fetcher.transcript_video_fetcher import fetch_transcript_by_id, write_transcripts_to_json
from src.processor.sentiment import run_sentiment_analysis
from src.publisher.sentiment_grapher import generate_sentiment_output_graph

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_url", required=True)
    parser.add_argument("--output_path", required=True)
    return parser.parse_args()


def parse_video_id(args):
    return args.video_url.split("=")[1]



if __name__ == "__main__":
    args = parse_args()
    logger.info('fetching transcript from video_url:' + args.video_url)
    video_id = parse_video_id(args)
    logger.info('Going to fetch transcripts for video_id:' + video_id)
    transcripts = fetch_transcript_by_id(video_id)
    logger.info('Going to write transcripts into json')
    json_files = write_transcripts_to_json(transcripts, args.output_path)
    sentiment_output_files = run_sentiment_analysis(json_files, args.output_path)
    logger.info("Going to generate output graph")
    generate_sentiment_output_graph(sentiment_output_files, args.output_path)
    logger.info('done')
