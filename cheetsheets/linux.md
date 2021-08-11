# linux commands 

## todo:
1. clean up notes
   
## contents


# awk

# blkid

`blkid /dev/sdb1`
    
_fstab_
    
    UUID=c286bbaf-91fd-4f16-8155-614cd6d507a9 /chroot xfs nobarrier,noatime 00

# dmicode

`sudo /usr/sbin/dmidecode`

`sudo /usr/sbin/dmidecode --string system-manufacturer`

`sudo /usr/sbin/dmidecode --string system-product-name`

`sudo /usr/sbin/dmidecode --string system-serial-number`

# file size sorted 
    
`ls -lahrS`

`du -sh ./* | grep G | sort -n`

# find exit status
    
`echo $?`

# find file and dir size
    
`ls -laht * | grep G | sort -n`

`du -sh ./* | grep G| sort -n`

# find and remove
    
`find /backups/mysqldumps/ -name "dump_150302_00016*"`

`find /backups/mysqldumps/ -name "dump_150302_000160*" -exec rm -i {} \;`

# find process by port
    
`sudo netstat -nlp | grep 54439`

`sudo lsof -i :54439`

`sudo lsof -i tcp:54439`

# fuser
    
`fuser -m /scratch/exports`

`fuser -v -m /tmp`

# gdb

# inodes

`ls -1 /var/lock`

`stat /var/lock`

`df -i`

`du -i`

# ln 

sudo ln -sf /usr/bin/{xscreensaver,cinnamon-screensaver}

# mdadm

# status check
    
    watch -n1 cat /proc/mdstat
    mdadm -D /dev/md0

# sync check
    
    cat /sys/block/md0/md/sync_action
    echo "idle" > /sys/block/md0/md/sync_action
    echo "check" > /sys/block/md0/md/sync_action
    echo "repair" > /sys/block/md0/md/sync_action

# array state 
    
    cat /sys/block/md0/md/array_state
    echo "clean" > /sys/block/md0/md/array_state

# rebuild event 
    
    tail -f /var/log/syslog
    cat /proc/mdstat
    cat /proc/sys/dev/raid/speed_limit_min
    cat /sys/class/block/md0/md/sync_action
    echo check/idle/repair >> /sys/class/block/md0/md/sync_action
    /etc/mdadm.conf
    cat /sys/block/md0/md/mismatch_cnt
    mdadm --zero-superblock /dev/sda

# megacli

    MegaCli -PDList -aALL
    MegaCli -LDInfo -Lall -aALL
    MegaCli -CfgForeign -Scan -a0
    MegaCli -CfgForeign -Clear -a0
    MegaCli -CfgLdAdd r0[EnclosureID:SlotID] -a0

    MegaCli -AdpGetPciInfo -aAll
    MegaCli -EncInfo -a0
    MegaCli -LdPdInfo -a0
    MegaCli -LDInfo -Lall -a0
    MegaCli -LdPdInfo -a0 | grep -E "Virtual Drive:|Slot Number:" | xargs | sed -r 's/(Slot Number:)(\s[0-9]+)/\2,/g' | sed 's/(Target Id: .)/Physical Drives ids:/g' | sed 's/Virtual Drive:/\nVirtual Drive:/g'
    
    MegaCli -CfgLdAdd -rX[enclosure_id:physical_id,enclosure_id:physical_id] -aN
    MegaCli -CfgLdAdd -r0[245:3,245:4] -a0

# controller info
    
    MegaCli -AdpAllInfo -aALL
    MegaCli -CfgDsply -aALL
    MegaCli -AdpEventLog -GetEvents -f events.log -aALL && cat events.log
    MegaCli -AdpEventLog -GetEvents -f events.log -aALL && tail -n 30 events.log

## enclosure info
    
    MegaCli -EncInfo -aALL

#### virtual drive infromation
    
    MegaCli -LDInfo -Lall -aALL

#### physical drive info
    
    MegaCli -PDList -aALL
    MegaCli -PDInfo -PhysDrv [E:S] -aALL

#### make good
    
    MegaCli -PDMakeGood -PhysDrv[E:S] -aN

#### show missing drives
    
    MegaCli -Pdgetmissing -a0

#### battery backup info
    
    MegaCli  -AdpBbuCmd -aALL


*add disk to array manually* 
    
    sudo MegaCli -PDList -aALL| grep -i firm
    sudo MegaCli -PDMakeGood -PhysDrv[32:7] -a0
    sudo /usr/local/rnt/sbin/MegaCli -CfgLdAdd -r0 [32:7] -strpsz256 -a0

### memory 
    
    free -m

    vmstat -s

    cat /proc/meminfo

    cat /sys/devices/system/edac/mc/mc0/csrow*/ue_count

    cat /sys/devices/system/edac/mc/mc0/csrow*/ce_count

    sudo dmidecode -t memory

    ps aux | awk '{print $2, $4, $5, $11}' | sort -k2rn | head -n 2

    cat /proc/pid/smaps

### mv
    
    sudo mv /usr/bin/cinnamon-screensaver{,.real}

### netcat

#### recieving 
    
    nc -l 3306 | tar xzvf -

#### sending 
    
    tar -czf - *.frm | nc <server> 3306

### ps
    
    ps aux
    ps auxwwf | grep kcryptd | awk '{print $2, $11}
    ps auxf | sort -nr -k 4 | head -5

### rsync
    
    rsync -rvu --delete-before bin <server>:~/bin

### screen 
    
    sudo screen -x

### sed
    
    sed -i 48d .ssh/known_hosts
    sed -i '/dbch19a/d' .ssh/known_hosts

### string 
    
    string binary | grep 

### swap
    
    cat /proc/meminfo
    /proc/${PID}/smaps
    less /proc/14597/smaps
    /proc/${PID}/status
    less /proc/14587/status
    /proc/${PID}/stat

### systemctl
    
    sudo systemctl list-unit-files | grep enabled

    sudo systemctl status mysqld.service
    sudo systemctl stop mysqld.service
    sudo systemctl disable mysqld.service

    sudo systemctl status nails.service
    sudo systemctl stop nails.service

### shutdown
    
    shutdown -r 5 "message"
    shutdown -h now "message"

### tmux
    
    tmux
    tmux a
    tmux new -s foo
    tmux a -t foo

### top
    
    top

    top -bn1 | head -n 15


### writes to disk
    
    lsof | grep -e "[[:digit:]]\+w"

    iostat -d 10 /dev/fioa
    iostat -d 10 /dev/mapper/cachedev

### write zeros to log
    
    /dev/null > /var/log/messages

### ulimit
    
    ulimit

    ulimit -a

### user info
    
    id
    who
    w
    getent passwd 3615
    id brent.northcutt

### xfs
    
    mkfs.xfs
    xfs_info
    xfs_repair
    xfs_db -c frag -r /dev/sda3
    xfs_fr /dev/sda3
    xfs_bmap
    xfs_admin
    xfs_copy
