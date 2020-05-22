import usb.core
import usb.util

from infi.devicemanager import DeviceManager
dm = DeviceManager()
devices = dm.all_devices
for i in devices:
    try:
        print ('{} : address: {}, bus: {}, location: {}'.format(i.friendly_name, i.address, i.bus_number, i.location))
    except Exception:
        pass


import usb.backend.libusb1

def LoadDevices():
    backend = usb.backend.libusb1.get_backend(find_library=lambda x: "C:\\libusb-1.0.20\\MS64\\dll\\libusb-1.0.dll")
    return usb.core.find(backend=backend, find_all=True)

def DevicesAttached():

    counter = 0
    dev = LoadDevices()
    for d in dev:
        try:
            counter += 1
        except NotImplementedError:
            print("Device number " + str(counter) + " is busy." + "\n")
            counter += 1
        except usb.core.USBError:
            print("Device number " + str(counter) + " is either disconnected or not found." + "\n")
            counter += 1
    return counter

def EnumerateUSB():    #I use a simple function that scans all known USB connections and saves their info in the file
    counter = 0
    message = ''
    dev = LoadDevices()
    for d in dev:
        try:
            message += "USB Device number " + str(counter) + ":" + "\n"
            message += d._get_full_descriptor_str() + "\n"
            message += d.get_active_configuration() + "\n"
            message += "\n"
            counter += 1
        except NotImplementedError:
            message += "Device number " + str(counter) + " is busy." + "\n"
            message += "\n"
            counter += 1
        except usb.core.USBError:
            message += "Device number " + str(counter) + " is either disconnected or not found." + "\n"
            message += "\n"
            counter += 1

    return message
