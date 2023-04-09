FROM python:3.11

RUN apt update \
    && apt install -y --no-install-recommends \
    dpkg-dev usbutils libnfc-dev udev \
    && apt autoremove -y && apt-get clean && rm -rf /var/cache/apt/archives/* /var/lib/apt/lists/*

RUN  sh -c 'echo ACTION==\"add\", ATTRS{idVendor}==\"${VENDOR}\", ATTRS{idProduct}==\"${PRODUCT}\", GROUP=\"plugdev\" >> /etc/udev/rules.d/nfcdev.rules'

RUN pip install poetry && \
    poetry config --local virtualenvs.create true && \
    poetry config --local cache-dir .cache/pypoetry && \
    poetry config --local virtualenvs.in-project true

RUN apt update && \
    apt install -y wget unzip fontconfig && \
    mkdir /usr/share/fonts/googlefonts && \
    cd /usr/share/fonts/googlefonts && \
    wget https://github.com/google/fonts/archive/main.zip && \
    unzip main.zip && \
    cd fonts-main && \
    find . -name "*.ttf" -exec install -m644 {} /usr/share/fonts/googlefonts/ \; && \
    cd .. && \
    rm -rf main.zip fonts-main && \
    fc-cache -fv

WORKDIR /app
ENV PATH=/app/.venv/bin:$PATH