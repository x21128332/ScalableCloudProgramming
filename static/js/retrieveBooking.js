function retrieveBooking() {
    // Get the input value
    var bookingId = document.getElementById("booking_id").value;
    
    // Make an API request to retrieve the booking data
    fetch("https://apimaislingsbustours.azure-api.net/bt/bookings/" + bookingId)
      .then(response => {
        if (response.ok) {
          return response.json();
        } else {
          throw new Error("Could not retrieve booking data");
        }
      })
      .then(data => {
        // Update the table with the booking data
        var table = document.getElementById("bookingTable");
        table.innerHTML = `
          <tr>
            <td>${data.booking_id}</td>
            <td>${data.first_name}</td>
            <td>${data.origin}</td>
            <td>${data.destination}</td>
            <td>${data.departure_time}</td>
          </tr>
        `;
      })
      .catch(error => {
        // Display an error message
        var message = document.getElementById("errorMessage");
        message.textContent = error.message;
      });
  }