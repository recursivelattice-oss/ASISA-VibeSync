import requests
import json
import math

# Local API Configuration
API_URL = "https://127-0-0-1.lovense.club:30010/command"

def calculate_twist_intensity(m1, m2, distance, res1, res2):
    """
    Applies Infinite Finite Twist logic:
    Standard gravity pulls, but at 1e-9 resonance duality triggers repulsion.
    """
    G = 6.67430e-11
    threshold = 1e-9
    
    # Calculate force based on your physics formula
    force_magnitude = (G * m1 * m2 / pow(distance, 3)) * abs(res1 * res2)
    
    # Map force to a scale of 0-20 for hardware intensity
    intensity = min(int(force_magnitude * 1e12), 20) 
    return intensity

def send_sync_command(intensity):
    payload = {
        "command": "Function",
        "action": f"Vibrate:{intensity}",
        "timeSec": 0,
        "apiVer": 1
    }
    try:
        response = requests.post(API_URL, json=payload, timeout=2)
        return response.json()
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    current_intensity = calculate_twist_intensity(m1=1.0, m2=1.0, distance=1e-9, res1=0.8, res2=0.9)
    print(f"Twist Triggered! Force Intensity: {current_intensity}")
    send_sync_command(current_intensity)
