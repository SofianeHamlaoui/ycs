# YCS (Youtube Comment Scrapper)

## Introduction

A small command line utility for scraping YouTube comments using Python3 and Youtube API.

## Quick start

### Requirements

- A  YouTube Data API 
- Python3

### Installation

#### Linux

1- First, install python3

```   
    sudo apt install python3 < Debian-based distributions
    sudo dnf install python3 < RPM-based distributions
    sudo pacman -S python3 < Arch-based distributions
    sudo zypper install python3 < OS-based distributions
    sudo yum install python3 < RH-based distributions

```

2- Then install all requirement for python

```
    # install python requirements
    pip3 install -r requirements.txt
```

3- Get a YouTube Data API : follow this [tutorial](https://www.youtube.com/watch?v=pP4zvduVAqo)

4- Clone this repository 
```
    git clone git@github.com:massykezzoul/ycs.git
    cd src/
```

5- Write your API key in file named `api.key` in the `src/` directory by running this command or other way
```
    echo "<YOUR_API_KEY>" > src/api.key
```

6- Run the programme and pray
```
    python3 src/ycs.py > output.json # this print the result in the file 'output.json'
```

#### Windows

In futur update inchalah...

## In futur version

- Give the video id by argument
- Write the output in a file given by argument
- Set a number maximum of comments extracted

## Author

* Massili Kezzoul -> (massy.kezzoul@gmail.com)
* Last update     -> march 15, 2020
