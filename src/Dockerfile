
FROM python:3.10-slim
ENV DEBIAN_FRONTEND=noninteractive

# Install dependencies
RUN apt-get update && \
    apt-get install -y wget gnupg2 unzip curl && \
    apt-get install -y xvfb libxi6 libgconf-2-4 libss3 libglib2.0-0 libfontconfig1
    && rm -rf var/lib/apt/lists/*

# Install Chrome
RUN curl -sSL https://dl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    echo "deb http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google.list && \
    apt-get update && \
    apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN CHROME_DRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
    wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_DRIVER_VERSION/chromedriver_linux64.zip && \
    unzip /tmp/chromedriver.zip -d /usr/local/bin/ && \
    rm /tmp/chromedriver.zip

ENV DISPLAY=:99

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt --no-cache-dir

CMD ["python", "your_test_script.py"]
