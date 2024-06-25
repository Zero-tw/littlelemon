# Introduction to Little Lemon API

Welcome to the Little Lemon API documentation! This API powers the backend for a restaurant management system, providing endpoints for managing menu items, bookings, user authentication, and more. Below, you'll find details on how to interact with the API, including authentication requirements and example endpoints.


## Getting Started

### Running Unit Tests

You can run unit tests from the terminal using the following command: 
- `python manage.py test tests/`


### Serving Static HTML Content

Use this path to verify that the web application serves static HTML content with images and styles. Additional functionality has been added to enhance the page usability.
- `/restaurant`
## API Documentation

### Authentication

Most endpoints require Token-based authentication. You'll need to include the token in the Authorization header as follows:
- `Authorization: token <your_token>`

### Endpoints

- **User Registration**: `POST /api/users/` - No authentication required.
  Use this endpoint to create a new user.

- **User Login**: Use the `/api/auth/token/login` endpoint to authenticate and obtain a token.

- **Menu Items**: 
  - List all menu items: `GET /api/menu-items/` - Authentication required.
  - Retrieve a specific menu item: `GET /api/menu-items/<id>/` - Authentication required.
  - Create a new menu item: `POST /api/menu-items/` - Authentication required.
  - Delete a menu item: `DELETE /api/menu-items/<id>/` - Authentication required.

- **Booking**:
  - List all bookings: `GET /api/bookings/` - Authentication required.
  - Retrieve a specific booking: `GET /api/bookings/<id>/` - Authentication required.
  - Create a new booking: `POST /api/bookings/` - Authentication required.
  - Delete a booking: `DELETE /api/bookings/<id>/` - Authentication required.

Explore these endpoints using tools like Insomnia, Postman, or your favorite web browser. Feel free to reach out if you have any questions.