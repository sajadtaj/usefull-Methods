نصب `Postgres`:

```shell
apt search postgresql |grep post


apt install postgresql -y

```
دیدان کاربران و گروه ها : مشاهده میکنیم که کاربر و گروه `‍postgres` اضافه شده است . 

```shell
cat /etc/group
```
دیدن وضیعت `postgresql`

`RDBMS`
```shell
systemctl status postgresql
```
output:

    ● postgresql.service - PostgreSQL RDBMS
    Loaded: loaded (/lib/systemd/system/postgresql.service; e>
    Active: active (exited) since Sun 2024-12-29 12:18:38 +03>
    Process: 1690 ExecStart=/bin/true (code=exited, status=0/S>
    Main PID: 1690 (code=exited, status=0/SUCCESS)
    CPU: 1ms
    دسامبر 29 12:18:38 TAJ systemd[1]: Starting PostgreSQL RDBMS...
    دسامبر 29 12:18:38 TAJ systemd[1]: Finished PostgreSQL RDBMS.


`service`

```shell
systemctl s 
```
output:

    ● postgresql@14-main.service - PostgreSQL Cluster 14-main
    Loaded: loaded (/lib/systemd/system/postgresql@.service; enabled-runtime; vendor preset: enabled)
    Active: active (running) since Sun 2024-12-29 12:18:38 +0330; 53min left
    Process: 1292 ExecStart=/usr/bin/pg_ctlcluster --skip-systemctl-redirect 14-main start (code=exited, status=0/SUCCESS)
    Main PID: 1436 (postgres)
    Tasks: 7 (limit: 18180)
    Memory: 31.1M
    CPU: 319ms
    CGroup: /system.slice/system-postgresql.slice/postgresql@14-main.service
             ├─1436 /usr/lib/postgresql/14/bin/postgres -D /var/lib/postgresql/14/main -c config_file=/etc/postgresql/14/main/postgresql.conf
             ├─1450 "postgres: 14/main: checkpointer "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─1453 "postgres: 14/main: background writer "" "" "" "" "" "" "" "" "" "" "" "" "" "" ">
             ├─1454 "postgres: 14/main: walwriter "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             ├─1456 "postgres: 14/main: autovacuum launcher "" "" "" "" "" "" "" "" "" "" "" "" "" "">
             ├─1457 "postgres: 14/main: stats collector "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
             └─1458 "postgres: 14/main: logical replication launcher "" "" "" "" "" "" "" "" "" "" "">
        دسامبر 29 12:18:36 TAJ systemd[1]: Starting PostgreSQL Cluster 14-main...
        دسامبر 29 12:18:38 TAJ systemd[1]: Started PostgreSQL Cluster 14-main.


## Important Directory
در نصب PostgreSQL بر روی اوبونتو، چندین دایرکتوری مهم ایجاد می‌شوند که هر کدام محتوای خاص خود را دارند. در اینجا به مهم‌ترین آن‌ها اشاره می‌کنم:

1. **/etc/postgresql/version/main**: 

   - **محتوا:** فایل‌های پیکربندی PostgreSQL.
   - **مثال:** `postgresql.conf`, `pg_hba.conf`.

    - این دایرکتوری شامل فایل‌های پیکربندی PostgreSQL است. فایل‌های مهم شامل `postgresql.conf` برای تنظیمات کلی پایگاه داده و `pg_hba.conf` برای کنترل دسترسی به پایگاه داده می‌شود.
  
    - pg_hba.conf : `PostgreSQL hst-based Authentication`
    : وقتی می خواهیم از سایر سیستم ها و نتورک ها نیز به دیتابیس وصل بشویم  باید تنظیمات آنرا در ای قسمت انجام دهیم

2. **/var/lib/postgresql/**:
   - **محتوا:** داده‌های پایگاه داده.
   - **مثال:** دایرکتوری‌هایی که شامل داده‌ها و فایل‌های داخلی پایگاه داده می‌شوند.

    - **/var/lib/postgresql/**: داده‌های اصلی پایگاه داده در این دایرکتوری ذخیره می‌شوند. هر نسخه از PostgreSQL و هر پایگاه داده‌ای که ایجاد می‌کنید، به صورت دایرکتوری‌های جداگانه در این مسیر ذخیره می‌شود.


3. **/var/log/postgresql/**:\

   - **محتوا:** فایل‌های لاگ و ثبت رویدادها.
   - **مثال:** `postgresql-12-main.log`.

    - **/var/log/postgresql/**: فایل‌های لاگ که برای نظارت و دیباگ استفاده می‌شوند در این دایرکتوری ذخیره می‌شوند. این لاگ‌ها شامل اطلاعاتی درباره عملکرد پایگاه داده، خطاها و فعالیت‌های کاربران هستند.

4. **/usr/lib/postgresql/**:
   - **محتوا:** فایل‌های باینری و کتابخانه‌های PostgreSQL.
   - **مثال:** باینری‌های اصلی PostgreSQL مانند `psql`.

    - **/usr/lib/postgresql/**: فایل‌های باینری و کتابخانه‌های مورد نیاز برای اجرای PostgreSQL در این دایرکتوری قرار دارند. این شامل فایل‌های اجرایی مانند `psql` و کتابخانه‌های مورد نیاز برای عملکرد داخلی PostgreSQL است.

5. **/run/postgresql/**:
   - **محتوا:** فایل‌های موقت و سوکت‌ها.
   - **مثال:** فایل‌های سوکت برای ارتباط با پایگاه داده.

    - **/run/postgresql/**: فایل‌های موقت و سوکت‌ها برای ارتباط بین سرویس‌های مختلف و پایگاه داده در این مسیر قرار دارند. این دایرکتوری معمولاً حاوی فایل‌های سوکت Unix است که به کلاینت‌ها اجازه می‌دهد به پایگاه داده متصل شوند.

وارد کاربر postgre شدن:
```shell
su - postgre

# or
sudo -u postgres psql  # Enter in Postgre interactive env

```
دیدن مشخصات دیتابیس نصب شده و `وارد` دیتابیس شدن :

```shell
psql # Enter in interactive env
```

خارح شدن از محیط 
```shell
# in psql
\q
```

دیدن محل کانفیگ . محتویات `postgres`

```shell
whereis postgresql
```

دیدن دستورات `binary` مربوط بخ `postgres`

```shell
cd /usr/lib/postgresql/{version number}/bin

```

دیدن محل فایل های کانفیگ

```shell
cd /etc/postgresql/14/main

```

دیدن تعداد  دیتابیس ها 
```shell
# in psql
\l
```

دیدن پورت های که در حال شنیدن هستند.



```shell
ss
# or
ss -ntl
# or 
ss -nltp   # اینگه چه کاربر و پروسه ای در حال استفاده از پورت هست
```
میتوانیم بفهمیم چه پروسه های در حال اتصال به دیتابیس هستند و در صورت نیاز آنها را `kill` کنیم 

ساخت یوزر جدید:
```shell
# in psql
create user <name> password `1`;
```

## Create Database:

ابتدا بایست سرویس `postgres` را موقتا غیر فعال کنیم.

```shell
systemctl stop postgresql@14
```


---

قدم اول یافتن `initdb` در کاربر `postgres`

```shell
sudo find / -name initdb
```
output:

    /usr/lib/postgresql/14/bin/initdb

میتوانیم این مسیر را به `Path` سیستم اضافه کنیم.

```shell
export PATH=$PATH:/usr/lib/postgresql/14/bin/initdb
```
### `-D`

برای اتخاب مسیر دیتابیس بصورت دلخواه
یا اینکه متغیر `PGDATA` را تعریف کنیم . محلی که میخواهیم دیتا ما در آجا ذیره گردد.

>> توجه داشته باشید `PGDATA` ممکن است از قبل مقدار داشته باشد

```shell
export PGDATA=/path/to/your/data/directory
```

حالا میتوانیم دیتابیس را ایجاد نماییم:

```shell
initdb -D /yourDirection
#ex
mkdir /tmp/temp_DB # مسیر فایل از هربار خاموش شدن سیستم پاک می شود.

initdb -D /tmp/temp_DB
```

اگر مسیر را اضافه ننکرده باشیم باید به مسیر initdb  برویم و از آنجا دستور را اجرا کنیم.

```shell
cd /usr/lib/postgresql/14/bin/initdb
# then
./initdb -D /tmp/temp_DB
```
output:

    The files belonging to this database system will be owned by user "postgres".
    This user must also own the server process.

    The database cluster will be initialized with locales
    COLLATE:  en_US.UTF-8
    CTYPE:    en_US.UTF-8
    MESSAGES: en_US.UTF-8
    MONETARY: az_IR
    NUMERIC:  az_IR
    TIME:     az_IR
    The default database encoding has accordingly been set to "UTF8".
    The default text search configuration will be set to "english".

    Data page checksums are disabled.

    fixing permissions on existing directory /tmp/postgres-17 ... ok
    creating subdirectories ... ok
    selecting dynamic shared memory implementation ... posix
    selecting default max_connections ... 100
    selecting default shared_buffers ... 128MB
    selecting default time zone ... Asia/Tehran
    creating configuration files ... ok
    running bootstrap script ... ok
    performing post-bootstrap initialization ... ok
    syncing data to disk ... ok

    initdb: warning: enabling "trust" authentication for local connections
    You can change this by editing pg_hba.conf or using the option -A, or
    --auth-local and --auth-host, the next time you run initdb.

    Success. You can now start the database server using:

        ./pg_ctl -D /tmp/postgres-17/ -l logfile start



حتماً! در اینجا پیام پس از نصب دیتابیس PostgreSQL را به‌صورت تیتر و چکیده‌وار به فارسی توضیح می‌دهم:

1. **مالکیت فایل‌ها**:
   - فایل‌های مربوط به این سیستم پایگاه داده توسط کاربر "postgres" مالکیت خواهند شد.
   - این کاربر باید فرآیند سرور را نیز مالک باشد.

2. **محلی‌ها**:
   - COLLATE: en_US.UTF-8
   - CTYPE: en_US.UTF-8
   - MESSAGES: en_US.UTF-8
   - MONETARY: az_IR
   - NUMERIC: az_IR
   - TIME: az_IR

3. **کدگذاری پیش‌فرض**:
   - کدگذاری پیش‌فرض پایگاه داده به "UTF8" تنظیم شده است.

4. **پیکربندی جستجوی متن**:
   - پیکربندی پیش‌فرض جستجوی متن به "english" تنظیم خواهد شد.

5. **چکسام‌های صفحه داده**:
   - چکسام‌های صفحه داده غیرفعال هستند.

6. **تنظیم مجوزها**:
   - تنظیم مجوزها بر روی دایرکتوری موجود /tmp/postgres-17 ... موفق.

7. **ایجاد زیر-دایرکتوری‌ها**:
   - ایجاد زیر-دایرکتوری‌ها ... موفق.

8. **پیاده‌سازی حافظه مشترک پویا**:
   - انتخاب پیاده‌سازی حافظه مشترک پویا ... posix.

9. **حداکثر اتصالات**:
   - انتخاب حداکثر اتصالات پیش‌فرض ... 100.

10. **حافظه مشترک**:
    - انتخاب حافظه مشترک پیش‌فرض ... 128MB.

11. **منطقه زمانی**:
    - انتخاب منطقه زمانی پیش‌فرض ... Asia/Tehran.

12. **ایجاد فایل‌های پیکربندی**:
    - ایجاد فایل‌های پیکربندی ... موفق.

13. **اجرای اسکریپت بوت استرپ**:
    - اجرای اسکریپت بوت استرپ ... موفق.

14. **پیکربندی پس از بوت استرپ**:
    - پیکربندی پس از بوت استرپ ... موفق.

15. **همگام‌سازی داده‌ها**:
    - همگام‌سازی داده‌ها به دیسک ... موفق.

16. **احراز هویت "trust"**:
    - هشدار: فعال‌سازی احراز هویت "trust" برای اتصالات محلی.
    - می‌توانید این را با ویرایش فایل pg_hba.conf یا استفاده از گزینه -A، یا --auth-local و --auth-host، دفعه بعد که initdb را اجرا می‌کنید، تغییر دهید.

17. **موفقیت‌آمیز بودن فرآیند**:
    - اکنون می‌توانید سرور پایگاه داده را با استفاده از این دستور شروع کنید:
    ```sh
    ./pg_ctl -D /tmp/postgres-17/ -l logfile start
    ```

## راه اندازی سرویس `postgresql`

بعد از تعریف دیتابیس باید مجدد سرویس را بالا بیاریم توجه داشته باشید ممک است کاربر pstgres اختیار ایکار را ننداشته باشد و مجبور باشید از کاربر بالاتری کمک بگیریم.




```shell
./pg_ctl -D /tmp/temp_DB/ start 
```

`/tmp/temp_DB/` : این ادرس را بالاتر برای نگهداری اطلاعات دیتابس ساختیم

>> ./pg_ctl: No such file or directory

`./pg_ctl` : برای اجرای این دستورباید در دایرکتوری `/usr/lib/postgresql/14/bin` باشید. برای اینکه بفهمید برای اجرای این ددستور دقیقا باید در چه محیطی باشید میتوانید از دستور زیر کمک بگیرید:

```shell
sudo find / -name pg_ctl
```

