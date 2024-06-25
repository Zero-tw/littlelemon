# I decided to leave te code of the fron-end and models in restaurant and the api in littlelemonAPI.

You can run  unittests from terminal using: python manage.py test tests/

# This path can be used to check that web application serves static HTML content with images and styles. I also added some code to make the page fuctional.
/restaurant

You can use the following API paths for testing purposes using Insomnia or Postman clients
OR just browse using your favorite browser. To access most endpoints, you need to authenticate using Token-based authentication

# JDOSER endpoint, for example, to make POST request and create new user
/api/users/ 

# to login using JDOSER endpoint
/api/auth/token/login 

# Menu items
/api/menu-items/
/api/menu-items/{menuItemId}/

# Booking 
/api/booking/
/api/booking/{bookingId}
