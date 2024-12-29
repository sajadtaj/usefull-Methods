## init

هنگامی که کرنل بالا می اید کرنل `init` را راه می اندازد که مسول اجرای سایر برنامه با کانفیگ های مختلف می باشد. در توزیع های فعلی لیوکس `init`  از نوع `systemd` میباشد   .

## systemd
انواع پروسه های که `saystemd` راه می ادازد:

1. deamon
2. program
3. service
4. subservice

مشاهده init:

```shell
which init
```
output:
>> /usr/sbin/`init`

در واقع init اشاره به یک فایل دیگر دارد:

```shell
readlink -f /sbin/init
```

output :
>> /usr/lib/systemd/`systemd`


## ps

دیدن همه پروسه ها
```shell
ps 
# or
ls /poorc
``` 

### `-p`

میدانیم که همه پروسه ها در لیوکس یک ID دارند.
پروسه init دارای  ID یک  می باشد .
دید پروسه شماره `۱`

```shell
ps -p 1
```
output:

    PID  TTY  TIME     CMD
    1    ?    0:00:01  systemd

```shell
ls /proc/1
```
دیدن همه پروسه ها: بصورت ابشاری 

```shell
pstree |less
```

### `-u`

دید پروسه های یک کاربر 

```shell
ps -u <sername>
```

output:
    
    PID TTY       TIME      CMD
    2390 ?        00:00:00 systemd
    2391 ?        00:00:00 (sd-pam)
    2397 ?        00:00:00 pipewire
    2398 ?        00:00:00 pipewire-media-
    2399 ?        00:00:10 pulseaudio

### `aux`

دیدن پروسه همعه کاربران

```shell
ps aux
```

output:

    USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root           1  0.0  0.0 167076 11600 ?        Ss   08:48   0:01 /sbin/init splash
    root           2  0.0  0.0      0     0 ?        S    08:48   0:00 [kthreadd]
    avahi       1091  0.0  0.0   7712  3840 ?        Ss   08:48   0:00 avahi-daemon: running [TAJ.local]
    root        1093  0.0  0.0  10628  5248 ?        Ss   08:48   0:00 /usr/lib/bluetooth/bluetoothd
    root        1096  0.0  0.0  12380  3072 ?        Ss   08:48   0:00 /usr/sbin/cron -f -P
    message+    1099  0.0  0.0  11244  6016 ?        Ss   08:48   0:01 @dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only

    root        1129  0.0  0.0 243092  7728 ?        Ssl  08:48   0:00 /usr/libexec/power-profiles-daemon
    nvidia-+    1130  0.0  0.0   5324  1924 ?        Ss   08:48   0:00 /usr/bin/nvidia-persistenced --user nvidia-persistenced --no-persistence-mode --verbose
    syslog      1133  0.0  0.0 222404  5504 ?        Ssl  08:48   0:00 /usr/sbin/rsyslogd -n -iNONE


1. **USER**: نام کاربری که فرآیند را اجرا کرده است.
2. **PID**: شناسه فرآیند (Process ID) که به هر فرآیند در سیستم یک شماره منحصربه‌فرد اختصاص می‌دهد.
3. **%CPU**: درصد استفاده از CPU توسط فرآیند در حال اجرا.
4. **%MEM**: درصد استفاده از حافظه (RAM) توسط فرآیند.
5. **VSZ (Virtual Size)**: اندازه مجازی فرآیند که نشان‌دهنده کل فضای حافظه‌ای است که فرآیند به خود اختصاص داده است، شامل حافظه واقعی و حافظه مجازی.
6. **RSS (Resident Set Size)**: اندازه مجموعه مقیم که نشان‌دهنده میزان حافظه فیزیکی است که فرآیند در حال استفاده است.
7. **TTY**: نام ترمینالی که فرآیند از آن راه‌اندازی شده است. برای مثال، `tty1`، `pts/0`.
8. **STAT (Process State)**: وضعیت فعلی فرآیند که می‌تواند شامل حالت‌های مختلفی باشد مانند:
   - `R` (Running): در حال اجرا
   - `S` (Sleeping): در حالت خواب
   - `D` (Uninterruptible Sleep): در حالت خواب غیرقابل وقفه
   - `T` (Stopped): متوقف شده
   - `Z` (Zombie): فرآیند زامبی که خاتمه یافته اما هنوز توسط والدینش جمع‌آوری نشده است.
9. **START**: زمان شروع فرآیند.
10. **TIME**: مدت زمانی که فرآیند در حال اجرا بوده است.
11. **COMMAND**: دستوری که برای اجرای فرآیند استفاده شده است.

`مثال کاربردی:`

    USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
    root         1  0.0  0.1  22528  1100 ?        Ss   Dec29   0:01 /sbin/init
    root         2  0.0  0.0      0     0 ?        S    Dec29   0:00 [kthreadd]
    root         3  0.0  0.0      0     0 ?        S    Dec29   0:00 [ksoftirqd/0]


در این مثال:
- **USER** `root` است.
- **PID** برای فرآیند اول `1` است.
- **%CPU** صفر درصد است.
- **%MEM** مقدار 0.1 درصد است.
- **VSZ** برابر 22528 بایت است.
- **RSS** برابر 1100 بایت است.
- **TTY** `?` به معنای فرآیند بدون ترمینال است.
- **STAT** `Ss` به معنای فرآیند در حالت خواب با اولویت سیستمی است.
- **START** زمان شروع `Dec29` است.
- **TIME** مدت زمان اجرای 0:01 دقیقه است.
- **COMMAND** `'/sbin/init'` است که دستور اجرای فرآیند است.


## unit
سیستم  از  `unit` ساخته شده است و  هر `unit` میتواند سرویس یا مجموعه از سرویس ها یا یک اقدام باشد. همچی unit ها `نام` و `نوع` و `تنظیمات` دارند.

### `Unit types`:

1. **Service Units**: `.service`
2. **Socket Units**: `.socket`
3. **Target Units**: `.target`
4. **Mount Units**: `.mount`
5. **Automount Units**: `.automount`
6. **Swap Units**: `.swap`
7. **Path Units**: `.path`
8. **Timer Units**: `.timer`
9. **Slice Units**: `.slice`
10. **Scope Units**: `.scope`

در systemd، واحدها (units) اشیایی هستند که عملیات و فرآیندهای مختلف سیستم را نمایندگی می‌کنند. هر واحد (unit) نوع مشخصی دارد که عملکرد خاصی را تعیین می‌کند. در زیر به برخی از انواع واحدهای (unit types) معمول در systemd و توضیحات آن‌ها اشاره می‌شود:

#### انواع واحدها (Unit Types) در systemd:

1. **Service Units (واحدهای سرویس)**
   - **پسوند فایل:** `.service`
   - **توضیح:** سرویس‌ها (services) واحدهایی هستند که برای مدیریت و کنترل فرآیندها و دیمون‌ها (daemons) استفاده می‌شوند. مثال: `apache2.service` یا `nginx.service`.
   - **مثال:** راه‌اندازی یک وب‌سرور

2. **Socket Units (واحدهای سوکت)**
   - **پسوند فایل:** `.socket`
   - **توضیح:** این واحدها برای مدیریت سوکت‌های IPC (ارتباط بین فرآیندی) و شبکه استفاده می‌شوند. معمولاً با سرویس‌هایی که به اتصالات شبکه پاسخ می‌دهند، مرتبط هستند.
   - **مثال:** `sshd.socket`

3. **Target Units (واحدهای هدف)**
   - **پسوند فایل:** `.target`
   - **توضیح:** این واحدها برای سازمان‌دهی و گروه‌بندی سایر واحدها استفاده می‌شوند. آن‌ها نقاط سنکرون‌سازی را نمایندگی می‌کنند.
   - **مثال:** `multi-user.target` یا `graphical.target`

4. **Mount Units (واحدهای کوه‌گذاری)**
   - **پسوند فایل:** `.mount`
   - **توضیح:** این واحدها برای مدیریت نقاط کوه‌گذاری فایل‌سیستم‌ها استفاده می‌شوند. مشابه دستورات `mount` و `umount` در لینوکس.
   - **مثال:** `home.mount`

5. **Automount Units (واحدهای کوه‌گذاری خودکار)**
   - **پسوند فایل:** `.automount`
   - **توضیح:** این واحدها نقاط کوه‌گذاری خودکار را مدیریت می‌کنند و به `mount`ها اجازه می‌دهند به طور خودکار هنگام دسترسی، انجام شوند.
   - **مثال:** `home.automount`

6. **Swap Units (واحدهای مبادله)**
   - **پسوند فایل:** `.swap`
   - **توضیح:** این واحدها برای مدیریت فضای swap استفاده می‌شوند.
   - **مثال:** `swapfile.swap`

7. **Path Units (واحدهای مسیر)**
   - **پسوند فایل:** `.path`
   - **توضیح:** این واحدها برای نظارت بر مسیرهای فایل‌سیستم و اجرای سرویس‌ها در پاسخ به تغییرات در این مسیرها استفاده می‌شوند.
   - **مثال:** `cups.path`

8. **Timer Units (واحدهای تایمر)**
   - **پسوند فایل:** `.timer`
   - **توضیح:** این واحدها زمان‌بندی عملیات و اجرای سرویس‌ها در زمان‌های مشخص شده را مدیریت می‌کنند. مشابه cron jobs در لینوکس.
   - **مثال:** `backup.timer`

9. **Slice Units (واحدهای برش)**
   - **پسوند فایل:** `.slice`
   - **توضیح:** این واحدها برای مدیریت گروه‌های فرآیندی و تخصیص منابع استفاده می‌شوند.
   - **مثال:** `system.slice`

10. **Scope Units (واحدهای محدوده)**
    - **پسوند فایل:** `.scope`
    - **توضیح:** این واحدها برای مدیریت مجموعه‌های فرآیندی که خارج از systemd ایجاد شده‌اند، استفاده می‌شوند.
    - **مثال:** واحدهای `user.slice` برای تخصیص منابع به کاربر.

### ‍`list-unit`

دیدن مجموعه `unit` ها:

```shell
systemctl -list-units
```

### `--type`

مشص کردن نوع `unit` که میواهیم ببینیم.

`service` `socket` `target` `mount` `automount` `swap` `path` `timer` `slice` `scope`

```shell
systemd list-units --type=target
```