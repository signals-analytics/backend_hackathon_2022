import argparse
import logging

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    import sys
    print(sys.argv)
    parser = argparse.ArgumentParser()
    parser.add_argument("--video_url", required=True)
    args = parser.parse_args()

    video_url = args.video_url
    video_id =  video_url.split("=")[1]

    logger.info('fetching transcript from video_url:' + video_url)
    logger.info('video_id:' + video_id)



    logger.info('done')
