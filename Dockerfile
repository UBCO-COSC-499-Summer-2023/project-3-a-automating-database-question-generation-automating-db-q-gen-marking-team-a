FROM prairielearn/prairielearn:latest

# Update the package lists and install dependencies
RUN yum update -y && \
    yum install -y wget && \
    wget https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
    yum localinstall -y google-chrome-stable_current_x86_64.rpm && \
    rm google-chrome-stable_current_x86_64.rpm

# Download and install the corresponding version of ChromeDriver
RUN wget -O /usr/bin/chromedriver https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip && \
    unzip /usr/bin/chromedriver -d /usr/bin/ && \
    chmod +x /usr/bin/chromedriver

# Set the PATH environment variable to include ChromeDriver
ENV PATH="/usr/bin:${PATH}"

# Continue with the existing commands and configuration for your application
# ...
