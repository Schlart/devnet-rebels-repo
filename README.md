# GraphHopper Route Planner Web App

A Flask-based web application that provides route planning and turn-by-turn navigation using the GraphHopper API.

![Route Planner](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)
![License](https://img.shields.io/badge/license-MIT-orange.svg)

## Features

### Current Features ✅
- **Route Calculation**: Calculate routes between any two locations worldwide
- **Multiple Vehicle Types**: Support for car, bike, and foot routing
- **Turn-by-Turn Directions**: Detailed step-by-step navigation instructions
- **Distance & Duration**: Real-time calculation of trip distance and estimated travel time
- **Geocoding**: Automatic address-to-coordinates conversion
- **Map Integration**: Direct link to view routes on GraphHopper's interactive maps
- **Modern UI**: Clean, responsive web interface with gradient design
- **Real-time Feedback**: Loading indicators and error handling

### Planned Features 🚧
- **Route Alternatives**: Display multiple route options
- **Waypoint Support**: Add intermediate stops along the route
- **Route Export**: Export routes as GPX/KML files
- **Elevation Profile**: Show elevation changes along the route
- **Traffic Information**: Real-time traffic data integration
- **Route History**: Save and revisit previous routes
- **Custom Route Preferences**: Avoid highways, tolls, or ferries
- **Multi-language Support**: Interface translations
- **Dark Mode**: Toggle between light and dark themes
- **Route Sharing**: Share routes via URL

## Prerequisites

- Python 3.7 or higher
- GraphHopper API Key (free at [graphhopper.com](https://www.graphhopper.com/))

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Schlart/devnet-rebels-repo.git
cd devnet-rebels-repo
```

### 2. Create a Virtual Environment
```bash
python3 -m venv venv
```

### 3. Activate the Virtual Environment
**Linux/macOS:**
```bash
source venv/bin/activate
```

**Windows:**
```bash
venv\Scripts\activate
```

### 4. Install Dependencies
```bash
pip install flask requests
```

## Getting Your API Key

1. Visit [GraphHopper](https://www.graphhopper.com/)
2. Sign up for a free account
3. Navigate to your dashboard
4. Copy your API key from the credentials section
5. Free tier includes 500 requests per day

## Usage

### 1. Start the Application
```bash
python final.py
```

The server will start on `http://localhost:5000`

### 2. Access the Web Interface
Open your web browser and navigate to:
```
http://localhost:5000
```

Or access from another device on your network:
```
http://YOUR_IP_ADDRESS:5000
```

### 3. Plan Your Route
1. Enter your GraphHopper API key
2. Input your start location (e.g., "Berlin, Germany")
3. Input your end location (e.g., "Munich, Germany")
4. Select your vehicle type (car, bike, or foot)
5. Click "Calculate Route"
6. View detailed route information and turn-by-turn directions
7. (Optional) Click "View on GraphHopper Maps" to see the route visualized

## Project Structure
```
finalproj/
├── final.py              # Main Flask application
├── templates/
│   └── index.html        # Web interface
├── venv/                 # Virtual environment (not in repo)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## API Endpoints

### `GET /`
Serves the main web interface

### `POST /geocode`
Converts an address to coordinates
- **Request Body**: `{ "location": "string", "api_key": "string" }`
- **Response**: `{ "success": bool, "lat": float, "lng": float }`

### `POST /route`
Calculates route between two coordinates
- **Request Body**: 
```json
{
  "start_coords": {"lat": float, "lng": float},
  "end_coords": {"lat": float, "lng": float},
  "vehicle": "string",
  "api_key": "string"
}
```
- **Response**: Route details including distance, time, and instructions

## Troubleshooting

### Module Not Found Error
Make sure your virtual environment is activated:
```bash
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### Template Not Found Error
Ensure the `templates` folder exists and contains `index.html`

### API Key Issues
- Verify your API key is correct
- Check you haven't exceeded your daily request limit
- Ensure you're using a valid GraphHopper API key (not Google Maps, etc.)

### Port Already in Use
Change the port in `final.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Use different port
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- [GraphHopper](https://www.graphhopper.com/) for providing the routing API
- [Flask](https://flask.palletsprojects.com/) for the web framework

## Contact

For questions or issues, please open an issue on the GitHub repository.

---

**Note**: This is a educational project. For production use, consider implementing proper API key management, rate limiting, and error handling.