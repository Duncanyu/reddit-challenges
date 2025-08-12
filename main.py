import asyncio

from bleak import BleakScanner

def detected(device, advertisement_data):
    print(f"Name: {device.name or 'Unknown'}\n   ID: {device.address}\n  SSI: {advertisement_data.rssi} dBm\n")

async def main():
    scanner = BleakScanner(detection_callback = detected)
    await scanner.start()
    await asyncio.sleep(5.0)
    await scanner.stop()
    

asyncio.run(main())