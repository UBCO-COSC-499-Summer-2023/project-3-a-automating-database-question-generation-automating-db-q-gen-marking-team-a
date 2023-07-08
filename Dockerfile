FROM prairielearn/prairielearn:latest

# Update the package lists and install necessary dependencies
RUN yum update -y && \
    yum install -y wget ca-certificates && \
    yum install -y libX11 fontconfig libXrender libXext cups-libs dbus-glib xorg-x11-server-Xvfb && \
    yum clean all

# Install Chrome
RUN wget -q -O /tmp/google-chrome-stable.rpm https://dl.google.com/linux/direct/google-chrome-stable_current_x86_64.rpm && \
    yum localinstall -y /tmp/google-chrome-stable.rpm && \
    rm /tmp/google-chrome-stable.rpm

# Install ChromeDriver
RUN wget -q -O /tmp/chromedriver_linux64.zip https://chromedriver.storage.googleapis.com/94.0.4606.61/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver_linux64.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver_linux64.zip && \
    chmod +x /usr/local/bin/chromedriver

# Add the ChromeDriver binary to the system path
ENV PATH="/usr/local/bin:${PATH}"














# code to run bash inside container
# winpty docker exec -it pl bash
# google-chrome-stable --version
# chromedriver --version