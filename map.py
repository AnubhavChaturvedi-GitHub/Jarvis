import googlemaps

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
api_key = 'YOUR_API_KEY'
gmaps = googlemaps.Client(key=api_key)


def geocode_address(address):
    try:
        # Geocode the address to get its coordinates
        geocode_result = gmaps.geocode(address)

        # Extract the latitude and longitude from the result
        location = geocode_result[0]['geometry']['location']
        lat, lng = location['lat'], location['lng']

        return lat, lng

    except Exception as e:
        print(f"Error geocoding address: {e}")
        return None


if __name__ == "__main__":
    # Example: Geocode the address "1600 Amphitheatre Parkway, Mountain View, CA"
    address_to_geocode = "1600 Amphitheatre Parkway, Mountain View, CA"

    coordinates = geocode_address(address_to_geocode)

    if coordinates:
        print(f"Coordinates for {address_to_geocode}: Latitude={coordinates[0]}, Longitude={coordinates[1]}")
    else:
        print("Geocoding failed.")
