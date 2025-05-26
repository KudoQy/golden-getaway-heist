# Use an official PHP image from the Docker Hub
FROM php:8.0-apache

# Enable Apache rewrite module (if needed for your challenge)
RUN a2enmod rewrite

# Copy the current directory contents into the /var/www/html directory of the container
COPY . /var/www/html/

# Set the working directory inside the container
WORKDIR /var/www/html/

# Expose port 80 to allow HTTP traffic
EXPOSE 80
