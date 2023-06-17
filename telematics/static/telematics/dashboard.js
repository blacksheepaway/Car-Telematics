$(document).ready(function() {
    axios.get('/api/cars/')
        .then(function(response) {
            var cars = response.data;
            var timestamps = [];
            var speeds = [];
            var rpms = [];
            var fuel_levels = [];
            var temperatures = [];
            for (var i = 0; i < cars.length; i++) {
                var car = cars[i];
                var row = '<tr>' +
                    '<td>' + car.vin + '</td>' +
                    '<td>' + car.make + '</td>' +
                    '<td>' + car.model + '</td>' +
                    '<td>' + car.year + '</td>' +
                    '<td>' + car.timestamp + '</td>' +
                    '<td>' + car.speed.toFixed(2) + ' km/h' + '</td>' +
                    '<td>' + car.rpm.toFixed(2) + '</td>' +
                    '<td>' + car.fuel_level.toFixed(2) + ' %' + '</td>' +
                    '<td>' + car.temperature.toFixed(2) + ' °C' + '</td>' +
                    '</tr>';
                $('#car-table').append(row);
                timestamps.push(car.timestamp);
                speeds.push(car.speed);
                rpms.push(car.rpm);
                fuel_levels.push(car.fuel_level);
                temperatures.push(car.temperature);
            }

            var data = [
                {
                    x: timestamps,
                    y: speeds,
                    mode: 'lines',
                    name: 'Speed'
                },
                {
                    x: timestamps,
                    y: rpms,
                    mode: 'lines',
                    name: 'RPM'
                },
                {
                    x: timestamps,
                    y: fuel_levels,
                    mode: 'lines',
                    name: 'Fuel Level'
                },
                {
                    x: timestamps,
                    y: temperatures,
                    mode: 'lines',
                    name: 'Temperature'
                }
            ];

            var layout = {
                title: 'Car Telematics Over Time',
                xaxis: {
                    title: 'Timestamp'
                },
                yaxis: {
                    title: 'Value'
                }
            };

            Plotly.newPlot('graph', data, layout);
        })
        .catch(function(error) {
            console.error(error);
        });
});
