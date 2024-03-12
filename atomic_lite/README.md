First install python 3.1:
``sudo apt-get install python3.12``
Then install poetry:
Then install the dependencies using poetry:
``poetry install``
Then install the dependencies using poetry:
``poetry install``

First erase the flash memory:
``poetry run esptool.py --chip esp32 --port /dev/ttyUSBCOM6 erase_flash``
Run the following:
``poetry run esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ESP32_GENERIC-20240105-v1.22.1.bin``