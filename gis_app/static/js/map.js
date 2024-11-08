document.addEventListener('DOMContentLoaded', function() {
    // Initialize the map and set the view to default coordinates
    var map = L.map('map').setView([51.505, -0.09], 13);

    // Add OpenStreetMap tile layer
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Get the API URL from the data attribute in the HTML
    var apiPointsUrl = document.getElementById('mapContainer').getAttribute('data-point-url');
    var apiLinesUrl = document.getElementById('mapContainer').getAttribute('data-lines-url');
    var apiPolygonsUrl = document.getElementById('mapContainer').getAttribute('data-polygons-url');

    var markers = [];

    // Retrieve JWT token from localStorage
    // var jwtToken = localStorage.getItem('jwtToken'); // Ensure this is set after login

    var jwtToken = ''
    // Helper function to add JWT to request headers
    function getHeaders() {
        return {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${jwtToken}`
        };
    }

    console.log('Headers:', getHeaders());


    // Fetch points from API and add them to the map
    function fetchPoints(query = '') {
        let url = apiPointsUrl;
        if (query) {
            url += `?search=${query}`;
        }

        fetch(url, {
            headers: getHeaders()
        })
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                clearMarkers();
                addPointsToMap(data);

                // Check localStorage for last updated point
                const lastUpdatedId = localStorage.getItem('lastUpdatedPointId');

                let targetPoint;
                if (lastUpdatedId) {
                    // Find the point with the stored ID in the fetched data
                    targetPoint = data.find(point => point.structure_id === parseInt(lastUpdatedId));
                }

                // If we have a target point, center on it; otherwise, default to first point
                if (targetPoint) {
                    var coordinates = extractCoordinates(targetPoint.geom);
                    map.setView([coordinates.lat, coordinates.lng], 16);
                } else {
                    var firstPoint = data[0];
                    var coordinates = extractCoordinates(firstPoint.geom);
                    map.setView([coordinates.lat, coordinates.lng], 16);
                }
            } else {
                alert("Point not available");
            }
        });
    }

    // Helper function to extract latitude and longitude from WKT (POINT format)
    function extractCoordinates(geom) {
        var coordinates = geom.match(/POINT \(([^)]+)\)/)[1].split(" ");
        return {
            lng: parseFloat(coordinates[0]),
            lat: parseFloat(coordinates[1])
        };
    }
    
    // Generate popup content with Edit and Delete buttons
    function getPopupContent(pointName, pointId) {
        return `
            <div>
                <strong>${pointName}</strong><br>
                <button id="editBtn-${pointId}" class="popup-btn">Edit</button>
                <button id="deleteBtn-${pointId}" class="popup-btn">Delete</button>
            </div>
        `;
    }

    // Add points to map with markers and tooltips with Edit/Delete buttons
    function addPointsToMap(points) {
        points.forEach(point => {
            var coordinates = extractCoordinates(point.geom);
            var marker = L.marker([coordinates.lat, coordinates.lng])
                .addTo(map)
                .bindPopup(getPopupContent(point.structure_name, point.structure_id));

            markers.push(marker);

            // Event listener for when the marker is clicked
            marker.on('popupopen', function() {
                // Add event listener for Edit button
                document.getElementById(`editBtn-${point.structure_id}`).addEventListener('click', function() {
                    openEditForm(marker, point);
                });

                // Add event listener for Delete button
                document.getElementById(`deleteBtn-${point.structure_id}`).addEventListener('click', function() {
                    deletePoint(point.structure_id);
                });
            });
        });
    }

    // Open a small form for editing just below the clicked marker
    function openEditForm(marker, point) {
        const form = document.getElementById('smallEditForm');
        const input = document.getElementById('smallEditInput');
        
        // Set the input value to current point name
        input.value = point.structure_name;

        // Get the pixel position of the marker and position the form accordingly
        const markerLatLng = marker.getLatLng();
        const markerPoint = map.latLngToContainerPoint(markerLatLng);
        form.style.left = `${markerPoint.x - form.offsetWidth / 2}px`;  // Center horizontally
        form.style.top = `${markerPoint.y + 20}px`;  // Place just below the marker

        // Show the form
        form.style.display = 'block';

        // Add an event listener for saving the changes
        document.getElementById('smallSaveEdit').onclick = function() {
            const newName = input.value;

            // Use the original location coordinates from the point object
            const updatedLocation = point.geom;

            fetch(apiPointsUrl.replace(/\/$/, '') + '/' + point.structure_id + '/', {
                method: 'PUT',
                headers: getHeaders(),
                body: JSON.stringify({
                    name: newName,          
                    geom: updatedLocation  
                })
            })
            .then(response => {
                if (response.ok) {
                    // Store the updated point ID in localStorage
                    localStorage.setItem('lastUpdatedPointId', point.structure_id);
                    fetchPoints();  // Refresh points on the map
                    form.style.display = 'none';  // Hide the form after saving
                } else {
                    return response.json().then(errorData => {
                        console.error("Error:", errorData);
                        alert("Failed to update the point: " + (errorData.geom || errorData.name).join(", "));
                    });
                }
            });
        };

        // Add an event listener to close the form when the cancel button is clicked
        document.getElementById('smallCancelEdit').onclick = function() {
            form.style.display = 'none';
        };
    }

    // Delete the point
    function deletePoint(pointId) {
        if (confirm('Are you sure you want to delete this point?')) {
            fetch(apiPointsUrl.replace(/\/$/, '') + '/' + pointId + '/', {
                method: 'DELETE',
                headers: getHeaders()
            }).then(response => {
                if (response.ok) {
                    fetchPoints();
                }
            });
        }
    }

    // Clear all existing markers from the map
    function clearMarkers() {
        markers.forEach(marker => map.removeLayer(marker));
        markers = [];
    }

    // Handle adding a new point by clicking on the map
    var selectedLatLng = null;
    document.getElementById('addPointBtn').addEventListener('click', function() {
        alert('Click on the map to select point location');
        map.on('click', onMapClick);
    });

    function onMapClick(e) {
        selectedLatLng = e.latlng;
        document.getElementById('form').style.display = 'block';
        map.off('click', onMapClick);
    }

    // Save the new point via POST request
    document.getElementById('savePoint').addEventListener('click', function() {
        var pointName = document.getElementById('name').value;

        if (pointName && selectedLatLng) {
            fetch(apiPointsUrl, {
                method: 'POST',
                headers: getHeaders(),
                body: JSON.stringify({
                    name: pointName,
                    geom: {
                        x: selectedLatLng.lng,
                        y: selectedLatLng.lat
                    }
                })
            })
            .then(response => response.json())
            .then(data => {
                localStorage.setItem('lastUpdatedPointId', data.structure_id);
                fetchPoints();
                document.getElementById('form').style.display = 'none';
                selectedLatLng = null;
                document.getElementById('name').value = '';
            });
        }
    });

    // Initial load of points
    fetchPoints();

    // Cancel adding a point
    document.getElementById('cancel').addEventListener('click', function() {
        document.getElementById('form').style.display = 'none';
        selectedLatLng = null;
    });

    // Search functionality
    document.getElementById('searchButton').addEventListener('click', function() {
        var searchQuery = document.getElementById('searchInput').value;
        if (searchQuery) {
            fetchPoints(searchQuery);
        }
    });
});
