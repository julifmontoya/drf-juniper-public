
# Juniper Api Soap Integration

## 1. Definition
The objective of this project is to demonstrate how the JP API from Juniper was developed and integrated. The API technology is based on SOAP, and a backend was developed to transform the requests into JSON format. Due to the complexity of the integration, large sections of the code have been removed. In the evidence folder, JSON requests and responses can be found, as well as images that document the development process. Unfortunately, it is not possible to provide the complete code for free.

## 2. Project Goal
This project involves integrating a SOAP-based API from Juniper into a backend system, with the primary objective of facilitating hotel-related operations through various endpoints. It includes a static mapping process for the hotel portfolio and a dynamic flow for booking operations. Designing a database to store hotel codes alongside their respective cities is crucial for efficient retrieval and management of hotel data

## 3. Technologies Used
The integration uses the following technologies:
- Python Django Rest Framework (DRF): For building the backend API.
- requests library: For making HTTP requests.
- xmltodict: For converting XML responses from the SOAP API into JSON format.

## 4. Technical Details
### SOAP to REST Conversion:
- Utilize the requests library to send SOAP requests to the Juniper API.
- Convert SOAP XML responses to JSON using xmltodict.
- Structure responses to match the expected format for the Django Rest Framework.

### Database Design:
- Design tables to store hotel codes, cities, and related data.
- Optimize for quick lookup and efficient data management.

### Static Mapping Process:
- Map hotel portfolio data to the database.
- Ensure data consistency and integrity through validation checks.

### Dynamic Booking Flow:
- Implement booking rules and availability checks.
- Handle booking requests, cancellations, and booking status updates.

## 5. Endpoints
### Retrieval and save all available hotel codes:
v1/hotel-portfolio/

### Checks hotel availability:
v1/hotel-availability

### Validate the combination in order to complete the booking flow process:
v1/hotel-bookingrules/

### Booking confirmation request:
v1/hotel-booking/

### Cancels bookings:
v1/hotel-cancelbooking

### Reads booking details:
v1/hotel-readbooking/

### Lists all bookings:
v1/hotel-bookinglist/

## 4. References
Link from JP API
https://api-edocs.ejuniper.com/en/api/jp/hotel-api