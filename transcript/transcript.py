import json
from youtube_transcript_api import YouTubeTranscriptApi
import datetime

def get_transcript(video_id):
    """
    Fetch transcript with timestamp, message, start, and end times for a given YouTube video ID
    and save it to a JSON file.
    """
    try:
        # Fetch the transcript for the provided video_id
        transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Initialize a list to store the transcript with start, end, and message
        transcript_data = []
        
        for i, transcript in enumerate(transcript_list):
            # Convert start timestamp (in seconds) to HH:MM:SS format
            start_time = transcript['start']
            timestamp = str(datetime.timedelta(seconds=int(start_time)))
            text = transcript['text']
            
            # Estimate the end time as the start time of the next transcript entry, if available
            if i + 1 < len(transcript_list):
                end_time = transcript_list[i + 1]['start']
            else:
                # If it's the last message, assume a default duration (e.g., 2 seconds)
                end_time = start_time + 2
            
            # Append transcript entry with start, end, and message
            transcript_data.append({
                "timestamp": timestamp,
                "start": start_time,
                "end": end_time,
                "text": text
            })
        
        # Save the transcript data to a JSON file
        output_filename = f"{video_id}_transcript.json"
        with open(output_filename, "w", encoding="utf-8") as json_file:
            json.dump(transcript_data, json_file, indent=4)
        
        print(f"Transcript successfully saved to {output_filename}")
    
    except Exception as e:
        print(f"Error fetching transcript: {e}")

if __name__ == "__main__":
    # Replace this with the video ID you want to fetch the transcript for
    video_id = "VAGZGQg31hs"
    get_transcript(video_id)





# import json
# from youtube_transcript_api import YouTubeTranscriptApi
# import datetime

# def get_transcript(video_id):
#     """
#     Fetch transcript with timestamp and message for a given YouTube video ID
#     and save it to a JSON file.
#     """
#     try:
#         # Fetch the transcript for the provided video_id
#         transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
        
#         # Initialize a list to store the transcript with timestamp
#         transcript_data = []
        
#         for transcript in transcript_list:
#             # Convert timestamp (start in seconds) to HH:MM:SS format
#             timestamp = str(datetime.timedelta(seconds=int(transcript['start'])))
#             text = transcript['text']
            
#             # Append transcript entry to the list
#             transcript_data.append({
#                 "timestamp": timestamp,
#                 "message": text
#             })
        
#         # Save the transcript data to a JSON file
#         output_filename = f"{video_id}_transcript.json"
#         with open(output_filename, "w", encoding="utf-8") as json_file:
#             json.dump(transcript_data, json_file, indent=4)
        
#         print(f"Transcript successfully saved to {output_filename}")
    
#     except Exception as e:
#         print(f"Error fetching transcript: {e}")

# if __name__ == "__main__":
#     # Replace this with the video ID you want to fetch the transcript for
#     video_id = "lYSfGuig0Jk"
#     get_transcript(video_id)
