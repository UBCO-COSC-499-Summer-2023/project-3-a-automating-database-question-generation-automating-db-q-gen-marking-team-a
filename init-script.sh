#!/bin/bash

# Install Chrome dependencies
apt-get update && apt-get install -y --no-install-recommends wget ca-certificates

# Download and install Chrome
wget -q -O chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
dpkg -i chrome.deb
apt-get -f install -y
rm chrome.deb

# Start your application
# ...
