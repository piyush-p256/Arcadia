from utils.cv_utils import detect_key_moments
from utils.audio_utils import generate_caption

# Main logic for fan-personalized highlights
def create_personalized_highlight(request):
    moments = detect_key_moments(request.match_id, request.preferences)
    captions = [generate_caption(m) for m in moments]
    return {
        "player_id": request.player_id,
        "highlight_clip": f"/clips/{request.match_id}_{request.player_id}.mp4",
        "captions": captions
    }