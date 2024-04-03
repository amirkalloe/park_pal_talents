# Park Pal Talents

This repository contains the code for the Park Pal Talents project.

## Prerequisites

- Python 3.12
- Poetry
- SQLite
- Docker

## Installation

1. First install python 3.12:
``sudo apt-get install python3.12``
2. Then install poetry:
``sudo apt install python3-poetry``
3. Make sure to use ptyhon 3.12:
``poetry env use 3.12``
4. Then install the dependencies using poetry:
``poetry install``

5. Set up the database
``sudo apt install sqlite``
``make migration_upgrade_base``

6. Build dockerfile:
``docker build -t amirkalloe/container . -f "backend/Dockerfile"``

7. First erase the flash memory:
``poetry run esptool.py --chip esp32 --port /dev/ttyUSBCOM6 erase_flash``
8. Run the following:
``poetry run esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ESP32_GENERIC-20240105-v1.22.1.bin``