#!/usr/bin/python

import dbus

bus = dbus.SystemBus()

snapper = dbus.Interface(bus.get_object('org.opensuse.Snapper', '/org/opensuse/Snapper'),
                         dbus_interface='org.opensuse.Snapper')


snapshots = snapper.ListSnapshots("root")

for snapshot in snapshots:
    print snapshot[0], snapshot[1], snapshot[2], snapshot[3], snapshot[4], snapshot[5],
    for k, v in snapshot[6].items():
        print "%s=%s" % (k, v),
    print

