import lvm
import time

#print [item for item in dir(lvm) if not item.startswith("__")]
'''
['LibLVMError', 'THIN_DISCARDS_IGNORE', 'THIN_DISCARDS_NO_PASSDOWN', 'THIN_DISCARDS_PASSDOWN', 'configFindBool', 'configOverride', 'configReload', 'error', 'gc', 'getVersion', 'listPvs', 'listVgNames', 'listVgUuids', 'percentToFloat', 'pvCreate', 'pvRemove', 'scan', 'vgCreate', 'vgNameFromDevice', 'vgNameFromPvid', 'vgNameValidate', 'vgOpen']
'''
#pv
'''
['getDevSize', 'getFree', 'getMdaCount', 'getName', 'getProperty', 'getSize', 'getUuid', 'listPVsegs', 'resize']
'''

#vg
'''
['addTag', 'close', 'createLvLinear', 'createLvThin', 'createLvThinpool', 'extend', 'getExtentCount', 'getExtentSize', 'getFreeExtentCount', 'getFreeSize', 'getMaxLv', 'getMaxPv', 'getName', 'getProperty', 'getPvCount', 'getSeqno', 'getSize', 'getTags', 'getUuid', 'isClustered', 'isExported', 'isPartial', 'listLVs', 'listPVs', 'lvFromName', 'lvFromUuid', 'lvNameValidate', 'pvFromName', 'pvFromUuid', 'reduce', 'remove', 'removeTag', 'setExtentSize', 'setProperty']
'''

#lv
'''
['activate', 'addTag', 'deactivate', 'getAttr', 'getName', 'getOrigin', 'getProperty', 'getSize', 'getTags', 'getUuid', 'isActive', 'isSuspended', 'listLVsegs', 'remove', 'removeTag', 'rename', 'resize', 'snapshot']
'''


def print_lvm_stuff():
    vg_names = lvm.listVgNames()
    for vg_name in vg_names:
        vg = lvm.vgOpen(vg_name, 'r')
        print '=================================='

        print\
        'VG name:{}\nID:{}\nSize:{}\nExtentCount:{}\nExtentSize:{}\nFreeExtentCount:{}\nFreeSize:{}\nMaxLv:{}\nMaxPv:{}\nPvCount:{}\nSeqno:{}\nClustered:{}\nExported:{}\nPartial:{}'.format(
        vg.getName(),
        vg.getUuid(),
        vg.getSize(),
        vg.getExtentCount(),
        vg.getExtentSize(),
        vg.getFreeExtentCount(),
        vg.getFreeSize(),
        vg.getMaxLv(),
        vg.getMaxPv(),
        vg.getPvCount(),
        vg.getSeqno(),
        vg.isClustered(),
        vg.isExported(),
        vg.isPartial()
        )

        print '\\\\\\\\\\\\\\\\PVs\\\\\\\\\\\\\\\\\\\\\\\\\\'
        pv_list = vg.listPVs()
        for pv in pv_list:
            print\
            'PV name:{}\nID:{}\nSize:{}\nMdaCount:{}\nFree:{}\nDevSize:{}\n'.format(
            pv.getName(),
            pv.getUuid(),
            pv.getSize(),
            pv.getMdaCount(),
            pv.getFree(),
            pv.getDevSize()
            )
        print '\\\\\\\\\\\\\\\\PVs\\\\\\\\\\\\\\\\\\\\\\\\\\'

        print '\\\\\\\\\\\\\\\\LVs\\\\\\\\\\\\\\\\\\\\\\\\\\'
        lv_list = vg.listLVs()
        for lv in lv_list:
            print\
            'LV name:{}\nID:{}\nSize:{}\nAttr:{}\nOrigin:{}\nActive:{}\nSuspended:{}'.format(
            lv.getName(),
            lv.getUuid(),
            lv.getSize(),
            lv.getAttr(),
            lv.getOrigin(),
            lv.isActive(),
            lv.isSuspended()
            )
        print '\\\\\\\\\\\\\\\\LVs\\\\\\\\\\\\\\\\\\\\\\\\\\'

        vg.close()

        return True

print_lvm_stuff()

device = '/dev/sdd'
vg_name = 'TEST_VG'
lv_name = 'TEST_LV'

#test create one PV one VG one LV and delete
def normal_LV():

    lvm.pvCreate(device)

    vg = lvm.vgCreate(vg_name)

    vg.extend('/dev/sdd')

    pv_list = vg.listPVs()
    for pv in pv_list:
        print 'PV name: ', pv.getName(), ' ID: ', pv.getUuid(), 'Size: ', pv.getSize()
    lv = vg.createLvLinear(lv_name, 1024*1024*1024 )

    print lv.deactivate()
    print lv.getAttr()
    raw_input('acticate?')
    print lv.activate()
    print lv.getAttr()


    vg.close()
    raw_input('??')

    #vg.reduce('/dev/sdd')

    vg = lvm.vgOpen(vg_name, 'w')
    lv = vg.lvFromName(lv_name)
    lv.remove()

    vg.remove()

    lvm.configReload()

    lvm.pvRemove(device)

    return True

#normal_LV()

#test create one PV one VG one pool LV one thin LV and delete
def thinpool_LV():
    
    device = '/dev/sdd'
    vg_name = 'TEST_VG'
    lv_pool = 'TEST_POOL'
    lv_thin = 'TEST_THIN'

    lvm.pvCreate(device) 
    
    vg = lvm.vgCreate(vg_name)

    vg.extend('/dev/sdd')
    
    pv_list = vg.listPVs()
    for pv in pv_list:
        print 'PV name: ', pv.getName(), ' ID: ', pv.getUuid(), 'Size: ', pv.getSize()
    lv = vg.createLvThinpool(lv_pool, 1024*1024*1024 )
    lv2 = vg.createLvThin(lv.getName(), lv_thin, 1024*1024*1024*1024)

    print lv2.deactivate()
    print lv2.getAttr()
    print lv.deactivate()
    print lv.getAttr()
    raw_input('acticate?')
    print lv.activate()
    print lv.getAttr()
    print lv2.activate()
    print lv2.getAttr()


    vg.close()
    raw_input('??')
     
    #vg.reduce('/dev/sdd')

    vg = lvm.vgOpen(vg_name, 'w')
    lv = vg.lvFromName(lv_thin)
    lv.remove()

    lv = vg.lvFromName(lv_pool)
    lv.remove()

    vg.remove()

    lvm.configReload()

    lvm.pvRemove(device) 

    return True

#thinpool_LV()
