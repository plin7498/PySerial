#!/usr/bin/env python
# parallel port access using the ppdev driver

import sys
import struct
import fcntl
import os

#----
# Generated by h2py 0.1.1 from <linux/ppdev.h>,
# then cleaned up a bit by Michael P. Ashton and then a gain by chris ;-)
# Changes for Python2.2 support (c) September 2004 Alex.Perry@qm.com


def sizeof(type): return struct.calcsize(type)
def _IOC(dir, type, nr, size):  return (dir << _IOC_DIRSHIFT ) | (type << _IOC_TYPESHIFT ) |\
                                       (nr << _IOC_NRSHIFT ) | (size << _IOC_SIZESHIFT)
def _IO(type, nr):      return _IOC(_IOC_NONE,  type, nr, 0)
def _IOR(type,nr,size): return _IOC(_IOC_READ,  type, nr, sizeof(size))
def _IOW(type,nr,size): return _IOC(_IOC_WRITE, type, nr, sizeof(size))

_IOC_SIZEBITS   = 14
_IOC_SIZEMASK   = (1L << _IOC_SIZEBITS ) - 1
_IOC_NRSHIFT    = 0
_IOC_NRBITS     = 8
_IOC_TYPESHIFT  = _IOC_NRSHIFT + _IOC_NRBITS
_IOC_TYPEBITS   = 8
_IOC_SIZESHIFT  = _IOC_TYPESHIFT + _IOC_TYPEBITS
IOCSIZE_MASK    = _IOC_SIZEMASK << _IOC_SIZESHIFT
IOCSIZE_SHIFT   = _IOC_SIZESHIFT

# Python 2.2 uses a signed int for the ioctl() call, so ...
if ( sys.version_info[0] < 3 ) or ( sys.version_info[1] < 3 ):
 _IOC_WRITE      =  1L
 _IOC_READ       = -2L
 _IOC_INOUT      = -1L
else:
 _IOC_WRITE      =  1L
 _IOC_READ       =  2L
 _IOC_INOUT      =  3L

_IOC_DIRSHIFT   = _IOC_SIZESHIFT + _IOC_SIZEBITS
IOC_INOUT       = _IOC_INOUT << _IOC_DIRSHIFT
IOC_IN          = _IOC_WRITE << _IOC_DIRSHIFT
IOC_OUT         = _IOC_READ << _IOC_DIRSHIFT

_IOC_NONE       = 0
PP_IOCTL        = ord('p')
PPCLAIM         = _IO(PP_IOCTL,  0x8b)
PPCLRIRQ        = _IOR(PP_IOCTL, 0x93, 'i')

PPDATADIR       = _IOW(PP_IOCTL, 0x90, 'i')
PPEXCL          = _IO(PP_IOCTL,  0x8f)
PPFCONTROL      = _IOW(PP_IOCTL, 0x8e, 'BB')
PPGETFLAGS      = _IOR(PP_IOCTL, 0x9a, 'i')
PPGETMODE       = _IOR(PP_IOCTL, 0x98, 'i')
PPGETMODES      = _IOR(PP_IOCTL, 0x97, 'I')
PPGETPHASE      = _IOR(PP_IOCTL, 0x99, 'i')
PPGETTIME       = _IOR(PP_IOCTL, 0x95, 'll')
PPNEGOT         = _IOW(PP_IOCTL, 0x91, 'i')
PPRCONTROL      = _IOR(PP_IOCTL, 0x83, 'B')
PPRDATA         = _IOR(PP_IOCTL, 0x85, 'B')
#'OBSOLETE__IOR' undefined in 'PPRECONTROL'
PPRELEASE       = _IO(PP_IOCTL,  0x8c)
#'OBSOLETE__IOR' undefined in 'PPRFIFO'
PPRSTATUS       = _IOR(PP_IOCTL, 0x81, 'B')
PPSETFLAGS      = _IOW(PP_IOCTL, 0x9b, 'i')
PPSETMODE       = _IOW(PP_IOCTL, 0x80, 'i')
PPSETPHASE      = _IOW(PP_IOCTL, 0x94, 'i')
PPSETTIME       = _IOW(PP_IOCTL, 0x96, 'll')
PPWCONTROL      = _IOW(PP_IOCTL, 0x84, 'B')
PPWCTLONIRQ     = _IOW(PP_IOCTL, 0x92, 'B')
PPWDATA         = _IOW(PP_IOCTL, 0x86, 'B')
#'OBSOLETE__IOW' undefined in 'PPWECONTROL'
#'OBSOLETE__IOW' undefined in 'PPWFIFO'
#'OBSOLETE__IOW' undefined in 'PPWSTATUS'
PPYIELD         = _IO(PP_IOCTL, 0x8d)
PP_FASTREAD     = 1 << 3
PP_FASTWRITE    = 1 << 2
PP_W91284PIC    = 1 << 4
PP_FLAGMASK     = PP_FASTWRITE | PP_FASTREAD | PP_W91284PIC
PP_MAJOR        = 99
_ASMI386_IOCTL_H= None
_IOC_DIRBITS    = 2
_IOC_DIRMASK    = (1 << _IOC_DIRBITS) - 1
_IOC_NRMASK     = (1 << _IOC_NRBITS) - 1
_IOC_TYPEMASK   = (1 << _IOC_TYPEBITS ) - 1

def _IOC_DIR(nr):       return (nr >> _IOC_DIRSHIFT)  & _IOC_DIRMASK
def _IOC_NR(nr):        return (nr >> _IOC_NRSHIFT)   & _IOC_NRMASK
def _IOC_SIZE(nr):      return (nr >> _IOC_SIZESHIFT) & _IOC_SIZEMASK
def _IOC_TYPE(nr):      return (nr >> _IOC_TYPESHIFT) & _IOC_TYPEMASK
def _IOWR(type, nr, size): return _IOC(_IOC_READ | _IOC_WRITE, type, nr , sizeof(size))

__ELF__         = 1
__i386          = 1
__i386__        = 1
__linux         = 1
__linux__       = 1
__unix          = 1
__unix__        = 1
i386            = 1
linux           = 1
unix            = 1

#-------- Constants from <linux/parport.h>

PARPORT_CONTROL_STROBE  = 0x1
PARPORT_CONTROL_AUTOFD  = 0x2
PARPORT_CONTROL_INIT    = 0x4
PARPORT_CONTROL_SELECT  = 0x8
PARPORT_STATUS_ERROR    = 8
PARPORT_STATUS_SELECT   = 0x10
PARPORT_STATUS_PAPEROUT = 0x20
PARPORT_STATUS_ACK      = 0x40
PARPORT_STATUS_BUSY     = 0x80

IEEE1284_MODE_NIBBLE    = 0
IEEE1284_MODE_BYTE      = 1
IEEE1284_MODE_COMPAT    = 1<<8
IEEE1284_MODE_BECP      = 1<<9
IEEE1284_MODE_ECP       = 1<<4
IEEE1284_MODE_ECPRLE    = IEEE1284_MODE_ECP | (1<<5)
IEEE1284_MODE_ECPSWE    = 1<<10
IEEE1284_MODE_EPP       = 1<<6
IEEE1284_MODE_EPPSL     = 1<<11
IEEE1284_MODE_EPPSWE    = 1<<12
IEEE1284_DEVICEID       = 1<<2
IEEE1284_EXT_LINK       = 1<<14

IEEE1284_ADDR           = 1<<13
IEEE1284_DATA           = 0

PARPORT_EPP_FAST        = 1
PARPORT_W91284PIC       = 2
#----

class Parallel:
    """Class for controlling the pins on a parallel port

    This class provides bit-level access to the pins on a PC parallel
    port.  It is primarily designed for programs which must control
    special circuitry - most often non-IEEE-1284-compliant devices
    other than printers - using 'bit-banging' techniques.

    The current implementation makes ioctl() calls to the Linux ppdev
    driver, using the Python fcntl library.  It might be rewritten in
    C for extra speed.  This particular implementation is written for
    Linux; all of the upper-level calls can be ported to Windows as
    well.

    On Linux, the ppdev device driver, from the Linux 2.4 parallel
    port subsystem, is used to control the parallel port hardware.
    This driver must be made available from a kernel compile.  The
    option is called "Support user-space parallel-port drivers".  When
    using the module, be sure to unload the lp module first: usually
    the lp module claims exclusive access to the parallel port, and if
    it is loaded, this class will fail to open the parallel port file,
    and throw an exception.

    The primary source of information about the Linux 2.4 parallel
    port subsystem is Tim Waugh's documentation, the source for which
    is available in the kernel tree.  This document (called,
    appropriately enough, "The Linux 2.4 Parallel Port Subsystem"),
    thoroughly describes the parallel port drivers and how to use
    them.

    This class provides a method for each of the ioctls supported by
    the ppdev module.  The ioctl methods are named, in uppercase, the
    same as the ioctls they invoke.  The documentation for these
    methods was taken directly from the documentation for their
    corresponding ioctl, and modified only where necessary.

    Unless you have special reason to use the Linux ioctls, you should
    use instead the upper-level functions, which are named in
    lowerCase fashion and should be portable between Linux and
    Windows.  This way, any code you write for this class will (or
    should) also work with the Windows version of this class.
    
    """
    def __init__(self, port = 0):
        if type(port) == type(""):
            self.device = port
        else:
            self.device = "/dev/parport%d" % port
        self._fd = os.open(self.device, os.O_RDWR)
        self.PPEXCL()
        self.PPCLAIM()
        self.setDataDir(1)
        self.setData(0)

    def __del__(self):
        self.PPRELEASE()
        if self._fd is not None:
            os.close(self._fd)

    def timevalToFloat(self, timeval):
        t=struct.unpack('ll', timeval)
        return t[0] + (t[1]/1000000.0)

    def floatToTimeval(self, time):
        sec = int(time)
        usec = int(time*1000000.0)
        return struct.pack('ll', sec, usec)

    def PPCLAIM(self):
        """
        Claims access to the port. As a user-land device driver
        writer, you will need to do this before you are able to
        actually change the state of the parallel port in any
        way. Note that some operations only affect the ppdev driver
        and not the port, such as PPSETMODE; they can be performed
        while access to the port is not claimed.
        """
        fcntl.ioctl(self._fd, PPCLAIM)

    def PPEXCL(self):
        """
        Instructs the kernel driver to forbid any sharing of the port
        with other drivers, i.e. it requests exclusivity. The PPEXCL
        command is only valid when the port is not already claimed for
        use, and it may mean that the next PPCLAIM ioctl will fail:
        some other driver may already have registered itself on that
        port.

        Most device drivers don't need exclusive access to the
        port. It's only provided in case it is really needed, for
        example for devices where access to the port is required for
        extensive periods of time (many seconds).

        Note that the PPEXCL ioctl doesn't actually claim the port
        there and then---action is deferred until the PPCLAIM ioctl is
        performed.
        """
        fcntl.ioctl(self._fd, PPEXCL)

    def PPRELEASE(self):
        """
        Releases the port. Releasing the port undoes the effect of
        claiming the port. It allows other device drivers to talk to
        their devices (assuming that there are any).
        """
        fcntl.ioctl(self._fd, PPRELEASE)

    def PPYIELD(self):
        """
        Yields the port to another driver. This ioctl is a kind of
        short-hand for releasing the port and immediately reclaiming
        it. It gives other drivers a chance to talk to their devices,
        but afterwards claims the port back. An example of using this
        would be in a user-land printer driver: once a few characters
        have been written we could give the port to another device
        driver for a while, but if we still have characters to send to
        the printer we would want the port back as soon as possible.

        It is important not to claim the parallel port for too long,
        as other device drivers will have no time to service their
        devices. If your device does not allow for parallel port
        sharing at all, it is better to claim the parallel port
        exclusively (see PPEXCL).
        """
        fcntl.ioctl(self._fd, PPYIELD)

    def PPNEGOT(self, mode):
        """
        Performs IEEE 1284 negotiation into a particular
        mode. Briefly, negotiation is the method by which the host and
        the peripheral decide on a protocol to use when transferring
        data.

        An IEEE 1284 compliant device will start out in compatibility
        mode, and then the host can negotiate to another mode (such as
        ECP).

        The 'mode' parameter should be one of the following constants
        from PPDEV:

        - IEEE1284_MODE_COMPAT
        - IEEE1284_MODE_NIBBLE
        - IEEE1284_MODE_BYTE
        - IEEE1284_MODE_EPP
        - IEEE1284_MODE_ECP

        The PPNEGOT ioctl actually does two things: it performs the
        on-the-wire negotiation, and it sets the behaviour of
        subsequent read/write calls so that they use that mode (but
        see PPSETMODE).
        """
        fcntl.ioctl(self._fd, PPNEGOT, struct.pack('i', mode))

    def PPSETMODE(self, mode):
        """
        Sets which IEEE 1284 protocol to use for the read and write
        calls.

        The 'mode' parameter should be one of the following constants
        from PPDEV:

        - IEEE1284_MODE_COMPAT
        - IEEE1284_MODE_NIBBLE
        - IEEE1284_MODE_BYTE
        - IEEE1284_MODE_EPP
        - IEEE1284_MODE_ECP
        """
        fcntl.ioctl(self._fd, PPSETMODE, struct.pack('i', mode))

    def PPGETMODE(self):
        """
        Retrieves the IEEE 1284 mode being used for read and
        write.  The return value is one of the following constants
        from PPDEV:

        - IEEE1284_MODE_COMPAT
        - IEEE1284_MODE_NIBBLE
        - IEEE1284_MODE_BYTE
        - IEEE1284_MODE_EPP
        - IEEE1284_MODE_ECP
        """
        ret = struct.pack('i', 0)
        ret = fcntl.ioctl(self._fd, PPGETMODE, ret)
        return struct.unpack('i', ret)[0]

    def PPGETTIME(self):
        """
        Retrieves the time-out value. The read and write calls will
        time out if the peripheral doesn't respond quickly enough. The
        PPGETTIME ioctl retrieves the length of time that the
        peripheral is allowed to have before giving up.

        Returns the timeout value in seconds as a floating-point value.
        """
        ret = struct.pack('ll', 0, 0)
        ret = fcntl.ioctl(self._fd, PPGETTIME, ret)
        return timevalToFloat(ret)

    def PPSETTIME(self, time):
        """
        Sets the time-out (see PPGETTIME for more information).
        'time' is the new time-out in seconds; floating-point values
        are acceptable.
        """
        fcntl.ioctl(self._fd, PPSETTIME, floatToTimeval(time))

    def PPGETMODES(self):
        """
        Retrieves the capabilities of the hardware (i.e. the modes
        field of the parport structure).
        """
        raise NotImplementedError

    def PPSETFLAGS(self):
        """
        Sets flags on the ppdev device which can affect future I/O
        operations. Available flags are:

        - PP_FASTWRITE
        - PP_FASTREAD
        - PP_W91284PIC
        """
        raise NotImplementedError

    def PPWCONTROL(self, lines):
        """
        Sets the control lines.  The 'lines' parameter is a bitwise OR
        of the following constants from PPDEV:

        - PARPORT_CONTROL_STROBE
        - PARPORT_CONTROL_AUTOFD
        - PARPORT_CONTROL_INIT
        - PARPORT_CONTROL_SELECT
        """
        fcntl.ioctl(self._fd, PPWCONTROL, struct.pack('B', lines))

    def PPRCONTROL(self):
        """
        Returns the last value written to the control register, in the
        form of an integer, for which each bit corresponds to a control
        line (although some are unused).

        This doesn't actually touch the hardware; the last value
        written is remembered in software. This is because some
        parallel port hardware does not offer read access to the
        control register.

        The control lines bits are defined by the following constants
        from PPDEV:

        - PARPORT_CONTROL_STROBE
        - PARPORT_CONTROL_AUTOFD
        - PARPORT_CONTROL_SELECT
        - PARPORT_CONTROL_INIT
        """
        ret = struct.pack('B',0)
        ret = fcntl.ioctl(self._fd, PPRCONTROL, ret)
        return struct.unpack('B', ret)[0]

    def PPFCONTROL(self, mask, val):
        """
        Frobs the control lines. Since a common operation is to change
        one of the control signals while leaving the others alone, it
        would be quite inefficient for the user-land driver to have to
        use PPRCONTROL, make the change, and then use PPWCONTROL. Of
        course, each driver could remember what state the control
        lines are supposed to be in (they are never changed by
        anything else), but in order to provide PPRCONTROL, ppdev must
        remember the state of the control lines anyway.

        The PPFCONTROL ioctl is for "frobbing" control lines, and is
        like PPWCONTROL but acts on a restricted set of control
        lines. The ioctl parameter is a pointer to a struct
        ppdev_frob_struct:
        
        struct ppdev_frob_struct {
            unsigned char mask;
            unsigned char val;
        };

        The mask and val fields are bitwise ORs of control line names
        (such as in PPWCONTROL). The operation performed by PPFCONTROL
        is:

        new_ctr = (old_ctr & ~mask) | val

        In other words, the signals named in mask are set to the
        values in val.
        """
        fcntl.ioctl(self._fd, PPFCONTROL, struct.pack('BB', mask, val))

    def PPRSTATUS(self):
        """
        Returns an unsigned char containing bits set for each status
        line that is set (for instance, PARPORT_STATUS_BUSY). The
        ioctl parameter should be a pointer to an unsigned char.
        """
        ret = struct.pack('B',0)
        ret = fcntl.ioctl(self._fd, PPRSTATUS, ret)
        return struct.unpack('B', ret)[0]

    def PPDATADIR(self, out):
        """
        Controls the data line drivers. Normally the computer's
        parallel port will drive the data lines, but for byte-wide
        transfers from the peripheral to the host it is useful to turn
        off those drivers and let the peripheral drive the
        signals. (If the drivers on the computer's parallel port are
        left on when this happens, the port might be damaged.)
        This is only needed in conjunction with PPWDATA or PPRDATA.

        The 'out' parameter indicates the desired port direction.  If
        'out' is true or non-zero, the drivers are turned on (forward
        direction); otherwise, the drivers are turned off (reverse
        direction).
        """
        if out:
            msg=struct.pack('i',0)
        else:
            msg=struct.pack('i',1)
        fcntl.ioctl(self._fd, PPDATADIR, msg)

    def PPWDATA(self, byte):
        """
        Sets the data lines (if in forward mode). The ioctl parameter
        is a pointer to an unsigned char.
        """
        fcntl.ioctl(self._fd, PPWDATA,struct.pack('B',byte))

    def PPRDATA(self):
        """
        Reads the data lines (if in reverse mode). The ioctl parameter
        is a pointer to an unsigned char.
        """
        ret=struct.pack('B',0)
        ret=fcntl.ioctl(self._fd, PPRDATA,ret)
        return struct.unpack('B',ret)[0]

    def PPCLRIRQ(self):
        """
        Returns the current interrupt count, and clears it.  The ppdev
        driver keeps a count of interrupts as they are triggered.
        """
        ret=struct.pack('i',0)
        ret=fcntl.ioctl(self._fd, PPCLRIRQ,ret)
        return struct.unpack('i',ret)[0]

    def PPWCTLONIRQ(self, lines):
        """
        Set a trigger response. Afterwards when an interrupt is
        triggered, the interrupt handler will set the control lines as
        requested. The ioctl parameter is a pointer to an unsigned
        char, which is interpreted in the same way as for PPWCONTROL.

        The reason for this ioctl is simply speed. Without this ioctl,
        responding to an interrupt would start in the interrupt
        handler, switch context to the user-land driver via poll or
        select, and then switch context back to the kernel in order to
        handle PPWCONTROL. Doing the whole lot in the interrupt
        handler is a lot faster.
        """
        fcntl.ioctl(self._fd, PPWCTLONIRQ,struct.pack('B',lines))

    #data lines
##    def data(self):
##        """Returns the states of the data bus line drivers (pins 2-9)"""
##        return self._data

    def setDataDir(self,out):
        """Activates or deactivates the data bus line drivers (pins 2-9)"""
        self._dataDir = out
        self.PPDATADIR(out)

    def dataDir(self):
        """Returns true if the data bus line drivers are on (pins 2-9)"""
        return self._dataDir

    #control lines
##    def strobe(self):
##        """Returns the state of the nStrobe output (pin 1)"""
##        return (self.PPRCONTROL()&PARPORT_CONTROL_STROBE)==0

    def setDataStrobe(self, level):
        """Sets the state of the nStrobe output (pin 1)"""
        if level:
            self.PPFCONTROL(PARPORT_CONTROL_STROBE, 0)
        else:
            self.PPFCONTROL(PARPORT_CONTROL_STROBE, PARPORT_CONTROL_STROBE)

##    def autoFd(self):
##        """Returns the state of the nAutoFd output (pin 14)"""
##        return (self.PPRCONTROL()&PARPORT_CONTROL_AUTOFD)==0

    def setAutoFeed(self, level):
        """Sets the state of the nAutoFd output (pin 14)"""
        if level:
            self.PPFCONTROL(PARPORT_CONTROL_AUTOFD, 0)
        else:
            self.PPFCONTROL(PARPORT_CONTROL_AUTOFD, PARPORT_CONTROL_AUTOFD)

##    def init(self):
##        """Returns the state of the nInit output (pin 16)"""
##        return (self.PPRCONTROL()&PARPORT_CONTROL_INIT)!=0

    def setInitOut(self, level):
        """Sets the state of the nInit output (pin 16)"""
        if level:
            self.PPFCONTROL(PARPORT_CONTROL_INIT, PARPORT_CONTROL_INIT)
        else:
            self.PPFCONTROL(PARPORT_CONTROL_INIT, 0)

##    def selectIn(self):
##        """Returns the state of the nSelectIn output (pin 17)"""
##        return (self.PPRCONTROL()&PARPORT_CONTROL_SELECT)==0

    def setSelect(self,level):
        """Sets the state of the nSelectIn output (pin 17)"""
        if level:
            self.PPFCONTROL(PARPORT_CONTROL_SELECT, 0)
        else:
            self.PPFCONTROL(PARPORT_CONTROL_SELECT, PARPORT_CONTROL_SELECT)

    def setData(self,d):
        """Sets the states of the data bus line drivers (pins 2-9)"""
        self._data=d
        return self.PPWDATA(d)

    #status lines
    def getInError(self):
        """Returns the level on the nFault pin (15)"""
        return (self.PPRSTATUS() & PARPORT_STATUS_ERROR) != 0

    def getInSelected(self):
        """Returns the level on the Select pin (13)"""
        return (self.PPRSTATUS() & PARPORT_STATUS_SELECT) != 0

    def getInPaperOut(self):
        """Returns the level on the paperOut pin (12)"""
        return (self.PPRSTATUS() & PARPORT_STATUS_PAPEROUT) != 0

    def getInAcknowledge(self):
        """Returns the level on the nAck pin (10)"""
        return (self.PPRSTATUS() & PARPORT_STATUS_ACK) != 0

    def getInBusy(self):
        """Returns the level on the Busy pin (11)"""
        return (self.PPRSTATUS() & PARPORT_STATUS_BUSY) == 0

