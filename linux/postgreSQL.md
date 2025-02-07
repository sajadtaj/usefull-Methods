# 1. نصب `Postgres`:

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
systemctl status postgresql@14-main.service  
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

# 2.Important Directory

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
3. **/var/log/postgresql/**:

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
su - postgres

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

# 3. پیدا کردن محل فایل های مختتلف

در هنگام نصب دیتابیس postgresql فایل های مهم آن در ای مسیر ها ذخیره می شود.
اما اگر بخواهیم که خودمان دیتابیس را صب کنیم میتوایم به کمک فلگ `-D` مشخص کنیم محل استقرار دیتابیس را

## Data Directory

یافتن محا نگهداری فایل ها `data`

```shell
sudo -u postgres psql -c 'SHOW data_directory;'
```

output:

    sudo -u postgres psql -c 'SHOW data_directory;'

## Log

دو محل برای نگهداری لاگ ها داریم در خخصوص pstgreSQL

+ `/var/log/postgresql/`
+ `/usr/lib/postgresql/14/bin/logfile `

### 1. /usr/lib/postgresql/14/bin/logfile

ماهیت: این فایل می‌تواند یک لاگ موقت یا کاربردی در مسیر باینری‌های PostgreSQL باشد.

کاربرد:

+ معمولاً این نوع فایل‌ها برای اجرای مستقیم دستورات باینری استفاده می‌شوند، یا به عنوان لاگ‌هایی مرتبط با اسکریپت‌های تستی یا ابزارهای خاص که با نسخه‌ی خاصی از PostgreSQL کار می‌کنند، ایجاد می‌شوند.
+ احتمالاً توسط خود PostgreSQL تولید نشده باشد و نتیجه اجرای دستی یک ابزار باشد.

موقعیت:

در مسیر باینری‌های PostgreSQL ذخیره شده که ابزارهای مرتبط با اجرای نسخه‌ی خاصی از PostgreSQL را در خود جای می‌دهد.
دسترسی به این مسیر معمولاً برای کاربران عادی محدود است و بیشتر سیستم‌ادمین‌ها یا کاربران خاص به آن دسترسی دارند.

### 2. /var/log/postgresql

ماهیت:
این مسیر محل پیش‌فرض ثبت لاگ‌های سیستم PostgreSQL است که توسط سرویس اصلی پایگاه داده مدیریت می‌شود.
کاربرد:
شامل لاگ‌های مختلف نظیر:

+ لاگ‌های عملیاتی : شروع و توقف سرویس‌ها
+ لاگ‌های خطا: خطاهای سیستمی یا مرتبط با اجرای Queryها
+ لاگ‌های دسترسی : اطلاعات درباره‌ی کاربرانی که به پایگاه داده متصل شده‌اند
+ این فایل‌ها به طور پیش‌فرض توسط سیستم لاگینگ PostgreSQL (مانند log_directory و log_destination) مدیریت و تولید می‌شوند.

موقعیت:

+ در مسیر پیش‌فرض لاگ‌های سیستم (مانند /var/log/) ذخیره شده و نیازمند دسترسی ریشه‌ای (root) یا دسترسی کاربران خاص سرویس PostgreSQL است.
+ این مسیر به صورت مداوم و پویا به‌روزرسانی می‌شود.

## config Directory

یافتن محا نگهداری فایل ها `config`

```shell
sudo -u postgres psql -c 'SHOW config_file;'
```

output:

    /etc/postgresql/14/main/postgresql.conf

# 4.Create Database cluster:

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
>>

```shell
export PGDATA=/path/to/your/data/directory
```

حالا میتوانیم دیتابیس را ایجاد نماییم:

```shell
./initdb -D /yourDirection
#ex
mkdir /tmp/temp_DB # مسیر فایل از هربار خاموش شدن سیستم پاک می شود.

./initdb -D /tmp/temp_DB
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

    ./pg_ctl -D /tmp/temp_DB/ -l logfile start

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

## `logfile`

>> ### نکته مهم :
>>

    اگر فایل مربوط به`logfile` در دسترس نبود میتوایم خودمان یک فایل با ام مشخص `logfile` در مسیر دلخواه درست کیم و با آن پروزه را اغاز کنیم.

    مثال

```shell
mkdir /yourdirect
touch /yourdirect/logfile

# سپس دیتابیس را بالا بیاریم

./pg_ctl -D /tmp/temp_DB/ -l /tmp/logfile_tmp/logfile start

# اگر دیتابیس بالا نیامد میتوانیم لاگ های آنرا از مسیر زیر بررسی کننیم

cat /yourdirect/logfile
```

## `Data`

#### مشخص نمودن مسیر دیتا Data directry

می توانیم از طریق فایل postgres.conf و خط که توضیحات مسیر دیتا را داده است مسیر نگهداری دیتا را مشخص کنیم.فایل های `pg_hba`  و `pg_ident` در ای مسیر قرار میگیرند. باید قبل از آن سرویس `postgres را متوقف `کرده باشیم و بعد از اعمال تغییرات مجددا آنرا بالا بیاوریم.

```shell
#  in directory postgres init like : tmp/temp_db
/tmp/temp_db$ grep 'data' postgresql.conf 
```

    برای تغییر مسیر ذخیره دیتا باید مسیر زیر را تغییر دهیم به مسیر دلخواه

Output:

    data_directory = 'ConfigDir'		# use data in another directory

## راه اندازی سرویس `postgresql`

بعد از تعریف دیتابیس باید مجدد سرویس را بالا بیاریم توجه داشته باشید ممک است کاربر postgres اختیار اینکار را نداشته باشد و مجبور باشید از کاربر بالاتری کمک بگیریم.

```shell
./pg_ctl -D /tmp/temp_DB/ start 
```

`/tmp/temp_DB/` : این ادرس را بالاتر برای نگهداری اطلاعات دیتابس ساختیم

>> ./pg_ctl: No such file or directory
>>

`./pg_ctl` : برای اجرای این دستورباید در دایرکتوری `/usr/lib/postgresql/14/bin` باشید. برای اینکه بفهمید برای اجرای این ددستور دقیقا باید در چه محیطی باشید میتوانید از دستور زیر کمک بگیرید:

```shell
sudo find / -name pg_ctl
# عدم نمایش خطوط permissuin denied
find / -name pg_ctl 2>/dev/null
```

---

# 5. `pg_hba`.conf

 فایل **pg_hba.conf** مشخص می‌کند که چه کسانی می‌توانند به دیتابیس‌ها دسترسی داشته باشند و چگونه احراز هویت می‌شوند. این تنظیمات به چهار بخش اصلی تقسیم می‌شود: **type**، **database**، **user**، **address**، و **method**.

### بخش‌های اصلی

1. **type**     : نوع اتصال (محلی یا از راه دور).
2. **database** : نام دیتابیس یا دیتابیس‌هایی که دسترسی به آنها مجاز است.
3. **user**     : کاربر یا کاربران مجاز برای دسترسی.
4. **address**  : آدرس IP یا محدوده‌ای از آدرس‌های IP که اجازه دسترسی دارند.
5. **method**   : روش احراز هویت.

### مثال‌های کاربردی

#### مثال 1: احراز هویت با استفاده از `md5`

فرض کنید می‌خواهید فقط کاربر `user1` از شبکه محلی با آدرس 192.168.1.0/24 به دیتابیس `mydb` دسترسی داشته باشد و احراز هویت با استفاده از روش `md5` انجام شود.

```plaintext
host mydb user1 192.168.1.0/24 md5
```

#### مثال 2: احراز هویت با استفاده از `trust`

اگر می‌خواهید همه کاربران به دیتابیس‌ها از طریق اتصالات محلی بدون نیاز به رمز عبور دسترسی داشته باشند، می‌توانید از روش `trust` استفاده کنید.

```plaintext
host all all 127.0.0.1/32 trust
```

#### مثال 3: احراز هویت با استفاده از `scram-sha-256`

برای افزایش امنیت، می‌توانید از روش `scram-sha-256` استفاده کنید. در این مثال، همه کاربران از شبکه 10.0.0.0/16 به همه دیتابیس‌ها با استفاده از این روش دسترسی دارند.

```plaintext
host all all 10.0.0.0/16 scram-sha-256
```

#### مثال 4: احراز هویت برای اتصالات SSL

اگر می‌خواهید فقط اتصالات SSL اجازه دسترسی داشته باشند و با استفاده از روش `cert` احراز هویت شوند، می‌توانید از این پیکربندی استفاده کنید.

```plaintext
hostssl all all 192.168.1.0/24 cert
```

### توضیحات مختصر برای هر بخش

- **type**:

  - `local`: اتصالات محلی از طریق سوکت‌های یونیکس.
  - `host`: اتصالات از راه دور با هر نوع (TCP/IP).
  - `hostssl`: اتصالات از راه دور با استفاده از SSL.
  - `hostnossl`: اتصالات از راه دور بدون استفاده از SSL.
- **database**:

  - `all`: تمام دیتابیس‌ها.
  - نام دیتابیس مشخص: مثلاً `mydb`.
- **user**:

  - `all`: تمام کاربران.
  - نام کاربر مشخص: مثلاً `user1`.
- **address**:

  - آدرس IP یا محدوده‌ای از آدرس‌های IP: مثلاً `192.168.1.0/24`.
- **method**:

  - `trust`: بدون نیاز به رمز عبور.
  - `md5`: احراز هویت با استفاده از رمز عبور رمزنگاری‌شده.
  - `scram-sha-256`: احراز هویت با استفاده از روش SCRAM-SHA-256.
  - `cert`: احراز هویت با استفاده از گواهینامه SSL/TLS.

## مثال

برای این که "علی" بتواند به دیتابیس `price` از سیستم خودش متصل شود و از یک روش احراز هویت مطمعن استفاده کند، می‌توانیم از روش احراز هویت `scram-sha-256`  استفاده کنیم. این روش‌ رمزهای عبور را به صورت رمزنگاری شده ارسال می‌کند و امنیت بیشتری را فراهم می‌کند.

### نمونه تنظیمات برای فایل `pg_hba.conf`

1. **تنظیمات برای احراز هویت با `scram-sha-256`:**

   ```plaintext
   host price ali 192.168.1.100/32 scram-sha-256
   ```

### توضیحات

- **type**: نوع اتصال (در اینجا `host` به معنی اتصال از راه دور).
- **database**: نام دیتابیس (`price`).
- **user**: نام کاربر (`ali`).
- **address**: آدرس IP یا محدوده‌ای از آدرس‌های IP که اجازه دسترسی دارند (مثلاً `192.168.1.100/32` که به معنی یک سیستم خاص با آدرس IP 192.168.1.100 است).
- **method**: روش احراز هویت (`scram-sha-256` یا `md5`).

### نکته‌ها

1. **احراز هویت با `scram-sha-256`**: این روش از الگوریتم SCRAM-SHA-256 برای رمزنگاری رمز عبور استفاده می‌کند و امنیت بالاتری نسبت به `md5` دارد.
   ```plaintext
   host price ali 192.168.1.100/32 scram-sha-256
   ```

با این تنظیمات، "علی" می‌تواند به دیتابیس `price` از سیستم خودش با یک روش احراز هویت مطمعن متصل شود.

    # TYPE  DATABASE        USER            ADDRESS                 METHOD

    host    price           ali             192.168.1.100/32        scram-sha-256

    # "local" is for Unix domain socket connections only
    local   all             all                                     peer
    # IPv4 local connections:
    host    all             all             127.0.0.1/32            scram-sha-256
    # IPv6 local connections:
    host    all             all             ::1/128                 scram-sha-256
    # Allow replication connections from localhost, by a user with the
    # replication privilege.
    local   replication     all                                     peer
    host    replication     all             127.0.0.1/32            scram-sha-256
    host    replication     all             ::1/128                 scram-sha-256

---

    # TYPE   DATABASE  USER    ADDRESS        METHOD
    # "local" is for Unix domain socket connections only
    local    all       all                    peer

این خط اتصالات محلی (local) را از طریق سوکت‌های یونیکس برای تمامی دیتابیس‌ها (all) و تمامی کاربران (all) تعریف می‌کند. روش احراز هویت peer به این معناست که نام سیستم‌عامل کاربر باید با نام کاربر پایگاه داده مطابقت داشته باشد.

    # TYPE   DATABASE  USER    ADDRESS      METHOD
    # IPv4 local connections:
    host     all       all     127.0.0.1/32 scram-sha-256

این خط اتصالات IPv4 محلی را برای تمامی دیتابیس‌ها (all) و تمامی کاربران (all) با آدرس IP 127.0.0.1/32 تعریف می‌کند. روش احراز هویت scram-sha-256 برای رمزنگاری امن رمز عبور استفاده می‌شود.

    # TYPE   DATABASE  USER    ADDRESS      METHOD
    # IPv6 local connections:
    host     all       all     ::1/128      scram-sha-256

این خط اتصالات IPv6 محلی را برای تمامی دیتابیس‌ها (all) و تمامی کاربران (all) با آدرس IP ::1/128 تعریف می‌کند. روش احراز هویت scram-sha-256 برای رمزنگاری امن رمز عبور استفاده می‌شود.

    # TYPE   DATABASE     USER    ADDRESS        METHOD
    # Allow replication connections from localhost, by a user with the
    # replication privilege.
    local   replication   all                       peer
    host    replication   all    127.0.0.1/32      scram-sha-256
    host    replication   all    ::1/128           scram-sha-256

**Replication**: replication به فرآیندی اطلاق می‌شود که در آن داده‌های پایگاه داده از یک سرور (primary) به سرورهای دیگر (standby) کپی می‌شود. این فرآیند به منظور پشتیبان‌گیری، تعادل بار، و بهبود دسترسی پایگاه داده انجام می‌شود. این تنظیمات معمولاً در محیط‌های تولیدی که نیاز به عملیات replication امن و محدود به سیستم محلی دارند، بسیار مهم هستند.

---

#### `Reload` کردن تنظیمات در دیتابیس

```shell
./pg_ctl -D /محل ایجاد دیتتابیس/ reload
 vmnbv ```

### دیدن `rules` های درون دیتابیس

```postgres
in_datbase =# select * from pg_hba_file_rules(); 
```

> output

    line_number | type  |   database    | user_name |  address  |                 netmask                 | auth_method | options | error
    -------------+-------+---------------+-----------+-----------+-----------------------------------------+-------------+---------+-------
          89 | local | {all}         | {all}     |           |                                         | trust       |         |
          91 | host  | {all}         | {all}     | 127.0.0.1 | 255.255.255.255                         | trust       |         |
          93 | host  | {all}         | {all}     | ::1       | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | trust       |         |
          96 | local | {replication} | {all}     |           |                                         | trust       |         |
          97 | host  | {replication} | {all}     | 127.0.0.1 | 255.255.255.255                         | trust       |         |
          98 | host  | {replication} | {all}     | ::1       | ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff | trust       |         |
    (6 rows)

# 5. postgresql.conf

فایل `postgresql.conf` نقش بسیار مهمی در تنظیم و مدیریت رفتار و عملکرد سرور PostgreSQL ایفا می‌کند. این فایل شامل مجموعه‌ای از تنظیمات پیکربندی است که جنبه‌های مختلف عملکرد پایگاه داده را کنترل می‌کنند. در اینجا برخی از وظایف کلیدی این فایل آورده شده است:

1. **تنظیمات شبکه و اتصال**:

 این فایل پورت TCP که سرور روی آن گوش می‌دهد و تعداد حداکثر اتصالات همزمان را تعیین می‌کند.

2. **مدیریت حافظه**:

تنظیمات مربوط به حافظه مورد استفاده برای کش کردن داده‌ها، عملیات‌های داخلی و نگهداری را مشخص می‌کند.

3. **ثبت گزارش**:

تنظیمات مربوط به مکان ذخیره‌سازی فایل‌های گزارش، الگوی نامگذاری آنها و نوع دستورات SQL که باید ثبت شوند را شامل می‌شود.

4. **پشتیبان‌گیری و تکثیر**:

 سطح اطلاعات نوشته شده در سیستم WAL، که برای پشتیبان‌گیری و تکثیر اهمیت دارد، را تعیین می‌کند.

5. **بهینه‌سازی عملکرد**:

تنظیمات مختلفی برای بهینه‌سازی عملکرد پایگاه داده، شامل مقدار حافظه قابل استفاده برای عملیات مرتب‌سازی و نگهداری و تخمین حافظه کلی موجود برای کش کردن داده‌ها.

این تنظیمات در فایل `postgresql.conf` به مدیران پایگاه داده اجازه می‌دهند تا عملکرد سرور PostgreSQL را به بهترین نحو تنظیم کنند. با تنظیم صحیح این فایل، می‌توانید عملکرد و امنیت پایگاه داده را بهینه کنید.
 در اینجا تعدادی از تنظیمات مهم در فایل `postgresql.conf` به صورت فهرست وار توضیح داده شده‌اند:

1. **port**:

 مشخص می‌کند که سرور بر روی کدام پورت TCP گوش می‌دهد.

```plaintext
   port = 5432
```

   اگر آنرا تغییر دادیم میتوانی از ددستور زیر استفاده کیم

```shell
   export PGPORT=5432
```

2. **max_connections**:

تعداد حداکثر اتصالات همزمان به پایگاه داده را تعیین می‌کند.

```plaintext
   max_connections = 100
```

3. **shared_buffers**:

 میزان حافظه‌ای که برای کش داده‌ها به PostgreSQL اختصاص داده می‌شود.

```plaintext
   shared_buffers = 128MB
```

4. **logging_collector**:

فعال یا غیرفعال کردن جمع‌آوری گزارش‌ها.

```plaintext
   logging_collector = on
```

5. **log_directory**:

دایرکتوری که فایل‌های گزارش در آن ذخیره می‌شوند را مشخص می‌کند.

```plaintext
   log_directory = 'pg_log'
```

6. **log_filename**:

 الگوی نامگذاری فایل‌های گزارش را تعیین می‌کند.

```plaintext
   log_filename = 'postgresql-%Y-%m-%d_%H%M%S.log'
```

7. **log_statement**:

مشخص می‌کند که کدام دستورات SQL ثبت شوند.

```plaintext
   log_statement = 'all'
```

8. **wal_level**:

سطح اطلاعات نوشته شده در سیستم WAL (Write-Ahead Logging) را تعیین می‌کند که برای تکثیر و پشتیبان‌گیری مهم است.

```plaintext
   wal_level = replica
```

9. **checkpoint_timeout**:

 حداکثر زمانی که بین نقاط بازآغاز خودکار WAL می‌گذرد را تعیین می‌کند.

```plaintext
   checkpoint_timeout = 5min
```

10. **work_mem**:

میزان حافظه‌ای که برای عملیات مرتب‌سازی داخلی و جدول‌های هش استفاده می‌شود قبل از نوشتن به فایل‌های موقت دیسک را تعیین می‌کند.

```plaintext
    work_mem = 4MB
```

11. **maintenance_work_mem**:

حداکثر حافظه‌ای که برای عملیات نگهداری مانند VACUUM، CREATE INDEX و ALTER TABLE ADD FOREIGN KEY استفاده می‌شود را تعیین می‌کند.

```plaintext
    maintenance_work_mem = 64MB
```

12. **effective_cache_size**:

تخمینی از مجموع حافظه موجود برای کش کردن دیسک توسط سیستم‌عامل و درون خود پایگاه داده است.

```plaintext
    effective_cache_size = 4GB
```

# 6.نحوه ایجاد کاربر و تنظیمات دسترسی

 چگونه  یک کاربر را در فایل `pg_hba.conf` تعریف کنید و به او دسترسی به دیتابیس مورد نظر بدهید:

1. **تعریف کاربر در فایل `pg_hba.conf`**:

   - فایل `pg_hba.conf` را باز کنید:

     ```bash
     sudo nano /محل ایجاد دیتتابیس/pg_hba.conf
     ```
   - در این فایل، یک خط مشابه زیر اضافه کنید:

     ```ini
     local    all             ali                                     password
     ```
   - فایل را ذخیره کنید و خارج شوید. در `nano`، می‌توانید با فشار دادن `Ctrl+O` برای ذخیره و `Ctrl+X` برای خروج این کار را انجام دهید.
   - تنظیمات PostgreSQL را برای اعمال تغییرات، مجدد بارگذاری کنید:

     ```bash
     sudo systemctl reload postgresql

     # یا

     ./pg_ctl -D /محل ایجاد دیتتابیس/ reload
     ```
2. **ایجاد کاربر در PostgreSQL**:

   - به کاربر `postgres` سوئیچ کنید و به خط فرمان PostgreSQL دسترسی پیدا کنید:

     ```bash
     sudo -i -u postgres
     psql
     ```
   - یک کاربر جدید (role) به نام "ali" ایجاد کنید و برای آن یک رمز عبور تنظیم کنید:

     ```sql
     CREATE ROLE ali WITH LOGIN PASSWORD 'your_password';
     ```
3. **ایجاد دیتابیس**:

   - دیتابیس جدیدی به نام مثلاً "mydatabase" ایجاد کنید:
     ```sql
     CREATE DATABASE mydatabase;
     ```
4. **اعطای دسترسی‌ها**:

   - دسترسی‌های لازم را به کاربر "ali" اعطا کنید تا بتواند به دیتابیس "mydatabase" دسترسی داشته باشد:

     ```sql
     GRANT ALL PRIVILEGES ON DATABASE mydatabase TO ali;
     ```
   - از خط فرمان PostgreSQL خارج شوید:

     ```sql
     \q
     ```
   - از حالت کاربر `postgres` خارج شوید:

     ```bash
     exit
     ```
5. **اتصال به دیتابیس**:

   - حالا می‌توانید با استفاده از کاربر "ali" به دیتابیس "mydatabase" وصل شوید:
     ```bash
     psql -U ali -h localhost -p 5433 -d mydatabase
     ```

# 8. متغیر های محیطی

برای اتصال به پایگاه داده PostgreSQL با توجه به متغیرهای محیطی که تعریف کردید، می‌توانید از دستور زیر استفاده کنید:

```bash
psql
```

این دستور از متغیرهای محیطی که قبلاً تنظیم کرده‌اید برای اتصال به پایگاه داده استفاده می‌کند.

به عنوان مثال، اگر متغیرهای محیطی را به این صورت تنظیم کرده‌اید:

```bash
export PGUSER=your_username
export PGPASSWORD=your_password
export PGHOST=localhost
export PGPORT=5432
export PGDATABASE=your_database_name
```

فقط کافیست دستور `psql` را اجرا کنید و به پایگاه داده متصل شوید.

`اگر` متغیرهای محیطی را تنظیم نکرده‌اید و می‌خواهید همه‌ی اطلاعات را در یک دستور بدهید، می‌توانید از دستور زیر استفاده کنید:

```bash
psql -U your_username -h localhost -p 5432 -d your_database_name
```

این دستور به صورت کامل شامل نام کاربری، میزبان، پورت و نام پایگاه داده است.

میتتواید لیست کامل این متغیر ها را از اپرس زیر ببیید:

>> https://www.postgresql.org/docs/current/libpq-envars.html
>>

# 9. جداول مهم

حتماً! در PostgreSQL، تعدادی جدول سیستمی وجود دارند که برای مدیریت و نگهداری دیتابیس استفاده می‌شوند. در اینجا لیستی از مهم‌ترین جداول سیستمی به همراه توضیحات نقش هر کدام آورده شده است:

1. **pg_database**:

   - **نقش**: اطلاعات مربوط به دیتابیس‌های موجود در سرور PostgreSQL را نگهداری می‌کند.
2. **pg_user**:

   - **نقش**: اطلاعات مربوط به کاربران دیتابیس را نگهداری می‌کند. (جدولی که قبلاً به آن اشاره کردید)
3. **pg_roles**:

   - **نقش**: اطلاعات مربوط به نقش‌ها (Roles) که شامل کاربران و گروه‌های کاربری است را نگهداری می‌کند.
4. **pg_tables**:

   - **نقش**: لیستی از تمامی جداول موجود در دیتابیس را نگهداری می‌کند.
5. **pg_indexes**:

   - **نقش**: اطلاعات مربوط به ایندکس‌های جداول را نگهداری می‌کند.
6. **pg_attribute**:

   - **نقش**: اطلاعات مربوط به ستون‌های جداول را نگهداری می‌کند.
7. **pg_class**:

   - **نقش**: اطلاعات مربوط به کلاس‌های دیتابیس از جمله جداول، ایندکس‌ها، و سایر موجودیت‌ها را نگهداری می‌کند.
8. **pg_namespace**:

   - **نقش**: اطلاعات مربوط به اسکیماها (Schemas) را نگهداری می‌کند.
9. **pg_constraint**:

   - **نقش**: اطلاعات مربوط به محدودیت‌ها (Constraints) مانند کلیدهای اصلی و خارجی را نگهداری می‌کند.
10. **pg_stat_activity**:

    - **نقش**: اطلاعات مربوط به فعالیت‌های فعلی دیتابیس، شامل جلسات کاربران و پرس و جوهای در حال اجرا را نگهداری می‌کند.

مثال:

```postgresql
select * from pg_user;

```

Output:

    rolname          | rolsuper | rolinherit | rolcreaterole | rolcreatedb | rolcanlogin | rolreplication | rolconnlimit | rolpassword | rolvaliduntil | rolbypassrls | rolconfig | oid
    ---------------------------+----------+------------+---------------+-------------+-------------+----------------+--------------+-------------+---------------+--------------+-----------+------
      postgres                  | t        | t          | t             | t           | t           | t              |           -1 | ********    |               | t            |           |   10
      pg_database_owner         | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 6171
      pg_read_all_data          | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 6181
      pg_write_all_data         | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 6182
      pg_monitor                | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 3373
      pg_read_all_settings      | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 3374
      pg_read_all_stats         | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 3375
      pg_stat_scan_tables       | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 3377
      pg_read_server_files      | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 4569
      pg_write_server_files     | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 4570
      pg_execute_server_program | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 4571
      pg_signal_backend         | f        | t          | f             | f           | f           | f              |           -1 | ********    |               | f            |           | 4200
      (12 rows)

# 10.Tablespace

در PostgreSQL، **Tablespace** ها مکان‌های فیزیکی در سیستم فایل هستند که داده‌های دیتابیس‌ها در آنجا ذخیره می‌شوند. استفاده از Tablespace ها به شما امکان می‌دهد تا کنترل بیشتری بر توزیع داده‌ها در دیسک‌های مختلف داشته باشید و کارایی را بهینه کنید.

برای ایجاد یک Tablespace جدید، ابتدا باید یک دایرکتوری در سیستم فایل خود ایجاد کنید که PostgreSQL به آن دسترسی داشته باشد. سپس می‌توانید از دستور SQL زیر استفاده کنید تا یک Tablespace جدید بسازید:

`در PostgreSQL، برای ایجاد یک **پایگاه داده** و تنظیم **tablespace** (فضای ذخیره‌سازی سفارشی برای داده‌ها) می‌توانید از دستورات زیر استفاده کنید.

## 10.1 **مراحل ایجاد پایگاه داده و tablespace در PostgreSQL**

### 1. **ایجاد یک Tablespace**

ابتدا یک دایرکتوری برای tablespace ایجاد کنید (باید متعلق به کاربر `postgres` باشد):

```bash
sudo mkdir -p /var/lib/postgresql/tablespaces/my_tablespace
sudo chown -R postgres:postgres /var/lib/postgresql/tablespaces/my_tablespace
```

سپس در PostgreSQL، tablespace را ایجاد کنید:

```sql
CREATE TABLESPACE my_tablespace 
LOCATION '/var/lib/postgresql/tablespaces/my_tablespace';
```

### 2. **ایجاد یک پایگاه داده با استفاده از tablespace**

```sql
CREATE DATABASE my_database 
WITH TABLESPACE = my_tablespace;
```

### 3. **ایجاد جدول در Tablespace مورد نظر**

اگر بخواهید یک جدول را در این tablespace ذخیره کنید:

```sql
CREATE TABLE my_table (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
) TABLESPACE my_tablespace;
```

### **بررسی Tablespace پایگاه داده**

برای مشاهده tablespace یک پایگاه داده:

```sql
SELECT datname, spcname 
FROM pg_database d
LEFT JOIN pg_tablespace t ON d.dattablespace = t.oid;
```

دیدن لیست `Tablespace` در کلاستر

```bash
select * from pg_tablespace ;
```

### **حذف Tablespace**

برای حذف tablespace (بعد از انتقال یا حذف جداول مرتبط):

```sql
DROP TABLESPACE my_tablespace;
```

#### **نکات مهم:**

- `tablespace` یک فضای ذخیره‌سازی برای جداول و ایندکس‌ها در یک مسیر خاص است.
- فقط **superuser** یا کاربری با سطح دسترسی بالا می‌تواند tablespace ایجاد کند.
- قبل از حذف یک tablespace باید تمام جداول ذخیره‌شده در آن را منتقل یا حذف کنید.

در این دایرکتوری، PostgreSQL فایل‌هایی ایجاد خواهد کرد که داده‌های جداول و ایندکس‌هایی که در این Tablespace قرار داده شده‌اند، ذخیره می‌کند. این فایل‌ها شامل بلوک‌های داده و سایر اطلاعات مرتبط با دیتابیس خواهند بود.

## 10.2 **تغییر محل یک Tablespace در PostgreSQL**

در PostgreSQL، **tablespace** مکانی در سیستم فایل است که داده‌های پایگاه داده در آن ذخیره می‌شوند. گاهی اوقات نیاز است که مکان آن را تغییر دهیم. سناریوهای مختلفی برای این کار وجود دارد که باید با دقت اجرا شوند تا از بروز مشکلاتی مانند خرابی داده‌ها یا از دست رفتن اطلاعات جلوگیری شود.

---

### سناریوهای تغییر مکان Tablespace

#### 1. انتقال tablespace به یک دیسک یا پارتیشن جدید برای بهبود عملکرد یا افزایش فضا

 **مثال:** فرض کنید فضای `/var/lib/postgresql/tablespaces` پر شده است و می‌خواهید آن را به `/mnt/new_disk/tablespaces` منتقل کنید.

#### 2️. انتقال به یک سرور جدید برای مهاجرت (Migration)

 **مثال:** اگر سرور PostgreSQL را به ماشین جدیدی منتقل می‌کنید، ممکن است بخواهید محل tablespace را نیز تغییر دهید.

#### 3️. بهینه‌سازی ذخیره‌سازی بر اساس نوع داده

 **مثال:** می‌خواهید ایندکس‌ها را در یک SSD و جداول حجیم را در یک هارد معمولی (HDD) نگه دارید.

---

### نکاتی که باید در نظر گرفت

+ **داده‌ها را قبل از انتقال حتماً پشتیبان بگیرید (Backup)**
+ **بررسی کنید که tablespace شامل چه جداولی است**
+ **اتصال کاربران به پایگاه داده را متوقف کنید** (تا در حین انتقال، تغییراتی روی داده‌ها انجام نشود)
+ **مطمئن شوید که دسترسی‌های لازم برای PostgreSQL روی مسیر جدید تنظیم شده است**
+ **بررسی کنید که سرور به درستی بعد از تغییر محل tablespace اجرا می‌شود**

---

## *روش تغییر محل یک Tablespace*

### 1. *بررسی محل فعلی tablespace*

قبل از هر کاری، بررسی کنید که tablespace در چه مسیری قرار دارد:

```sql
SELECT spcname, pg_tablespace_location(oid) 
FROM pg_tablespace;
```

### 2.  متوقف کردن سرویس PostgreSQL

```bash
sudo systemctl stop postgresql
```

### 3.  انتقال فیزیکی داده‌ها به محل جدید

```bash
mv /var/lib/postgresql/tablespaces/my_tablespace /mnt/new_disk/tablespaces/
```

### 4.  تغییر مسیر symbolic link در PostgreSQL

برای اطمینان از اینکه PostgreSQL محل جدید را بشناسد، یک لینک نمادین ایجاد کنید:

```bash
ln -s /mnt/new_disk/tablespaces/my_tablespace /var/lib/postgresql/tablespaces/my_tablespace
```

### 5. تنظیم مجوزهای دسترسی

```bash
chown -R postgres:postgres /mnt/new_disk/tablespaces/my_tablespace
chmod 700 /mnt/new_disk/tablespaces/my_tablespace
```

### 6. راه‌اندازی مجدد PostgreSQL

```bash
sudo systemctl start postgresql
```

### 7. بررسی تغییرات

```sql
SELECT spcname, pg_tablespace_location(oid) 
FROM pg_tablespace;
```

---

## 10.3 روش جایگزین: ایجاد Tablespace جدید و انتقال جداول

اگر نمی‌خواهید مستقیماً محل tablespace را تغییر دهید، می‌توانید یک **tablespace جدید** ایجاد کنید و جداول را منتقل کنید.

### 1.  ایجاد tablespace جدید

```sql
CREATE TABLESPACE new_tablespace 
LOCATION '/mnt/new_disk/tablespaces/new_tablespace';
```

### 2️. انتقال جداول به tablespace جدید

```sql
ALTER TABLE my_table SET TABLESPACE new_tablespace;
```

### 3️. بررسی انتقال

```sql
SELECT tablename, tablespace 
FROM pg_tables 
WHERE tablename = 'my_table';
```

### 4️. حذف tablespace قدیمی (در صورت عدم نیاز)

```sql
DROP TABLESPACE old_tablespace;
```

---

✔ اگر بخواهید مسیر فیزیکی tablespace را تغییر دهید، باید داده‌ها را به صورت **دستی** جابه‌جا کنید.
✔ اگر بخواهید فقط جداول خاصی را منتقل کنید، می‌توانید از `ALTER TABLE ... SET TABLESPACE` استفاده کنید.
✔ همیشه **پشتیبان‌گیری از داده‌ها** و **توقف سرویس PostgreSQL** را قبل از اعمال تغییرات انجام دهید.

# 11. pg_wal در PostgreSQL   

`pg_wal` (مخفف **"Write-Ahead Logging"**) یک دایرکتوری مهم در PostgreSQL است که شامل لاگ‌های تراکنشی پایگاه داده می‌شود. این مکانیزم به PostgreSQL کمک می‌کند تا **دوام (durability) داده‌ها** را تضمین کرده و در صورت خرابی یا قطع شدن سیستم، داده‌ها را بازیابی کند.  

---

## **کارکرد `pg_wal`**  
در PostgreSQL، تمام تغییرات داده‌ای ابتدا در **WAL (Write-Ahead Log)** ثبت می‌شوند، سپس داده‌ها به دیسک نوشته می‌شوند. این روش باعث می‌شود که حتی در صورت خرابی، سیستم بتواند با استفاده از WAL تغییرات انجام‌شده را مجدداً اعمال کند.  

### **مراحل نوشتن داده در PostgreSQL:**  
1. ابتدا تغییرات در WAL (داخل `pg_wal/`) نوشته می‌شوند.  
2. سپس این تغییرات در بافر حافظه اعمال می‌شوند.  
3. در نهایت، پس از یک **checkpoint**، داده‌های دائمی در فایل‌های داده ذخیره می‌شوند.  

### **مزایا:**  
- افزایش قابلیت بازیابی (recovery) در صورت خرابی سیستم  
- بهبود عملکرد نوشتن داده‌ها از طریق پردازش دسته‌ای  
- امکان replication و Point-In-Time Recovery (PITR)  

---

## **محل `pg_wal` در PostgreSQL**  
به طور پیش‌فرض، `pg_wal` در دایرکتوری داده‌های PostgreSQL ذخیره می‌شود. می‌توانید محل آن را با دستور زیر بررسی کنید:  

```sql
# in sql
SHOW data_directory;
```  
```shell
#in terminal
find / -name 'pg_wal' 2>/dev/null/
```

در خروجی، مسیر داده‌های PostgreSQL نمایش داده می‌شود. درون این مسیر، `pg_wal/` قرار دارد.  

مثلاً در یک نصب استاندارد:  
```bash
ls /var/lib/postgresql/14/main/pg_wal
```  

---

## **مدیریت `pg_wal`**  

### **بررسی اندازه `pg_wal`**  
```sql
SELECT * FROM pg_ls_waldir();
```  
یا در سیستم‌عامل:  
```bash
du -sh /var/lib/postgresql/14/main/pg_wal
```  

### **تغییر مسیر `pg_wal` به یک دیسک دیگر**  
اگر `pg_wal` بیش از حد بزرگ شد یا نیاز به دیسک سریع‌تری داشتید، می‌توانید مسیر آن را تغییر دهید.  

#### **روش تغییر مسیر `pg_wal`**  
1. **خاموش کردن PostgreSQL**  
   ```bash
   sudo systemctl stop postgresql
   ```  
2. **انتقال `pg_wal` به محل جدید (مثلاً `/mnt/new_disk/pg_wal/`)**  
   ```bash
   mv /var/lib/postgresql/14/main/pg_wal /mnt/new_disk/pg_wal
   ```  
3. **ایجاد symbolic link**  
   ```bash
   ln -s /mnt/new_disk/pg_wal /var/lib/postgresql/14/main/pg_wal
   ```  
4. **تنظیم دسترسی‌ها**  
   ```bash
   chown -R postgres:postgres /mnt/new_disk/pg_wal
   chmod 700 /mnt/new_disk/pg_wal
   ```  
5. **راه‌اندازی مجدد PostgreSQL**  
   ```bash
   sudo systemctl start postgresql
   ```  

### **پاک‌سازی `pg_wal` و جلوگیری از اشغال فضای زیاد**  
اگر فایل‌های WAL بیش از حد جمع شوند، می‌توان با استفاده از `pg_archivecleanup` یا `pg_recyling` فضای آن را مدیریت کرد.  

**روش کاهش اندازه WAL به صورت دستی:**  
```sql
SELECT pg_switch_wal();  -- تغییر فایل WAL فعلی
SELECT pg_walfile_name(pg_current_wal_lsn());  -- مشاهده فایل جدید WAL
```  

**فعال کردن Auto Vacuum برای حذف WAL‌های قدیمی:**  
```sql
ALTER SYSTEM SET wal_keep_size = '512MB'; -- محدود کردن اندازه WAL
SELECT pg_reload_conf(); -- بارگذاری مجدد تنظیمات
```  

---

## **بازیابی داده‌ها با `pg_wal`**  
اگر پایگاه داده خراب شد، می‌توان از `pg_wal` برای بازیابی استفاده کرد:  

**بازیابی از WAL قدیمی:**  
```bash
pg_restore -d my_database -W my_wal_file
```  

**بازیابی Point-In-Time Recovery (PITR):**  
- تمام WALهای مورد نیاز را در مسیر `pg_wal` قرار دهید.  
- `recovery.conf` را پیکربندی کنید.  
- PostgreSQL را در حالت **restore** اجرا کنید.  

---

## **نتیجه‌گیری**  
- `pg_wal` قلب سیستم **بازیابی و دوام داده‌ها** در PostgreSQL است.  
- اگر پایگاه داده دچار خرابی شود، از WAL برای **بازیابی داده‌ها** استفاده می‌شود.  
- اگر `pg_wal` بیش از حد رشد کرد، می‌توان آن را **مدیریت یا به دیسک دیگری منتقل کرد.**  

# 12. `pg_ctl` در PostgreSQL   

`pg_ctl` یک ابزار مدیریتی در PostgreSQL است که برای **مدیریت فرآیند سرور پایگاه داده** استفاده می‌شود. این ابزار به شما امکان می‌دهد **PostgreSQL را راه‌اندازی، متوقف، راه‌اندازی مجدد و بررسی وضعیت** آن را کنترل کنید.  

---

## **کارکرد `pg_ctl`**  

### **۱. راه‌اندازی (Start) سرور PostgreSQL**  
برای راه‌اندازی PostgreSQL با استفاده از `pg_ctl`، از دستور زیر استفاده کنید:  

```bash
./pg_ctl start -D /var/lib/postgresql/14/main
```
یا  
```bash
./pg_ctl -D /var/lib/postgresql/14/main -l logfile start
```

🔹 **توضیحات:**  
- `-D /path/to/data_directory` مسیر دایرکتوری داده‌های PostgreSQL را مشخص می‌کند.  
- `-l logfile` یک فایل لاگ برای ثبت پیام‌های سرور ایجاد می‌کند.  

---

### **۲. متوقف کردن (Stop) سرور PostgreSQL**  
برای خاموش کردن ایمن سرور، از یکی از روش‌های زیر استفاده کنید:  

```bash
./pg_ctl stop -D /var/lib/postgresql/14/main
```

می‌توانید روش متوقف کردن را مشخص کنید:  

```bash
./pg_ctl stop -D /var/lib/postgresql/14/main -m smart
```

🔹 **روش‌های متوقف کردن (`-m` mode):**  
| حالت | توضیح |
|------|--------|
| `smart` (پیش‌فرض) | همه کلاینت‌های متصل باید اتصال خود را ببندند، سپس سرور خاموش می‌شود. |
| `fast` | تمام تراکنش‌ها لغو شده و سرور بلافاصله خاموش می‌شود. (روش توصیه‌شده) |
| `immediate` | پردازش سرور بلافاصله متوقف شده و در اجرای بعدی، بازیابی از WAL انجام می‌شود. (غیرمطمئن) |

مثلاً، اگر بخواهید PostgreSQL را **بلافاصله** خاموش کنید:  
```bash
./pg_ctl stop -D /var/lib/postgresql/14/main -m fast
```

---

### **۳. بررسی وضعیت سرور PostgreSQL**  
برای مشاهده وضعیت سرور، از این دستور استفاده کنید:  

```bash
./pg_ctl status -D /var/lib/postgresql/14/main
```

اگر PostgreSQL در حال اجرا باشد، خروجی مشابه زیر خواهید دید:  
```
./pg_ctl: server is running (PID: 12345)
```
در غیر این صورت، خروجی می‌گوید که سرور اجرا نمی‌شود.  

---

### **۴. راه‌اندازی مجدد (Restart) سرور PostgreSQL**  
برای راه‌اندازی مجدد سرور بدون نیاز به توقف دستی:  

```bash
./pg_ctl restart -D /var/lib/postgresql/14/main
```

اگر می‌خواهید سرور را سریع‌تر راه‌اندازی کنید:  

```bash
./pg_ctl restart -D /var/lib/postgresql/14/main -m fast
```

---

### **۵. بارگذاری مجدد (Reload) پیکربندی بدون ریستارت**  
اگر تغییراتی در `postgresql.conf` ایجاد کرده‌اید و می‌خواهید بدون راه‌اندازی مجدد، آنها را اعمال کنید، از دستور زیر استفاده کنید:  

```bash
./pg_ctl reload -D /var/lib/postgresql/14/main
```

---

## **مقایسه `pg_ctl` با `systemctl`**  
در توزیع‌های مدرن لینوکس، PostgreSQL معمولاً توسط `systemd` مدیریت می‌شود و می‌توان از `systemctl` نیز استفاده کرد:

| **عملیات**  | **با `pg_ctl`** | **با `systemctl`** |
|-------------|----------------|--------------------|
| راه‌اندازی  | `pg_ctl start -D /var/lib/postgresql/14/main` | `sudo systemctl start postgresql` |
| توقف        | `pg_ctl stop -D /var/lib/postgresql/14/main` | `sudo systemctl stop postgresql` |
| وضعیت      | `pg_ctl status -D /var/lib/postgresql/14/main` | `sudo systemctl status postgresql` |
| راه‌اندازی مجدد | `pg_ctl restart -D /var/lib/postgresql/14/main` | `sudo systemctl restart postgresql` |

در سیستم‌هایی که از `systemd` پشتیبانی می‌کنند، توصیه می‌شود از `systemctl` استفاده کنید، مگر اینکه PostgreSQL را به‌صورت دستی اجرا کرده باشید.

---

## **بررسی مسیر `pg_ctl` و نسخه PostgreSQL**  
برای بررسی نسخه PostgreSQL و مسیر `pg_ctl`، می‌توانید از دستورات زیر استفاده کنید:  

```bash
pg_ctl --version
```
```bash
which pg_ctl
```
یا  
```bash
find / -name "pg_ctl" 2>/dev/null
```

---

- `pg_ctl` یک ابزار مدیریتی برای **کنترل فرآیند سرور PostgreSQL** است.  
- می‌توان از آن برای **راه‌اندازی، توقف، بررسی وضعیت، راه‌اندازی مجدد و بارگذاری تنظیمات** استفاده کرد.  
- گزینه‌های **`-m smart`، `-m fast` و `-m immediate`** تعیین می‌کنند که سرور چگونه متوقف شود.  
- در سیستم‌های مدرن، بهتر است از `systemctl` برای مدیریت PostgreSQL استفاده شود.  

# 13. `pg_dump` در PostgreSQL   

`pg_dump` یک ابزار پشتیبان‌گیری (Backup) در PostgreSQL است که برای **گرفتن نسخه پشتیبان از یک پایگاه داده خاص** استفاده می‌شود. این ابزار داده‌ها و ساختار پایگاه داده را در قالب‌های مختلف استخراج می‌کند و به شما امکان می‌دهد که آنها را در یک سرور دیگر بازیابی کنید.  

---

## **۱. نحوه استفاده از `pg_dump`**  
فرمت کلی دستور:  
```bash
pg_dump -U username -d database_name -F format -f backup_file
```

🔹 **توضیح پارامترها:**  
- `-U username` → نام کاربری PostgreSQL  
- `-d database_name` → نام پایگاه داده‌ای که می‌خواهید پشتیبان بگیرید  
- `-F format` → فرمت خروجی (`c` برای فرمت فشرده، `t` برای tar، `p` برای plain text)  
- `-f backup_file` → نام فایل خروجی  

---

## **۲. مثال‌های کاربردی**  

### **۱. گرفتن بکاپ متنی (SQL Dump)**  
```bash
pg_dump -U postgres -d mydb -F p -f backup.sql
```
🔹 این دستور **کل پایگاه داده `mydb` را در قالب یک فایل متنی (`.sql`) ذخیره می‌کند** که می‌توان آن را با `psql` بازیابی کرد.

---

### **۲. گرفتن بکاپ فشرده (Custom Format)**  
```bash
pg_dump -U postgres -d mydb -F c -f backup.dump
```
🔹 این نوع بکاپ فشرده شده و فقط با `pg_restore` قابل بازیابی است.  

---

### **۳. گرفتن بکاپ در قالب `tar`**  
```bash
pg_dump -U postgres -d mydb -F t -f backup.tar
```
🔹 این فرمت را می‌توان با `pg_restore` بازیابی کرد و برای انتقال به سرورهای دیگر مناسب است.  

---

### **۴. گرفتن بکاپ فقط از ساختار (بدون داده‌ها)**  
```bash
pg_dump -U postgres -d mydb -s -f structure.sql
```
🔹 این دستور فقط **اسکیمای پایگاه داده** (ساختار جداول، ایندکس‌ها و توابع) را ذخیره می‌کند، بدون داده‌ها.  

---

### **۵. گرفتن بکاپ فقط از داده‌ها (بدون اسکیمای جداول)**  
```bash
pg_dump -U postgres -d mydb -a -f data_only.sql
```
🔹 این دستور فقط **داده‌های داخل جداول** را بدون ایجاد ساختار ذخیره می‌کند.  

---

## **۳. بازیابی اطلاعات از `pg_dump`**  
اگر بکاپ متنی (`.sql`) گرفته‌اید، برای بازیابی از `psql` استفاده کنید:  

```bash
psql -U postgres -d newdb -f backup.sql
```

اگر بکاپ در فرمت `c` یا `t` گرفته‌اید، از `pg_restore` استفاده کنید:  

```bash
pg_restore -U postgres -d newdb backup.dump
```

---

# 14. `pg_dumpall` در PostgreSQL 

`pg_dumpall` ابزاری برای گرفتن **نسخه پشتیبان از کل سرور PostgreSQL** است. این ابزار نه‌تنها تمام پایگاه داده‌ها را ذخیره می‌کند، بلکه **کاربران، رول‌ها، تنظیمات و دسترسی‌ها** را نیز شامل می‌شود.  

---

## **۱. نحوه استفاده از `pg_dumpall`**  
فرمت کلی:  
```bash
pg_dumpall -U username -f backup.sql
```
🔹 این دستور تمام پایگاه داده‌های سرور PostgreSQL را در یک فایل متنی ذخیره می‌کند.  

---

## **۲. مثال‌های کاربردی**  

### **۱. گرفتن بکاپ از کل سرور**  
```bash
pg_dumpall -U postgres -f all_databases_backup.sql
```
🔹 این دستور **از تمام پایگاه داده‌ها، کاربران و تنظیمات سرور PostgreSQL پشتیبان می‌گیرد**.  

---

### **۲. گرفتن بکاپ بدون تنظیمات سرور (فقط پایگاه داده‌ها)**  
```bash
pg_dumpall -U postgres --no-role-passwords -f databases_backup.sql
```
🔹 این دستور **رمز عبور رول‌ها را در خروجی قرار نمی‌دهد** و فقط شامل اطلاعات پایگاه داده‌ها می‌شود.  

---

## **۳. بازیابی اطلاعات از `pg_dumpall`**  
چون خروجی `pg_dumpall` یک **فایل SQL متنی** است، می‌توان آن را مستقیماً با `psql` بازیابی کرد:  

```bash
psql -U postgres -f all_databases_backup.sql
```
🔹 این دستور **همه پایگاه داده‌ها و تنظیمات را روی سرور جدید بازیابی می‌کند**.  

---

## **۴. تفاوت‌های `pg_dump` و `pg_dumpall`**  

- `pg_dump` **فقط از یک پایگاه داده مشخص پشتیبان می‌گیرد**.  
- برای گرفتن بکاپ از **تمام پایگاه داده‌های موجود در سرور**، از `pg_dumpall` استفاده کنید.  


| ویژگی | `pg_dump` | `pg_dumpall` |
|--------|----------|--------------|
| تعداد پایگاه داده | یک پایگاه داده خاص | همه پایگاه داده‌ها روی سرور |
| رول‌ها و کاربران | شامل نمی‌شود | شامل رول‌ها و کاربران |
| تنظیمات سرور | شامل نمی‌شود | شامل تنظیمات `postgresql.conf` و `pg_hba.conf` |
| نوع خروجی | SQL, tar, custom, directory | فقط SQL |

---

## **۵. چه زمانی از `pg_dump` یا `pg_dumpall` استفاده کنیم؟**  

 **از `pg_dump` استفاده کنید اگر:**  
- می‌خواهید فقط **یک پایگاه داده خاص** را پشتیبان‌گیری کنید.  
- به **فرمت‌های فشرده (custom, tar, directory)** نیاز دارید.  
- می‌خواهید از طریق `pg_restore` بازیابی کنید.  

 **از `pg_dumpall` استفاده کنید اگر:**  
- می‌خواهید **از تمام پایگاه داده‌های سرور بکاپ بگیرید**.  
- نیاز دارید که **رول‌ها، کاربران و تنظیمات سرور** نیز ذخیره شوند.  
- قصد مهاجرت به یک سرور دیگر را دارید.  

---

- `pg_dump` برای گرفتن **بکاپ از یک پایگاه داده خاص** با فرمت‌های متنوع استفاده می‌شود.  
- `pg_dumpall` برای گرفتن **بکاپ از کل سرور PostgreSQL (تمام پایگاه داده‌ها، کاربران و تنظیمات)** کاربرد دارد.  
- برای بازیابی `pg_dumpall` از `psql` و برای `pg_dump` از `psql` یا `pg_restore` استفاده می‌شود.  

# 15. Meta-commands
در PostgreSQL، متا کامندها (Meta-commands) به دستورات خاصی اشاره دارند که در محیط **psql** (کلاینت خط فرمان PostgreSQL) استفاده می‌شوند. این دستورات به کاربر اجازه می‌دهند که اطلاعات مربوط به پایگاه داده، جداول، شاخص‌ها، تنظیمات و سایر منابع را به راحتی مشاهده و مدیریت کند. متا کامندها با علامت **\** شروع می‌شوند و به شما امکانات مختلفی در مدیریت پایگاه داده می‌دهند.

در ادامه، برخی از مهم‌ترین و پرکاربردترین متا کامندهای PostgreSQL را توضیح می‌دهیم:

### 1. `\d`
   - **توضیح:** نمایش ساختار (schema) یک شیء در پایگاه داده، مانند جداول، نماها و ایندکس‌ها.
   - **کاربرد:**
     - `\d` : لیستی از تمام جداول، نماها، و ایندکس‌های موجود در پایگاه داده را نشان می‌دهد.
     - `\d table_name` : ساختار جدول خاصی را نمایش می‌دهد.
     - `\d+ table_name` : ساختار جدول همراه با جزئیات بیشتر (مثل اندازه‌ها، شاخص‌ها و ...) را نمایش می‌دهد.
   
   - **مثال‌ها:**
     ```bash
     \d
     \d users
     \d+ users
     ```

### 2. `\l`   - **توضیح:** نمایش لیست تمامی پایگاه‌های داده موجود در سیستم.
   - **کاربرد:** این دستور به شما امکان می‌دهد تا فهرستی از تمامی پایگاه‌های داده موجود در سرور PostgreSQL را مشاهده کنید.
   - **مثال:**
     ```bash
     \l
     ```

### 3. `\c`   - **توضیح:** اتصال به یک پایگاه داده دیگر.
   - **کاربرد:** با این دستور می‌توانید از پایگاه داده فعلی به یک پایگاه داده دیگر متصل شوید.
   - **مثال:**
     ```bash
     \c my_database
     ```

### 4. `\d`
   - **توضیح:** نمایش تمامی جداول موجود در پایگاه داده فعلی.
   - **کاربرد:** این دستور لیستی از تمامی جداول موجود در پایگاه داده فعلی را به نمایش می‌گذارد.
   - **مثال:**
     ```bash
     \dt
     ```

### 5. `\d`
   - **توضیح:** نمایش تمامی نماها (views).
   - **کاربرد:** این دستور فهرستی از تمامی نماها در پایگاه داده فعلی را نشان می‌دهد.
   - **مثال:**
     ```bash
     \dv
     ```

### 6. `\d`
   - **توضیح:** نمایش تمامی ایندکس‌ها.
   - **کاربرد:** با این دستور می‌توانید فهرستی از تمامی ایندکس‌های موجود در پایگاه داده فعلی را مشاهده کنید.
   - **مثال:**
     ```bash
     \di
     ```

### 7. `\d`
   - **توضیح:** نمایش تمامی توابع (functions).
   - **کاربرد:** این دستور لیستی از تمامی توابع (مانند توابع ذخیره شده) موجود در پایگاه داده را نشان می‌دهد.
   - **مثال:**
     ```bash
     \df
     ```

### 8. `\x`
   - **توضیح:** تغییر قالب نمایش نتایج به حالت گسترده (expanded).
   - **کاربرد:** این دستور نمایش نتایج را به صورت گسترده انجام می‌دهد که برای نتایج بزرگ‌تر یا پیچیده‌تر مفید است.
   - **مثال:**
     ```bash
     \x
     ```

### 9. `\!`
   - **توضیح:** اجرای دستورات سیستم از داخل psql.
   - **کاربرد:** این دستور به شما این امکان را می‌دهد که دستورات سیستم‌عامل را از داخل محیط psql اجرا کنید.
   - **مثال:**
     ```bash
     \! ls
     ```

### 10. `\q`
   - **توضیح:** خروج از محیط psql.
   - **کاربرد:** این دستور برای خروج از محیط psql استفاده می‌شود.
   - **مثال:**
     ```bash
     \q
     ```

### 11. `\i`
   - **توضیح:** اجرای یک اسکریپت SQL از یک فایل.
   - **کاربرد:** این دستور به شما این امکان را می‌دهد که یک فایل SQL را از داخل psql اجرا کنید.
   - **مثال:**
     ```bash
     \i /path/to/your/file.sql
     ```

### 12. `\h`
   - **توضیح:** نمایش مستندات مربوط به دستورات SQL.
   - **کاربرد:** این دستور به شما کمک می‌کند تا مستندات مربوط به دستورات SQL مختلف را مشاهده کنید.
   - **مثال:**
     ```bash
     \h SELECT
     ```

### 13. `\p`
   - **توضیح:** نمایش محتوای آخرین دستور SQL وارد شده.
   - **کاربرد:** این دستور آخرین دستوری که وارد کرده‌اید را نمایش می‌دهد.
   - **مثال:**
     ```bash
     \p
     ```

### 14. `\r`
   - **توضیح:** پاک کردن محتویات بافر (buffer).
   - **کاربرد:** این دستور برای پاک کردن بافر به کار می‌رود.
   - **مثال:**
     ```bash
     \r
     ```

### 15. `\set`
   - **توضیح:** تنظیم متغیرهای داخلی psql.
   - **کاربرد:** با این دستور می‌توانید متغیرهای داخلی psql را تنظیم کنید. به عنوان مثال، می‌توانید فرمت نمایش نتایج را تغییر دهید.
   - **مثال:**
     ```bash
     \set ECHO all
     ```

### 16. `\copy`
   - **توضیح:** وارد کردن یا صادر کردن داده‌ها به فایل.
   - **کاربرد:** این دستور برای وارد کردن داده‌ها از فایل به جدول یا صادر کردن داده‌ها از جدول به فایل استفاده می‌شود.
   - **مثال:**
     ```bash
     \copy my_table to '/path/to/file.csv' with (format csv);
     ```

### 17. `\timing`
   - **توضیح:** فعال یا غیرفعال کردن نمایش زمان اجرای دستورات.
   - **کاربرد:** این دستور به شما این امکان را می‌دهد که زمان اجرای دستورات SQL را مشاهده کنید.
   - **مثال:**
     ```bash
     \timing
     ```

### 18. `\conninfo`
   - **توضیح:** نمایش اطلاعات اتصال به پایگاه داده.
   - **کاربرد:** این دستور اطلاعات مربوط به اتصال فعلی شما به پایگاه داده را نشان می‌دهد.
   - **مثال:**
     ```bash
     \conninfo
     ```
# 16. Show commands
### دستور `SHOW` در PostgreSQL  

دستور `SHOW` در PostgreSQL برای نمایش مقدار فعلی پارامترهای زمان اجرا استفاده می‌شود. این پارامترها می‌توانند از طریق دستور `SET`، ویرایش فایل پیکربندی `postgresql.conf`، متغیر محیطی `PGOPTIONS` یا فلگ‌های خط فرمان هنگام راه‌اندازی سرور تنظیم شوند.  

---

### **نحوه استفاده از `SHOW`**  

- **نمایش مقدار یک پارامتر خاص:**  
  ```sql
  SHOW name;
  ```
  مثال برای مشاهده مقدار فعلی پارامتر `DateStyle`:
  ```sql
  SHOW DateStyle;
  ```

- **نمایش تمام پارامترهای پیکربندی:**  
  ```sql
  SHOW ALL;
  ```

---

### **پارامترهای کلیدی که با `SHOW` قابل نمایش هستند**  

| **پارامتر**          | **توضیح** |
|---------------------|----------|
| `SERVER_VERSION`   | نمایش نسخه سرور PostgreSQL |
| `SERVER_ENCODING`  | نمایش کدگذاری کاراکترهای سمت سرور |
| `LC_COLLATE`       | نمایش تنظیمات محلی دیتابیس برای ترتیب‌دهی متون |
| `LC_CTYPE`         | نمایش تنظیمات محلی دیتابیس برای طبقه‌بندی کاراکترها |
| `IS_SUPERUSER`     | نمایش وضعیت سوپریوزر برای نقش جاری |
| `TimeZone`         | نمایش منطقه زمانی سرور |
| `default_transaction_isolation` | نمایش سطح ایزوله‌سازی پیش‌فرض تراکنش‌ها |
| `max_connections`  | نمایش حداکثر تعداد اتصالات مجاز به دیتابیس |
| `shared_buffers`   | نمایش میزان حافظه اختصاص داده‌شده به کش دیتابیس |
| `effective_cache_size` | نمایش مقدار تخمینی کش مؤثر برای بهینه‌سازی اجرا |
| `port` | دیدن پورت های باز متصل|

---

### **مثال‌ها**  

- مشاهده مقدار فعلی پارامتر `geqo`:
  ```sql
  SHOW geqo;
  ```

- مشاهده منطقه زمانی سرور:
  ```sql
  SHOW TimeZone;
  ```

- نمایش تعداد اتصالات مجاز:
  ```sql
  SHOW max_connections;
  ```

- نمایش تمام تنظیمات:
  ```sql
  SHOW ALL;
  ```

---

همچنین، می‌توان از تابع `current_setting` برای دریافت مقدار پارامترها استفاده کرد:
```sql
SELECT current_setting('TimeZone');
```
# 17. Data Types 
## **انواع داده (Data Types) در PostgreSQL**  


### **📍 الف) انواع داده‌ی عددی (Numeric Types)**  

| **نوع داده**  | **حجم ذخیره‌سازی** | **دامنه‌ی مقدار** | **مثال مقدار** |
|--------------|------------------|----------------|----------------|
| `SMALLINT`   | ۲ بایت           | `-32,768` تا `32,767` | `100` |
| `INTEGER`    | ۴ بایت           | `-2,147,483,648` تا `2,147,483,647` | `5000` |
| `BIGINT`     | ۸ بایت           | `-9E+18` تا `9E+18` | `10000000000` |
| `REAL`       | ۴ بایت           | مقدار اعشاری با دقت ۶ رقم اعشار | `3.14159` |
| `DOUBLE PRECISION` | ۸ بایت  | مقدار اعشاری با دقت ۱۵ رقم اعشار | `3.14159265358979` |
| `NUMERIC(p, s)` | متغیر | مقدار اعشاری دقیق | `12345.6789` |

✅ **نکته:**  
- `NUMERIC(10, 2)` یعنی **۱۰ رقم که ۲ رقم آن اعشار است**.  
- برای ذخیره‌ی دقیق **ارز و پول** بهتر است از `NUMERIC` به‌جای `REAL` استفاده کنید.  

---

### **📍 ب) انواع داده‌ی متنی (Character Types)**  

| **نوع داده**  | **حجم ذخیره‌سازی** | **توضیح** |
|--------------|------------------|-----------|
| `TEXT`       | متغیر            | طول نامحدود |
| `VARCHAR(n)` | متغیر            | حداکثر `n` کاراکتر |
| `CHAR(n)`    | ثابت             | همیشه `n` کاراکتر ذخیره می‌شود |

✅ **نکته:**  
- `TEXT` مناسب‌ترین گزینه برای ذخیره‌ی رشته‌های متنی نامحدود است.  
- `VARCHAR(n)` فقط در صورتی که محدودیت خاصی برای طول مقدار دارید استفاده شود.  

🔹 **مثال:**
```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    bio TEXT
);
```

---

### **📍 ج) انواع داده‌ی زمانی (Date & Time Types)**  

| **نوع داده**    | **فرمت نمونه مقدار**      | **توضیح** |
|---------------|--------------------|-----------|
| `DATE`       | `2025-02-07`       | فقط تاریخ |
| `TIME`       | `14:30:00`         | فقط زمان |
| `TIMESTAMP`  | `2025-02-07 14:30:00` | تاریخ و زمان |
| `INTERVAL`   | `2 days 10 hours`  | فاصله‌ی زمانی |

🔹 **مثال:**
```sql
CREATE TABLE events (
    id SERIAL PRIMARY KEY,
    event_name TEXT,
    event_date TIMESTAMP
);
```
```sql
INSERT INTO events (event_name, event_date) VALUES 
    ('Conference', '2025-03-15 10:00:00'),
    ('Workshop', '2025-04-20 15:30:00');
```

---

### **📍 د) انواع داده‌ی Boolean**  

| **نوع داده** | **مقدار مجاز** |
|-------------|--------------|
| `BOOLEAN`   | `TRUE`, `FALSE` |

🔹 **مثال:**
```sql
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    description TEXT,
    is_completed BOOLEAN
);
```
```sql
INSERT INTO tasks (description, is_completed) VALUES 
    ('Write report', TRUE),
    ('Fix bug', FALSE);
```

---

### **📍 ه) انواع داده‌ی JSON و JSONB**  
PostgreSQL از `JSON` و `JSONB` پشتیبانی می‌کند که برای **ذخیره و پردازش داده‌های ساختاریافته‌ی JSON** استفاده می‌شوند.

| **نوع داده** | **توضیح** |
|-------------|-----------|
| `JSON`      | ذخیره‌ی متن JSON (غیرقابل ایندکس شدن و کندتر) |
| `JSONB`     | ذخیره‌ی باینری JSON (ایندکس‌پذیر و سریع‌تر) |

🔹 **مثال:**
```sql
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    details JSONB
);
```
```sql
INSERT INTO products (details) VALUES 
    ('{"name": "Laptop", "price": 2499.99, "brand": "Dell"}');
```
```sql
SELECT details->>'name' AS product_name FROM products;
```

---
## **نوع داده‌ی `OID` در PostgreSQL**  
🔹 `OID` مخفف **Object Identifier** است و یک نوع داده‌ی **۴ بایتی عدد صحیح بدون علامت (Unsigned Integer)** محسوب می‌شود که در PostgreSQL برای **شناسه‌گذاری اشیاء داخلی دیتابیس** به کار می‌رود.  

### **📌 ویژگی‌های `OID`:**
- به‌عنوان **شناسه‌ی یکتا (Unique Identifier)** برای اشیاء پایگاه داده (مانند جداول، ایندکس‌ها، توابع و ...) استفاده می‌شود.  
- هر **شیء سیستمی در PostgreSQL** یک مقدار `OID` دارد.  
- مقدار `OID` به‌طور خودکار هنگام ایجاد اشیاء توسط PostgreSQL اختصاص داده می‌شود.  

### **📌 مشاهده `OID` اشیاء در دیتابیس**
#### ۱️⃣ نمایش `OID` تمام جداول دیتابیس:  
```sql
SELECT oid, relname FROM pg_class WHERE relkind = 'r';
```
#### ۲️⃣ نمایش `OID` یک جدول خاص:  
```sql
SELECT oid FROM pg_class WHERE relname = 'users';
```
(در اینجا `users` نام جدول مورد نظر است.)  

---

## **نوع داده‌ی `REAL` در PostgreSQL**  
🔹 `REAL` یک نوع داده‌ی عددی **ممیز شناور (Floating Point)** با دقت ۴ بایتی است که برای ذخیره‌سازی اعداد اعشاری با دقت تقریبی استفاده می‌شود.  

### **📌 ویژگی‌های `REAL`:**
- دقت ذخیره‌سازی تا **۶ رقم اعشار**  
- مناسب برای محاسباتی که به دقت بالا نیاز ندارند  
- امکان ذخیره‌ی مقادیر بسیار کوچک و بسیار بزرگ  
- امکان **عدم دقت (Precision Loss)** به دلیل ساختار ذخیره‌سازی ممیز شناور  

### **📌 مثال استفاده از `REAL`:**  
```sql
CREATE TABLE prices (
    id SERIAL PRIMARY KEY,
    product_name TEXT,
    price REAL
);
```
```sql
INSERT INTO prices (product_name, price) VALUES 
    ('Laptop', 2499.99),
    ('Phone', 899.95),
    ('Tablet', 499.49);
```
```sql
SELECT * FROM prices;
```

✅ **نکته:** اگر به دقت بیشتری نیاز دارید، از `NUMERIC` یا `DECIMAL` استفاده کنید.

---
---

💡 **سوالی در مورد انواع داده‌ها دارید؟** 😃
# 18. pg_class
### **جدول `pg_class` در PostgreSQL**  
جدول `pg_class` اطلاعات متادیتا درباره‌ی تمام جداول، ایندکس‌ها، ویوها و سایر اشیاء دیتابیسی را ذخیره می‌کند. این جدول در ترکیب با سایر جداول سیستمی مانند `pg_namespace` (برای فضای نام) و `pg_attribute` (برای ستون‌های جداول) می‌تواند برای بررسی ساختار دیتابیس و بهینه‌سازی عملکرد آن بسیار مفید باشد.
جدول **`pg_class`** یکی از کاتالوگ‌های سیستمی (System Catalog) در PostgreSQL است که اطلاعات مربوط به جداول، ایندکس‌ها، ویوها و سایر اشیاء ذخیره‌شده در دیتابیس را نگه می‌دارد. این جدول اطلاعات متادیتا (metadata) را در مورد هر شیء در دیتابیس ذخیره می‌کند.  

---

### **محتوای `pg_class`**
هر ردیف در این جدول مربوط به یک **relation** (جدول، ایندکس، ویو، sequence و ...) است. برخی از ستون‌های مهم `pg_class` عبارت‌اند از:

| **ستون**         | **نوع داده** | **توضیح** |
|----------------|------------|-----------|
| `oid`         | `oid`      | شناسه یکتای هر relation در دیتابیس |
| `relname`     | `name`     | نام جدول، ایندکس یا ویو |
| `relnamespace`| `oid`      | شناسه `pg_namespace` که فضای نام (Schema) مربوطه را مشخص می‌کند |
| `reltype`     | `oid`      | شناسه نوع (data type) مرتبط با این relation |
| `relowner`    | `oid`      | شناسه کاربری که مالک این relation است |
| `relkind`     | `char`     | نوع شیء ذخیره‌شده (جدول، ایندکس، ویو و ...) |
| `reltuples`   | `real`     | تعداد تقریبی ردیف‌های موجود در relation (با تحلیل `ANALYZE` به‌روز می‌شود) |
| `relpages`    | `integer`  | تعداد تقریبی صفحات ذخیره‌سازی برای این relation |
| `relhasindex` | `boolean`  | آیا این relation ایندکس دارد؟ (True/False) |

---

### **مقدار `relkind` و معنای آن**
ستون `relkind` نوع relation را مشخص می‌کند. مقادیر مهم این ستون عبارت‌اند از:

| **مقدار `relkind`** | **نوع relation** |
|-----------------|-----------------|
| `r`            | جدول معمولی (Table) |
| `i`            | ایندکس (Index) |
| `S`            | شمارنده (`Sequence`) |
| `v`            | ویو (View) |
| `m`            | materialized view |
| `c`            | جدول ترکیبی (Composite Type) |
| `t`            | جدول موقت (TOAST Table) |
| `f`            | foreign table |

---

### **چند مثال کاربردی**
#### 1. نمایش تمام جداول موجود در دیتابیس  
```sql
SELECT relname FROM pg_class WHERE relkind = 'r';
```

#### 2. نمایش تعداد تقریبی رکوردهای جداول  
```sql
SELECT relname, reltuples::bigint AS estimated_rows FROM pg_class WHERE relkind = 'r' ORDER BY reltuples DESC;
```

#### 3. نمایش ایندکس‌های موجود در دیتابیس  
```sql
SELECT relname FROM pg_class WHERE relkind = 'i';
```

#### 4. نمایش اطلاعات یک جدول خاص  
```sql
SELECT * FROM pg_class WHERE relname = 'users';
```
(در اینجا `users` نام جدول موردنظر است.)

---

# 19.Schema


### **1. تعریف Schema**  
در PostgreSQL، **Schema** یک فضای نام (Namespace) برای سازمان‌دهی اشیاء دیتابیسی مانند **جداول، ایندکس‌ها، ویوها، فانکشن‌ها، sequenceها و سایر موجودیت‌های پایگاه داده** است.  
به زبان ساده، **Schema مانند یک پوشه در یک سیستم فایل عمل می‌کند** که می‌توان داخل آن جداول و سایر اشیاء مرتبط را ذخیره کرد.  

### **2. دلایل استفاده از Schema**  

#### ✅ **مدیریت بهتر داده‌ها**  
- استفاده از Schema به دسته‌بندی بهتر جداول و اشیاء کمک می‌کند، مخصوصاً زمانی که یک پایگاه داده بزرگ با تعداد زیادی جدول داشته باشیم.  

#### ✅ **افزایش امنیت و کنترل دسترسی**  
- امکان **تعیین سطح دسترسی کاربران** برای هر Schema جداگانه وجود دارد.  
- برای مثال، می‌توان برخی کاربران را به **یک Schema خاص محدود کرد** و اجازه دسترسی به سایر Schemaها را نداد.  

#### ✅ **امکان تفکیک داده‌های مرتبط به پروژه‌ها یا ماژول‌ها**  
- در یک سیستم که چندین ماژول دارد، می‌توان هر ماژول را در یک Schema مجزا نگه داشت.  

#### ✅ **پشتیبانی از چندین نسخه از یک جدول**  
- با استفاده از Schema می‌توان **نسخه‌های مختلف یک جدول** را در یک پایگاه داده ذخیره کرد، مثلاً:  
  - `schema1.customers`
  - `schema2.customers`  

#### ✅ **امکان اجرای تست بدون تغییر داده‌های اصلی**  
- می‌توان یک Schema مخصوص تست ایجاد کرد و **کدها را روی داده‌های تستی اجرا کرد** بدون آنکه داده‌های اصلی تغییری کنند.  

---

### **3. نحوه استفاده از Schema در PostgreSQL**  

#### **📌 نمایش تمام Schemaهای موجود در دیتابیس**
```sql
SELECT nspname FROM pg_catalog.pg_namespace;
```

#### **📌 ایجاد یک Schema جدید**
```sql
CREATE SCHEMA my_schema;
```
- این دستور یک **Schema جدید** با نام `my_schema` ایجاد می‌کند.  

#### **📌 حذف یک Schema**  
```sql
DROP SCHEMA my_schema CASCADE;
```
- اگر `CASCADE` استفاده شود، تمام جداول و اشیاء داخل Schema نیز حذف خواهند شد.  

#### **📌 ایجاد جدول در یک Schema خاص**  
```sql
CREATE TABLE my_schema.users (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT UNIQUE
);
```
- این جدول درون `my_schema` ایجاد خواهد شد.  

#### **📌 استفاده از Schema خاص هنگام کوئری زدن**  
```sql
SELECT * FROM my_schema.users;
```
- به دلیل وجود چندین Schema در پایگاه داده، همیشه باید قبل از نام جدول، نام Schema را مشخص کرد.  

#### **📌 تغییر Schema پیش‌فرض برای یک نشست (Session)**
```sql
SET search_path TO my_schema;
```
- بعد از اجرای این دستور، نیازی به نوشتن `my_schema.` در کوئری‌ها نیست.  
- مثلاً پس از `SET search_path` می‌توان مستقیماً نوشت:
  ```sql
  SELECT * FROM users;
  ```
  
#### **📌 تغییر مالکیت یک Schema**  
```sql
ALTER SCHEMA my_schema OWNER TO new_user;
```
- این دستور مالکیت Schema را به کاربر `new_user` تغییر می‌دهد.  

#### **📌 دادن دسترسی به یک Schema به کاربران دیگر**  
```sql
GRANT USAGE ON SCHEMA my_schema TO some_user;
```
- با این دستور، کاربر `some_user` می‌تواند از اشیاء داخل `my_schema` استفاده کند.  

---

### **4. موضوعات کلیدی مرتبط با Schema در PostgreSQL**  

#### **📍 Schema پیش‌فرض (`public`)**  
- در PostgreSQL، **به‌صورت پیش‌فرض تمام جداول و اشیاء در Schema‌ای به نام `public` ایجاد می‌شوند.**  
- یعنی اگر شما بدون مشخص کردن نام Schema، یک جدول ایجاد کنید:
  ```sql
  CREATE TABLE users (
      id SERIAL PRIMARY KEY,
      name TEXT
  );
  ```
  این جدول در **Schema پیش‌فرض (`public`)** ذخیره می‌شود و معادل این است:
  ```sql
  CREATE TABLE public.users (
      id SERIAL PRIMARY KEY,
      name TEXT
  );
  ```

- اگر نمی‌خواهید که کاربران عادی به این Schema پیش‌فرض دسترسی داشته باشند، می‌توانید دسترسی آن را حذف کنید:
  ```sql
  REVOKE CREATE ON SCHEMA public FROM PUBLIC;
  ```

#### **📍 تغییر Schema پیش‌فرض برای یک کاربر**  
اگر بخواهید کاربری هنگام ورود به دیتابیس یک Schema خاص را به‌عنوان پیش‌فرض داشته باشد، از این دستور استفاده کنید:
```sql
ALTER ROLE some_user SET search_path TO my_schema;
```
---

### **5. مقایسه Schema با Database در PostgreSQL**  

گاهی اوقات این سؤال پیش می‌آید که **بهتر است از چند دیتابیس استفاده کنیم یا از چند Schema در یک دیتابیس؟**  

✅ **استفاده از چند دیتابیس مناسب است اگر:**  
- نیاز به **مدیریت کاملاً جداگانه** برای داده‌ها داشته باشیم.  
- هر دیتابیس تنظیمات خاص خودش را داشته باشد.  
- کاربران و سطوح دسترسی برای هر دیتابیس کاملاً جداگانه تعریف شوند.  

✅ **استفاده از چند Schema در یک دیتابیس مناسب است اگر:**  
- می‌خواهیم همه داده‌ها در یک پایگاه داده مدیریت شوند، اما در عین حال **سازمان‌یافته و دسته‌بندی شده باشند**.  
- نیاز به استفاده از **Join بین جداول مختلف در Schemaهای مختلف** داریم.  
- نیاز به یک دیتابیس واحد اما با تفکیک بخش‌های مختلف (مثلاً مالی، فروش، کاربران) داریم.  

---
# 20. template0 & template1
در پستگرس، دیتابیس‌های `template1` و `template0` به عنوان دو دیتابیس پیش‌فرض وجود دارند که نقش خاصی در ساختار و عملکرد سیستم دارند. این دیتابیس‌ها معمولاً برای مدیریت الگوهای پیش‌فرض و تنظیمات اولیه استفاده می‌شوند. در ادامه، به توضیح جزئیات هر یک از آنها می‌پردازم:

---

### **1. دیتابیس `template1`:**
#### **کاربرد:**
- `template1` به عنوان دیتابیس پیش‌فرض برای ساخت دیتابیس‌های جدید در نظر گرفته شده است.
- هر باری که با دستور `CREATE DATABASE` یک دیتابیس جدید ایجاد می‌کنید، پستگرس از این دیتابیس به عنوان الگو (template) استفاده می‌کند.
  
#### **وظایف:**
- ذخیره سازی تمام تنظیمات پیش‌فرض و ساختارهای اولیه که باید در دیتابیس‌های جدید وجود داشته باشد.
- شامل تعریف‌های پایه‌ای مثل رول‌ها (roles)، دسترسی‌ها، و ساختارهای داخلی پستگرس است.

#### **ویژگی‌ها:**
- این دیتابیس حالت "read-write" است، اما توصیه می‌شود تغییرات زیادی در آن اعمال نشود، زیرا هر تغییر در آن به دیتابیس‌های جدیدی که از آن ساخته می‌شوند منتقل می‌شود.
- اگر نیاز به تغییرات خاص در دیتابیس‌های جدید دارید، می‌توانید از دیتابیس‌های الگوی دیگر (مانند `template0`) استفاده کنید.

#### **چه دردی می‌خورد؟**
- این دیتابیس به کاربران اجازه می‌دهد بدون نیاز به تنظیم مجدد ساختار و تنظیمات، دیتابیس‌های جدیدی با تنظیمات پیش‌فرض ایجاد کنند.
- با استفاده از `template1`، مطمئن می‌شویم که تمام دیتابیس‌های جدید به طور یکسان و با استانداردهای مشخص ایجاد شوند.

---

### **2. دیتابیس `template0`:**
#### **کاربرد:**
- `template0` یک دیتابیس پاک و خالی است که شامل تنظیمات پیش‌فرض پستگرس است، بدون هیچ تغییر یا اضافه‌کاری.
- این دیتابیس معمولاً برای ایجاد دیتابیس‌هایی که نباید تحت تأثیر تغییرات قبلی در `template1` قرار بگیرند استفاده می‌شود.

#### **وظایف:**
- فراهم کردن یک نقطه شروع خالص برای دیتابیس‌های جدید.
- اطمینان از اینکه دیتابیس‌های جدید فقط از تنظیمات پایه پستگرس استفاده کنند و تغییراتی که در `template1` اعمال شده است، روی آنها تأثیر نگذارد.

#### **ویژگی‌ها:**
- این دیتابیس به حالت "read-only" تنظیم شده است، بنابراین نمی‌توانید به صورت مستقیم تغییراتی در آن اعمال کنید.
- برای استفاده از این دیتابیس به عنوان الگو، باید در دستور `CREATE DATABASE` صریحاً از آن استفاده کنید. مثال:
  ```sql
  CREATE DATABASE mydb TEMPLATE template0;
  ```

#### **چه دردی می‌خورد؟**
- این دیتابیس برای مواقعی که نیاز به یک دیتابیس خالص و بدون هیچ تنظیم یا تغییر قبلی دارید، بسیار مفید است.
- با استفاده از `template0`، می‌توانید مطمئن شوید که دیتابیس جدید شما از هرگونه تغییرات نامطلوب در `template1` محافظت شده است.

---

### **تفاوت بین `template1` و `template0`:**
| ویژگی               | `template1`                          | `template0`                          |
|----------------------|---------------------------------------|---------------------------------------|
| **وضعیت**           | Read-write                           | Read-only                            |
| **استفاده پیش‌فرض** | الگوی پیش‌فرض برای ایجاد دیتابیس‌ها   | الگوی خالص و بدون تغییرات            |
| **تغییرپذیری**       | می‌تواند تغییر کند                  | ثابت و بدون تغییر                   |
| **دستور ایجاد**       | `CREATE DATABASE db_name;`          | `CREATE DATABASE db_name TEMPLATE template0;` |

---
# 21.Role


### **1. Role (نقش):**
#### **تعریف:**
- یک **Role** در پستگرس یک موجودیت منطقی است که برای مدیریت دسترسی‌ها و اعطای اختیارات (permissions) به کاربران طراحی شده است.
- Role می‌تواند شامل یک یا چند کاربر باشد و معمولاً برای سازماندهی دسترسی‌ها استفاده می‌شود.

#### **کاربرد:**
- ایجاد گروه‌های کاربری برای مدیریت دسترسی‌ها.
- تخصیص اختیارات به گروه‌ها یا کاربران.
- کنترل دسترسی به دیتابیس‌ها، جداول، توابع و سایر اشیاء پایگاه داده.

#### **دستورات مهم:**
1. **ایجاد Role:**
   ```sql
   CREATE ROLE role_name [WITH OPTIONS];
   ```
   - مثال:
     ```sql
     CREATE ROLE developer;
     ```

2. **تنظیم اختیارات برای Role:**
   - اجازه ورود به سیستم:
     ```sql
     ALTER ROLE role_name WITH LOGIN;
     ```
   - تنظیم رمز عبور:
     ```sql
     ALTER ROLE role_name WITH PASSWORD 'password';
     ```
   - تنظیم دسترسی ادمین:
     ```sql
     ALTER ROLE role_name WITH SUPERUSER;
     ```

3. **حذف Role:**
   ```sql
   DROP ROLE role_name;
   ```

4. **نمایش Roles موجود:**
   ```sql
   \du
   ```

#### **سناریوی استفاده:**
- ایجاد یک Role برای تیم توسعه‌دهندگان (`developer`) که فقط به دیتابیس‌های خاص دسترسی داشته باشند.
- ایجاد یک Role برای مدیران سیستم (`admin`) که تمام دسترسی‌ها را داشته باشند.

---

# 22. User 

#### **تعریف:**
- یک **User** در پستگرس یک نوع خاص از Role است که دارای اختیار `LOGIN` است.
- به عبارت دیگر، کاربر یک Role است که می‌تواند به سیستم وارد شود.

#### **کاربرد:**
- ایجاد کاربران فردی برای دسترسی به پایگاه داده.
- کنترل دسترسی‌ها برای هر کاربر.

#### **دستورات مهم:**
1. **ایجاد کاربر:**
   ```sql
   CREATE USER user_name [WITH OPTIONS];
   ```
   - مثال:
     ```sql
     CREATE USER john WITH PASSWORD 'securepassword';
     ```

2. **حذف کاربر:**
   ```sql
   DROP USER user_name;
   ```

3. **تنظیم رمز عبور کاربر:**
   ```sql
   ALTER USER user_name WITH PASSWORD 'newpassword';
   ```

4. **نمایش کاربران موجود:**
   ```sql
   SELECT * FROM pg_roles WHERE rolcanlogin = true;
   ```

#### **تمایز بین Role و User:**
- هر **User** یک **Role** است، اما هر **Role** لزوماً کاربر نیست.
- یک Role بدون اختیار `LOGIN` نمی‌تواند به سیستم وارد شود.

---

# 23. Owner (صاحب):
#### **تعریف:**
- **Owner** یا صاحب یک شیء (object) در پستگرس، شخص یا Role است که این شیء را ایجاد کرده است.
- صاحب یک شیء دارای تمام اختیارات بر روی آن است.

#### **کاربرد:**
- کنترل دسترسی به اشیاء پایگاه داده (مثل جداول، توابع و دیتابیس‌ها).
- مدیریت مالکیت اشیاء.

#### **دستورات مهم:**
1. **تغییر مالکیت شیء:**
   ```sql
   ALTER TABLE table_name OWNER TO new_owner;
   ```
   - مثال:
     ```sql
     ALTER TABLE employees OWNER TO admin;
     ```

2. **نمایش مالک شیء:**
   ```sql
   SELECT tableowner FROM pg_tables WHERE tablename = 'table_name';
   ```

#### **سناریوی استفاده:**
- انتقال مالکیت یک جدول از یک کاربر به Role مدیریتی.
- تخصیص مالکیت یک دیتابیس به یک Role خاص.

---

# 24. Permissions 

#### **تعریف:**
- **Permissions** یا دسترسی‌ها، مجموعه‌ای از حقوق است که به یک Role یا کاربر اختصاص داده می‌شود.
- این دسترسی‌ها شامل `SELECT`, `INSERT`, `UPDATE`, `DELETE`, و غیره است.

#### **دستورات مهم:**
1. **اعطای دسترسی:**
   ```sql
   GRANT permission ON object_name TO role_name;
   ```
   - مثال:
     ```sql
     GRANT SELECT, INSERT ON employees TO developer;
     ```

2. **حذف دسترسی:**
   ```sql
   REVOKE permission ON object_name FROM role_name;
   ```
   - مثال:
     ```sql
     REVOKE DELETE ON employees FROM developer;
     ```

3. **نمایش دسترسی‌ها:**
   ```sql
   \z object_name
   ```

#### **سناریوی استفاده:**
- اعطای دسترسی خواندنی (`SELECT`) به یک Role برای مشاهده جداول حساس.
- حذف دسترسی حذف (`DELETE`) از یک Role برای جلوگیری از اصلاحات غیرمجاز.

---

### 25. Group Role
#### **تعریف:**
- یک **Group Role** یک Role است که می‌تواند دیگر Roles یا Users را شامل شود.
- این گروه‌ها برای سازماندهی دسترسی‌ها و مدیریت کاربران استفاده می‌شوند.

#### **دستورات مهم:**
1. **ایجاد گروه:**
   ```sql
   CREATE ROLE group_name;
   ```

2. **افزودن کاربر به گروه:**
   ```sql
   GRANT group_name TO user_name;
   ```
   - مثال:
     ```sql
     GRANT developers TO john;
     ```

3. **حذف کاربر از گروه:**
   ```sql
   REVOKE group_name FROM user_name;
   ```

#### **سناریوی استفاده:**
- ایجاد یک گروه برای تیم توسعه‌دهندگان و اعطای دسترسی‌های مشترک به اعضای این گروه.

---

# 26. Superuser
#### **تعریف:**
- یک **Superuser** یک Role است که تمام اختیارات و دسترسی‌ها را دارد.
- این نقش معمولاً برای مدیران سیستم استفاده می‌شود.

#### **دستورات مهم:**
1. **ایجاد Superuser:**
   ```sql
   CREATE ROLE superuser_name WITH SUPERUSER;
   ```

2. **تغییر Role به Superuser:**
   ```sql
   ALTER ROLE role_name WITH SUPERUSER;
   ```

#### **نکته:**
- استفاده از Superuser باید با احتیاط انجام شود زیرا این نقش می‌تواند تمام اجزای سیستم را تحت کنترل قرار دهد.

---

### **7. تمایز بین مفاهیم:**


در پستگرس، مفاهیمی مثل **Role**, **Permissions**,**Superuser**, **Group Role**,**User**, و **Owner** نقش مهمی در مدیریت دسترسی‌ها، امنیت‌ها و کنترل استفاده از منابع پایگاه داده دارند. 

---
| مفهوم          | تعریف                                    | کاربرد                                  |
|-----------------|------------------------------------------|-----------------------------------------|
| **Role**        | موجودیت منطقی برای مدیریت دسترسی‌ها    | ایجاد گروه‌ها و تخصیص اختیارات         |
| **User**        | Role با اختیار `LOGIN`                  | ورود به سیستم                          |
| **Owner**       | صاحب یک شیء                            | مدیریت مالکیت اشیاء                    |
| **Permissions** | دسترسی‌ها به اشیاء                     | کنترل دسترسی‌ها                        |
| **Group Role**  | Role شامل دیگر Roles یا Users           | سازماندهی دسترسی‌ها                    |
| **Superuser**   | Role با تمام اختیارات                  | مدیریت کامل سیستم                     |

---

### **8. نحوه دسترسی به این مفاهیم:**
- **Role/User:** از طریق دستورات `CREATE ROLE`, `CREATE USER`, و `ALTER ROLE`.
- **Owner:** از طریق دستور `ALTER` برای تغییر مالکیت.
- **Permissions:** از طریق دستورات `GRANT` و `REVOKE`.
- **Group Role:** از طریق دستورات `GRANT` و `REVOKE` برای مدیریت اعضای گروه.

---

### **9. نکات کلیدی برای یادگیری:**
1. **سازماندهی دسترسی‌ها:** استفاده از Roles و Group Roles برای سازماندهی دسترسی‌ها.
2. **حداقل دسترسی:** تنظیم دسترسی‌ها به حداقل مورد نیاز برای هر Role.
3. **استفاده از Superuser با احتیاط:** تنها در مواقع ضروری از Superuser استفاده کنید.
4. **مدیریت رمز عبور:** اطمینان حاصل کنید که رمز عبورهای قوی و امن تعیین شده‌اند.
5. **آشنایی با دستورات:** دستورات `GRANT`, `REVOKE`, و `\du` را به خوبی یاد بگیرید.
---

# 27.Grant

### **مفهوم `GRANT` در پستگرس**

دستور `GRANT` در پستگرس برای اعطای اختیارات (permissions) به کاربران یا Roles استفاده می‌شود. با استفاده از این دستور، می‌توانید کنترل دقیقی بر روی دسترسی‌ها به اشیاء مختلف پایگاه داده (مثل جداول، دیتابیس‌ها، توابع و غیره) داشته باشید.

---

### **چه چیزی می‌توان با `GRANT` انجام داد؟**
- اعطای دسترسی‌های خواندنی (`SELECT`).
- اعطای دسترسی‌های نوشتنی (`INSERT`, `UPDATE`, `DELETE`).
- اعطای دسترسی به اجرای توابع (`EXECUTE`) یا استفاده از ساختارهای دیگر.
- اعطای دسترسی به سطح دیتابیس یا سطح جدول.
- اعطای دسترسی به کاربران یا Groups (Roles).

---

### **ساختار عمومی دستور `GRANT`:**
```sql
GRANT permission_type ON object_name TO role_name [WITH GRANT OPTION];
```

#### **جزئیات:**
1. **`permission_type`:** نوع دسترسی که می‌خواهید بدهید (مثلاً `SELECT`, `INSERT`, `UPDATE`, `DELETE`, `EXECUTE`, و غیره).
2. **`object_name`:** اسم شیءی که می‌خواهید دسترسی به آن داده شود (مثلاً یک جدول، دیتابیس، تابع، و غیره).
3. **`role_name`:** اسم Role یا Userی که می‌خواهید دسترسی به آنها داده شود.
4. **`WITH GRANT OPTION`:** این گزینه به Role اجازه می‌دهد که دسترسی را به دیگران منتقل کند.

---

### **مثال‌های دستور `GRANT`:**

#### **1. اعطای دسترسی خواندنی به یک جدول:**
```sql
GRANT SELECT ON table_name TO user_name;
```
- این دستور به کاربر `user_name` اجازه می‌دهد تا از جدول `table_name` داده‌ها را خوانده و استفاده کند.

#### **2. اعطای دسترسی نوشتنی به یک جدول:**
```sql
GRANT INSERT, UPDATE, DELETE ON table_name TO user_name;
```
- این دستور به کاربر اجازه می‌دهد تا داده‌های جدید به جدول اضافه کند (`INSERT`), داده‌های موجود را تغییر دهد (`UPDATE`), یا داده‌های جدول را حذف کند (`DELETE`).

#### **3. اعطای دسترسی به یک دیتابیس:**
```sql
GRANT ALL PRIVILEGES ON DATABASE database_name TO user_name;
```
- این دستور به کاربر تمام دسترسی‌ها (مثل ایجاد جدول، حذف جدول، و غیره) را در دیتابیس `database_name` می‌دهد.

#### **4. اعطای دسترسی به یک تابع:**
```sql
GRANT EXECUTE ON FUNCTION function_name TO user_name;
```
- این دستور به کاربر اجازه می‌دهد تا تابع `function_name` را اجرا کند.

#### **5. اعطای دسترسی به یک Group Role:**
```sql
GRANT SELECT ON table_name TO group_role_name;
```
- این دستور به همه اعضای گروه `group_role_name` دسترسی خواندنی به جدول `table_name` می‌دهد.

#### **6. اعطای دسترسی با `WITH GRANT OPTION`:**
```sql
GRANT SELECT ON table_name TO user_name WITH GRANT OPTION;
```
- این دستور به کاربر اجازه می‌دهد تا دسترسی خواندنی جدول را به دیگران منتقل کند.

---

### **دسترسی‌های ممکن در پستگرس:**

| دسترسی        | توضیحات                                                                 |
|----------------|-------------------------------------------------------------------------|
| `SELECT`       | دسترسی خواندنی به داده‌ها (مثلاً جداول).                               |
| `INSERT`       | دسترسی به افزودن داده‌های جدید.                                         |
| `UPDATE`       | دسترسی به تغییر داده‌های موجود.                                        |
| `DELETE`       | دسترسی به حذف داده‌ها.                                                 |
| `EXECUTE`      | دسترسی به اجرای توابع یا پروSEDURES.                                    |
| `USAGE`        | دسترسی به استفاده از اشیاء مثل سchema یا sequence.                     |
| `ALL PRIVILEGES`| تمام دسترسی‌ها (جمع‌بندی دسترسی‌ها).                                  |

---

### **تفاوت بین `GRANT` و `REVOKE`:**
- **`GRANT`:** برای اعطای دسترسی‌ها استفاده می‌شود.
- **`REVOKE`:** برای حذف دسترسی‌ها استفاده می‌شود.
  - مثال:
    ```sql
    REVOKE SELECT ON table_name FROM user_name;
    ```

---

### **سناریوهای استفاده:**

#### **1. مدیریت دسترسی‌ها برای توسعه‌دهندگان:**
- ایجاد یک Role برای توسعه‌دهندگان (`developers`) و اعطای دسترسی‌های محدود به جداول:
  ```sql
  CREATE ROLE developers;
  GRANT SELECT, INSERT, UPDATE ON employees TO developers;
  ```

#### **2. مدیریت دسترسی‌ها برای مدیران سیستم:**
- ایجاد یک Superuser برای مدیران سیستم:
  ```sql
  CREATE ROLE admin WITH SUPERUSER;
  ```

#### **3. مدیریت دسترسی‌ها برای کاربران خواندنی:**
- ایجاد یک Role برای کاربرانی که فقط باید داده‌ها را خوانده و مشاهده کنند:
  ```sql
  CREATE ROLE readonly_users;
  GRANT SELECT ON ALL TABLES IN SCHEMA public TO readonly_users;
  ```

---

### **نکات مهم:**

1. **مالکیت شیء:** تنها مالک یک شیء (Owner) یا Superuser می‌تواند دسترسی‌ها را اعطا یا حذف کند.
2. **سطح دقت:** می‌توانید دسترسی‌ها را به سطح جدول، ستون، یا حتی سطر محدود کنید.
3. **استفاده از `WITH GRANT OPTION`:** این گزینه باید با احتیاط استفاده شود، زیرا می‌تواند منجر به انتقال دسترسی‌ها به دیگران شود.
4. **نمایش دسترسی‌ها:** برای مشاهده دسترسی‌های موجود بر روی یک شیء، می‌توانید از دستور `\z` استفاده کنید:
   ```sql
   \z table_name
   ```

# 28.Exxtension

### **مفهوم Extensions در پستگرس**

#### **تعریف:**
Extensions (افزونه‌ها) در پستگرس، ابزارهایی هستند که به صورت مستقل توسعه یافته‌اند و می‌توانند به قابلیت‌های پایگاه داده اضافه شوند. با استفاده از این افزونه‌ها، می‌توانید توابع جدید، نوع داده‌های جدید، عملکردهای پیشرفته، و حتی ساختارهای خاصی را به پستگرس اضافه کنید.

#### **نقش افزونه‌ها:**
- افزودن قابلیت‌های جدید به پستگرس بدون نیاز به تغییر کد منبع.
- بهبود عملکرد و کارایی پایگاه داده.
- فراهم کردن ابزارهای پیشرفته برای پردازش داده‌ها، مدیریت انواع داده‌های مختلف، و انجام محاسبات پیچیده.

---

### **دستورات مهم برای کار با Extensions**

#### **1. نمایش لیست افزونه‌های موجود:**
```sql
SELECT * FROM pg_available_extensions;
```
- این دستور لیست تمام افزونه‌هایی را که می‌توانید در پستگرس نصب کنید، نمایش می‌دهد.

#### **2. نصب یک افزونه:**
```sql
CREATE EXTENSION extension_name;
```
- مثال:
  ```sql
  CREATE EXTENSION postgis;
  ```
  این دستور افزونه `postgis` را در پایگاه داده فعلی نصب می‌کند.

#### **3. حذف یک افزونه:**
```sql
DROP EXTENSION extension_name [CASCADE];
```
- مثال:
  ```sql
  DROP EXTENSION postgis CASCADE;
  ```
  - `CASCADE`: اگر افزونه اشیاء دیگر (مثل جداول یا توابع) را تأثیر دهد، این گزینه آن اشیاء را نیز حذف می‌کند.

#### **4. نمایش افزونه‌های نصب‌شده:**
```sql
SELECT * FROM pg_extension;
```
- این دستور لیست افزونه‌هایی را که در پایگاه داده فعلی نصب شده‌اند، نمایش می‌دهد.

#### **5. بروزرسانی یک افزونه:**
```sql
ALTER EXTENSION extension_name UPDATE [TO new_version];
```
- مثال:
  ```sql
  ALTER EXTENSION postgis UPDATE TO '3.0';
  ```

---

### **کاربردهای افزونه‌ها**

افزونه‌ها می‌توانند در زمینه‌های مختلفی مورد استفاده قرار گیرند:

1. **پردازش داده‌های مکانی:**
   - افزونه‌هایی مثل `PostGIS` برای مدیریت داده‌های جغرافیایی و انجام محاسبات مکانی استفاده می‌شوند.

2. **پشتیبانی از انواع داده‌های خاص:**
   - افزونه‌هایی مثل `hstore`, `jsonb`, و `ltree` برای مدیریت داده‌های ساختاریابی شده یا سلسله مراتبی طراحی شده‌اند.

3. **بهینه‌سازی پرس‌وجو:**
   - افزونه‌هایی مثل `pg_trgm` و `btree_gin` برای افزایش سرعت جستجوی متنی یا انجام عملیات پیشرفته روی اندیس‌ها استفاده می‌شوند.

4. **مدیریت امنیت:**
   - افزونه‌هایی مثل `pgcrypto` برای رمزگذاری داده‌ها و امنیت پایگاه داده.

5. **پیاده‌سازی الگوریتم‌های پیشرفته:**
   - افزونه‌هایی مثل `fuzzystrmatch` برای مقایسه رشته‌ها و انجام عملیات شباهت‌سنجی.

---

### **سناریوهای استفاده از افزونه‌ها**

#### **1. مدیریت داده‌های مکانی با PostGIS:**
- اگر نیاز دارید تا داده‌های مکانی (مثل مختصات جغرافیایی) را ذخیره کرده و پردازش کنید، از افزونه `PostGIS` استفاده کنید.
  ```sql
  CREATE EXTENSION postgis;
  ```

#### **2. جستجوی متنی پیشرفته با pg_trgm:**
- برای انجام جستجوهای متنی که حساسیت به تلفظ یا ترتیب کلمات داشته باشد، از افزونه `pg_trgm` استفاده کنید.
  ```sql
  CREATE EXTENSION pg_trgm;
  SELECT word, similarity(word, 'search_term') FROM table_name ORDER BY similarity DESC;
  ```

#### **3. ذخیره‌سازی داده‌های ساختاریابی شده با hstore:**
- اگر نیاز دارید تا داده‌های کلید-مقدار را ذخیره کنید، از افزونه `hstore` استفاده کنید.
  ```sql
  CREATE EXTENSION hstore;
  CREATE TABLE my_table (id serial, data hstore);
  INSERT INTO my_table (data) VALUES ('key1 => value1, key2 => value2');
  ```

#### **4. رمزگذاری داده‌ها با pgcrypto:**
- برای رمزگذاری داده‌های حساس (مثل رمز عبور)، از افزونه `pgcrypto` استفاده کنید.
  ```sql
  CREATE EXTENSION pgcrypto;
  SELECT crypt('password', gen_salt('bf'));
  ```

#### **5. پشتیبانی از JSONB برای داده‌های ساختاریابی شده:**
- برای ذخیره‌سازی داده‌های JSON پیشرفته، از نوع داده `JSONB` و افزونه‌های مرتبط استفاده کنید.
  ```sql
  CREATE TABLE my_table (id serial, data jsonb);
  INSERT INTO my_table (data) VALUES ('{"key": "value"}');
  ```

---

### **مهمترین افزونه‌های موجود در پستگرس**

#### **1. PostGIS:**
- **توضیح:** برای مدیریت داده‌های جغرافیایی.
- **استفاده:** ذخیره‌سازی و پردازش مختصات GPS، مناطق، و خطوط.

#### **2. hstore:**
- **توضیح:** نوع داده کلید-مقدار برای ذخیره داده‌های غیرساختاریابی شده.
- **استفاده:** مدیریت داده‌های متغیر بدون نیاز به تعریف ستون‌های ثابت.

#### **3. pg_trgm:**
- **توضیح:** برای جستجوی متنی پیشرفته و محاسبه شباهت رشته‌ها.
- **استفاده:** جستجوی پیشرفته در متن‌ها.

#### **4. pgcrypto:**
- **توضیح:** برای رمزگذاری و امنیت داده‌ها.
- **استفاده:** رمزگذاری رمز عبور، داده‌های حساس.

#### **5. fuzzystrmatch:**
- **توضیح:** برای مقایسه رشته‌ها و محاسبه شباهت.
- **استفاده:** جستجوی تقریبی در داده‌های متنی.

#### **6. btree_gin:**
- **توضیح:** اندیس GIN برای پشتیبانی از عملکردهای بسته‌بندی (array, JSONB).
- **استفاده:** بهینه‌سازی پرس‌وجوهای پیشرفته.

#### **7. citext:**
- **توضیح:** نوع داده متنی حساس به حروف کوچک/بزرگ.
- **استفاده:** مدیریت داده‌های متنی بدون نگرانی از حساسیت حروف کوچک/بزرگ.

#### **8. intarray:**
- **توضیح:** برای پشتیبانی از عملیات پیشرفته روی آرایه‌های عددی.
- **استفاده:** جستجو و فیلتر آرایه‌های عددی.

---

### **نحوه دانلود و نصب Extensions در پستگرس**

#### **1. افزونه‌های داخلی (Built-in Extensions):**
پستگرس چندین افزونه داخلی دارد که به صورت پیش‌فرض با نسخه‌های مختلف پستگرس توزیع می‌شوند. این افزونه‌ها نیازی به دانلود جداگانه ندارند و فقط با استفاده از دستور `CREATE EXTENSION` قابل فعال‌سازی هستند.

##### **مثال:**
```sql
CREATE EXTENSION postgis;
```

---

#### **2. افزونه‌های موجود در بسته `postgresql-contrib`:**
برخی از افزونه‌ها در بسته جداگانه‌ای به نام `postgresql-contrib` توزیع می‌شوند. برای استفاده از این افزونه‌ها، باید ابتدا بسته `postgresql-contrib` را نصب کنید.

##### **مراحل نصب:**

**a. روی سیستم‌عامل‌های مبتنی بر Linux (مانند Ubuntu):**
1. **به‌روزرسانی لیست بسته‌ها:**
   ```bash
   sudo apt update
   ```

2. **نصب بسته `postgresql-contrib`:**
   ```bash
   sudo apt install postgresql-contrib
   ```

3. **فعال‌سازی افزونه در پایگاه داده:**
   ```sql
   CREATE EXTENSION extension_name;
   ```
   مثال:
   ```sql
   CREATE EXTENSION pg_trgm;
   ```

**b. روی سیستم‌عامل macOS (با استفاده از Homebrew):**
1. **نصب Postgres و بسته `contrib`:**
   ```bash
   brew install postgresql
   ```

2. **فعال‌سازی افزونه در پایگاه داده:**
   ```sql
   CREATE EXTENSION extension_name;
   ```

**c. روی Windows:**
- افزونه‌های `contrib` معمولاً در حین نصب پستگرس به طور پیش‌فرض نصب می‌شوند.
- برای فعال‌سازی افزونه، به صورت معمول از دستور `CREATE EXTENSION` استفاده کنید.

---

#### **3. افزونه‌های خارجی (Third-party Extensions):**
برخی افزونه‌ها توسط سومین افراد یا شرکت‌ها توسعه یافته‌اند و نیاز به دانلود و نصب جداگانه دارند.

##### **مراحل نصب:**

**a. یافتن منبع افزونه:**
- افزونه‌های خارجی معمولاً در وب‌سایت‌های رسمی یا سرویس‌هایی مثل [PGXN](https://pgxn.org/) (PostgreSQL Extension Network) قرار دارند.

**b. دانلود افزونه:**
- از وب‌سایت رسمی یا PGXN، فایل‌های مربوط به افزونه را دانلود کنید.

**c. نصب افزونه:**
1. **استخراج فایل‌ها:**
   ```bash
   tar -xzf extension_name.tar.gz
   cd extension_name
   ```

2. **ساخت و نصب:**
   ```bash
   make
   sudo make install
   ```

3. **فعال‌سازی افزونه در پایگاه داده:**
   ```sql
   CREATE EXTENSION extension_name;
   ```

---

#### **4. نصب افزونه‌ها از طریق Docker:**
اگر از Docker برای اجرای پستگرس استفاده می‌کنید، می‌توانید افزونه‌ها را به صورت زیر نصب کنید:

1. **استفاده از تصویر پستگرس با `contrib`:**
   ```bash
   docker run --name my-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres:latest
   ```

2. **فعال‌سازی افزونه در داخل کانتینر:**
   ```sql
   CREATE EXTENSION extension_name;
   ```

---

#### **5. بررسی نسخه‌های سازگار:**
قبل از نصب یک افزونه، مطمئن شوید که آن افزونه با نسخه پستگرس شما سازگار است. این اطلاعات معمولاً در مستندات افزونه یا وب‌سایت رسمی آن ذکر شده است.

---

#### **6. حل مشکلات نصب:**
- **مشکل 1:** افزونه پیدا نشد.
  - **حل:** اطمینان حاصل کنید که بسته `postgresql-contrib` نصب شده است.
  
- **مشکل 2:** خطای سازگاری نسخه.
  - **حل:** افزونه را با نسخه‌ای که با پستگرس شما سازگار است، دانلود و نصب کنید.

- **مشکل 3:** دسترسی نادرست.
  - **حل:** اطمینان حاصل کنید که با Role‌ای که دسترسی Superuser دارد، عملیات را انجام می‌دهید.

---