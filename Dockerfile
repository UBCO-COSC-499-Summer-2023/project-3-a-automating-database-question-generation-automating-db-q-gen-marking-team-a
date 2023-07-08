FROM prairielearn/prairielearn:latest

# Update the package lists and install dependencies
RUN yum update -y && \
    yum install -y wget && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
    yum localinstall -y google-chrome-stable_current_x86_64.rpm && \
    rm google-chrome-stable_current_x86_64.rpm

# Copy the ChromeDriver binary to the appropriate location
COPY chromedriver/chromedriver /usr/bin/chromedriver

# Set executable permissions for ChromeDriver
RUN chmod +x /usr/bin/chromedriver

# Continue with the existing commands and configuration for your application
# ...












# code to run bash inside container
# winpty docker exec -it pl bash
# google-chrome-stable --version
# chromedriver --version