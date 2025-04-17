
def generate_feedback(data):
    # Analyze events
    decisions = data.events[:5]  # mock logic
    tips = [f"On event {i['type']}, try repositioning." for i in decisions]
    return {"player_id": data.player_id, "feedback": tips}