import argparse
import logging

from src.fetcher.transcript_video_fetcher import fetch_transcript_by_id, write_transcripts_to_json, merge_transcripts

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
    logger.info('Going to merge transcripts into json')
    merged_transcripts = merge_transcripts(transcripts)
    # write_transcripts_to_json(transcripts, args.output_path)
    logger.info('done')
