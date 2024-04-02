First install python 3.12:
``sudo apt-get install python3.12``
Then install poetry:
``sudo apt install python3-poetry``
Make sure to use ptyhon 3.12:
``poetry env use 3.12``
Then install the dependencies using poetry:
``poetry install``

Set up the database
``sudo apt install sqlite``
``make migration_upgrade_base``



First erase the flash memory:
``poetry run esptool.py --chip esp32 --port /dev/ttyUSBCOM6 erase_flash``
Run the following:
``poetry run esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x1000 ESP32_GENERIC-20240105-v1.22.1.bin``poetr