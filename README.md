# WMIC Query Tool

## About
This repository provides a simple WMIC query tool.
It can be used to read serial numbers of your hardware.

## Usage

### Example 1: Query mainboard serial number

```py
import wmic
print(wmic.query("baseboard")[0]["serialnumber"])
```

### Example 2: Query HDD serial numbers of non-portable devices

```py
import wmic

data = wmic.query("diskdrive", ["mediatype", "serialnumber"])
fix_disks = filter(lambda r: r["mediatype"] == "Fixed hard disk media", data)
hdd_ids = list(map(lambda r: r["serialnumber"], fix_disks))
print(hdd_ids)
```

### Example 3: Query all RAM chip data

```py
import wmic
print(wmic.query("memorychip"))
```
