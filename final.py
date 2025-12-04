from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/geocode', methods=['POST'])
def geocode():
    """Convert address to coordinates using GraphHopper Geocoding API"""
    data = request.json
    location = data.get('location')
    api_key = data.get('api_key')
    
    url = "https://graphhopper.com/api/1/geocode"
    params = {
        'q': location,
        'key': api_key,
        'limit': 1
    }
    
    try:
        response = requests.get(url, params=params)
        result = response.json()
        
        if 'hits' in result and len(result['hits']) > 0:
            point = result['hits'][0]['point']
            return jsonify({
                'success': True,
                'lat': point['lat'],
                'lng': point['lng']
            })
        else:
            return jsonify({
                'success': False,
                'error': f"Could not find location: {location}"
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/route', methods=['POST'])
def calculate_route():
    """Calculate route between two locations"""
    data = request.json
    start_coords = data.get('start_coords')
    end_coords = data.get('end_coords')
    vehicle = data.get('vehicle')
    api_key = data.get('api_key')
    
    url = "https://graphhopper.com/api/1/route"
    params = {
        'point': [
            f"{start_coords['lat']},{start_coords['lng']}", 
            f"{end_coords['lat']},{end_coords['lng']}"
        ],
        'vehicle': vehicle,
        'locale': 'en',
        'key': api_key,
        'instructions': 'true',
        'points_encoded': 'false'
    }
    
    try:
        response = requests.get(url, params=params)
        result = response.json()
        
        if 'paths' in result and len(result['paths']) > 0:
            path = result['paths'][0]
            distance = path['distance'] / 1000  # Convert to km
            time = path['time'] / 60000  # Convert to minutes
            
            instructions = []
            if 'instructions' in path:
                for instruction in path['instructions']:
                    instructions.append({
                        'text': instruction['text'],
                        'distance': instruction['distance']
                    })
            
            return jsonify({
                'success': True,
                'distance': round(distance, 2),
                'time': round(time, 0),
                'hours': round(time / 60, 1),
                'instructions': instructions,
                'map_url': f"https://graphhopper.com/maps/?point={start_coords['lat']},{start_coords['lng']}&point={end_coords['lat']},{end_coords['lng']}&vehicle={vehicle}"
            })
        else:
            error_msg = result.get('message', 'Unknown error occurred')
            return jsonify({
                'success': False,
                'error': f"Could not calculate route: {error_msg}"
            })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)