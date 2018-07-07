#import lvm
import pyudev
context = pyudev.Context()


for device in context.list_devices(MAJOR='8'):
    if (device.device_type == 'disk'):
        
        print device.get('ID_VENDOR') 
        print device.get('DEVNAME') 

        print "\n========================================\n"

        for key, value in device.items():
            print '{key}={value}'.format(key=key, value=value)

        print device
        print "\n========================================\n"

#for device in context.list_devices(subsystem='block', DEVTYPE='partition'):
#    print(device.get('ID_FS_LABEL', 'unlabeled partition'))

#for device in context.list_devices(subsystem='block',  DEVTYPE='disk'):
#    print('{0} ({1})'.format(device.device_node, device.device_type))
#    print('{0} attached to PCI slot {1}'.format(device.device_node, device.find_parent('pci')['PCI_SLOT_NAME']))


#context = pyudev.Context()
#monitor = pyudev.Monitor.from_netlink(context)
#monitor.filter_by(subsystem= 'block', device_type='disk' )
#for action, device in monitor:
#    if "MAJOR" in device and "DEVTYPE" in device:
#        if device.get('MAJOR') == "8" and device.get('DEVTYPE') == "disk":
#            if action == "add" or action == "remove":
#                print('{0}: {1}'.format(action, device.get('DEVNAME')))
#                for key, value in device.iteritems():
#                    print '{key}={value}'.format(key=key, value=value)

#                print device

#    print '{0}: {1}'.format(action, device)

#    if action == "add":
#        print "disk add"
#    elif action == "remove":
#        print "disk remove"
#    else:
#        pass




#SATA
"""
UDEV  [419327.284087] change   /devices/pci0000:80/0000:80:02.0/0000:81:00.0/host0/target0:0:5/0:0:5:0/block/sdb (block)
ACTION=change
DEVLINKS=/dev/disk/by-id/ata-WDC_WD20NPVX-00EA4T0_WD-WXP1E94D0VXT /dev/disk/by-id/wwn-0x50014ee2b66e9e36 /dev/disk/by-path/pci-0000:81:00.0-scsi-0:0:5:0
DEVNAME=/dev/sdb
DEVPATH=/devices/pci0000:80/0000:80:02.0/0000:81:00.0/host0/target0:0:5/0:0:5:0/block/sdb
DEVTYPE=disk
ID_ATA=1
ID_ATA_DOWNLOAD_MICROCODE=1
ID_ATA_FEATURE_SET_APM=1
ID_ATA_FEATURE_SET_APM_CURRENT_VALUE=128
ID_ATA_FEATURE_SET_APM_ENABLED=1
ID_ATA_FEATURE_SET_HPA=1
ID_ATA_FEATURE_SET_HPA_ENABLED=1
ID_ATA_FEATURE_SET_PM=1
ID_ATA_FEATURE_SET_PM_ENABLED=1
ID_ATA_FEATURE_SET_PUIS=1
ID_ATA_FEATURE_SET_PUIS_ENABLED=0
ID_ATA_FEATURE_SET_SECURITY=1
ID_ATA_FEATURE_SET_SECURITY_ENABLED=0
ID_ATA_FEATURE_SET_SECURITY_ENHANCED_ERASE_UNIT_MIN=392
ID_ATA_FEATURE_SET_SECURITY_ERASE_UNIT_MIN=392
ID_ATA_FEATURE_SET_SMART=1
ID_ATA_FEATURE_SET_SMART_ENABLED=1
ID_ATA_ROTATION_RATE_RPM=5200
ID_ATA_SATA=1
ID_ATA_SATA_SIGNAL_RATE_GEN1=1
ID_ATA_SATA_SIGNAL_RATE_GEN2=1
ID_ATA_WRITE_CACHE=1
ID_ATA_WRITE_CACHE_ENABLED=1
ID_BUS=ata
ID_FS_TYPE=LVM2_member
ID_FS_USAGE=raid
ID_FS_UUID=yGhYqu-jX26-0l0J-mj9j-RNs1-mxd2-3fhiIV
ID_FS_UUID_ENC=yGhYqu-jX26-0l0J-mj9j-RNs1-mxd2-3fhiIV
ID_FS_VERSION=LVM2 001
ID_MODEL=WDC_WD20NPVX-00EA4T0
ID_MODEL_ENC=WDC\x20WD20NPVX-00EA4T0\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
ID_PATH=pci-0000:81:00.0-scsi-0:0:5:0
ID_PATH_TAG=pci-0000_81_00_0-scsi-0_0_5_0
ID_REVISION=01.01A01
ID_SERIAL=WDC_WD20NPVX-00EA4T0_WD-WXP1E94D0VXT
ID_SERIAL_SHORT=WD-WXP1E94D0VXT
ID_TYPE=disk
ID_WWN=0x50014ee2b66e9e36
ID_WWN_WITH_EXTENSION=0x50014ee2b66e9e36
MAJOR=8
MINOR=16
SEQNUM=5293
SUBSYSTEM=block
USEC_INITIALIZED=250
"""

#SAS
"""
UDEV  [419474.581660] change   /devices/pci0000:80/0000:80:02.0/0000:81:00.0/host0/target0:0:12/0:0:12:0/block/sdd/sdd1 (block)
ACTION=change
DEVLINKS=/dev/disk/by-id/scsi-35000c500726358a7-part1 /dev/disk/by-id/wwn-0x5000c500726358a7-part1 /dev/disk/by-partlabel/logical /dev/disk/by-partuuid/26bbe855-393a-45a8-b03c-2ca092279361 /dev/disk/by-path/pci-0000:81:00.0-scsi-0:0:12:0-part1
DEVNAME=/dev/sdd1
DEVPATH=/devices/pci0000:80/0000:80:02.0/0000:81:00.0/host0/target0:0:12/0:0:12:0/block/sdd/sdd1
DEVTYPE=partition
ID_BUS=scsi
ID_FS_TYPE=LVM2_member
ID_FS_USAGE=raid
ID_FS_UUID=S6poQ6-tKhr-CCm6-6w0p-pboc-GIbN-s5whBs
ID_FS_UUID_ENC=S6poQ6-tKhr-CCm6-6w0p-pboc-GIbN-s5whBs
ID_FS_VERSION=LVM2 001
ID_MODEL=ST300MM0006
ID_MODEL_ENC=ST300MM0006\x20\x20\x20\x20\x20
ID_PART_ENTRY_DISK=8:48
ID_PART_ENTRY_NAME=logical
ID_PART_ENTRY_NUMBER=1
ID_PART_ENTRY_OFFSET=2048
ID_PART_ENTRY_SCHEME=gpt
ID_PART_ENTRY_SIZE=19529728
ID_PART_ENTRY_TYPE=0fc63daf-8483-4772-8e79-3d69d8477de4
ID_PART_ENTRY_UUID=26bbe855-393a-45a8-b03c-2ca092279361
ID_PART_TABLE_TYPE=dos
ID_PATH=pci-0000:81:00.0-scsi-0:0:12:0
ID_PATH_TAG=pci-0000_81_00_0-scsi-0_0_12_0
ID_REVISION=0003
ID_SCSI=1
ID_SCSI_SERIAL=S0K2ADLV0000M4386960
ID_SERIAL=35000c500726358a7
ID_SERIAL_SHORT=5000c500726358a7
ID_TYPE=disk
ID_VENDOR=SEAGATE
ID_VENDOR_ENC=SEAGATE\x20
ID_WWN=0x5000c500726358a7
ID_WWN_WITH_EXTENSION=0x5000c500726358a7
MAJOR=8
MINOR=49
SEQNUM=5296
SUBSYSTEM=block
USEC_INITIALIZED=511997348
"""


#SSD
"""
UDEV  [419940.198726] change   /devices/pci0000:80/0000:80:02.0/0000:81:00.0/host0/target0:2:1/0:2:1:0/block/sdf (block)
ACTION=change
DEVLINKS=/dev/disk/by-id/scsi-36000ea64c00d1a001db4226fc7b20efb /dev/disk/by-id/wwn-0x6000ea64c00d1a001db4226fc7b20efb /dev/disk/by-path/pci-0000:81:00.0-scsi-0:2:1:0
DEVNAME=/dev/sdf
DEVPATH=/devices/pci0000:80/0000:80:02.0/0000:81:00.0/host0/target0:2:1/0:2:1:0/block/sdf
DEVTYPE=disk
ID_BUS=scsi
ID_FS_TYPE=LVM2_member
ID_FS_USAGE=raid
ID_FS_UUID=QeI6aS-SqDr-5IUZ-c556-KfCu-EYyH-66379X
ID_FS_UUID_ENC=QeI6aS-SqDr-5IUZ-c556-KfCu-EYyH-66379X
ID_FS_VERSION=LVM2 001
ID_MODEL=MRROMB
ID_MODEL_ENC=MRROMB\x20\x20\x20\x20\x20\x20\x20\x20\x20\x20
ID_PATH=pci-0000:81:00.0-scsi-0:2:1:0
ID_PATH_TAG=pci-0000_81_00_0-scsi-0_2_1_0
ID_REVISION=3.40
ID_SCSI=1
ID_SCSI_SERIAL=00fb0eb2c76f22b41d001a0dc064ea00
ID_SERIAL=36000ea64c00d1a001db4226fc7b20efb
ID_SERIAL_SHORT=6000ea64c00d1a001db4226fc7b20efb
ID_TYPE=disk
ID_VENDOR=LSI
ID_VENDOR_ENC=LSI\x20\x20\x20\x20\x20
ID_WWN=0x6000ea64c00d1a00
ID_WWN_VENDOR_EXTENSION=0x1db4226fc7b20efb
ID_WWN_WITH_EXTENSION=0x6000ea64c00d1a001db4226fc7b20efb
MAJOR=8
MINOR=80
SEQNUM=5306
SUBSYSTEM=block
USEC_INITIALIZED=780
"""
