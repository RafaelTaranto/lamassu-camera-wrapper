# Preliminaries for Ubuntu 16.04
Installation for other distros may be slightly different.

## Packages

```
sudo add-apt-repository ppa:ubuntu-toolchain-r/test
sudo apt-get update
sudo apt-get install \
    build-essential cmake \
    libgtk2.0-dev pkg-config \
    libavcodec-dev libavformat-dev \
    libswscale-dev libpcsclite-dev \
    libv4l-dev libasound2-dev \
    gcc-4.9 g++-4.9
export CXX="g++-4.9"
sudo npm install -g node-gyp node-pre-gyp
```

## OpenCV@2.4.8

Install from APT

```
apt-get install -y libopencv-core-dev libopencv-highgui-dev libopencv-imgproc-dev libopencv-video-dev libopencv-features2d-dev libopencv-objdetect-dev
```

Or download the OpenCV source archive from https://opencv.org/releases.html and unpack it. In source folder run following:

```
mkdir build && cd build
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
make -j7
sudo make install
```

# Preliminaries for MacOS

## OpenCV

Using Brew install OpenCV@2.4.8

```
brew install opencv@2
brew install pkg-config
```

# Installation

## Mac OS X NodeJS setup

Note: Use the latest NodeJS version in the 8.* series.

```
curl -L https://git.io/n-install | bash -s -- -y 8.12
. ~/.bash_profile
```

## Installing packages

```
node-gyp build
npm install
```