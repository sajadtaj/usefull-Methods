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

+  `/var/log/postgresql/`

+  `/usr/lib/postgresql/14/bin/logfile `


### 1. /usr/lib/postgresql/14/bin/logfile


ماهیت: این فایل می‌تواند یک لاگ موقت یا کاربردی در مسیر باینری‌های PostgreSQL باشد.

کاربرد:

+  معمولاً این نوع فایل‌ها برای اجرای مستقیم دستورات باینری استفاده می‌شوند، یا به عنوان لاگ‌هایی مرتبط با اسکریپت‌های تستی یا ابزارهای خاص که با نسخه‌ی خاصی از PostgreSQL کار می‌کنند، ایجاد می‌شوند.
+  احتمالاً توسط خود PostgreSQL تولید نشده باشد و نتیجه اجرای دستی یک ابزار باشد.

موقعیت:

در مسیر باینری‌های PostgreSQL ذخیره شده که ابزارهای مرتبط با اجرای نسخه‌ی خاصی از PostgreSQL را در خود جای می‌دهد.
دسترسی به این مسیر معمولاً برای کاربران عادی محدود است و بیشتر سیستم‌ادمین‌ها یا کاربران خاص به آن دسترسی دارند.


### 2. /var/log/postgresql

ماهیت:
این مسیر محل پیش‌فرض ثبت لاگ‌های سیستم PostgreSQL است که توسط سرویس اصلی پایگاه داده مدیریت می‌شود.
کاربرد:
شامل لاگ‌های مختلف نظیر:
+  لاگ‌های عملیاتی : شروع و توقف سرویس‌ها
+  لاگ‌های خطا: خطاهای سیستمی یا مرتبط با اجرای Queryها
+  لاگ‌های دسترسی : اطلاعات درباره‌ی کاربرانی که به پایگاه داده متصل شده‌اند
+  این فایل‌ها به طور پیش‌فرض توسط سیستم لاگینگ PostgreSQL (مانند log_directory و log_destination) مدیریت و تولید می‌شوند.

موقعیت:
+  در مسیر پیش‌فرض لاگ‌های سیستم (مانند /var/log/) ذخیره شده و نیازمند دسترسی ریشه‌ای (root) یا دسترسی کاربران خاص سرویس PostgreSQL است.
+  این مسیر به صورت مداوم و پویا به‌روزرسانی می‌شود.




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

    برای تغییر مسیر ذخیره دیتا باید مسیر زیر را تغییر دهیم به مسیر دلواه

Output:

    data_directory = 'ConfigDir'		# use data in another directory

## راه اندازی سرویس `postgresql`

بعد از تعریف دیتابیس باید مجدد سرویس را بالا بیاریم توجه داشته باشید ممک است کاربر pstgres اختیار ایکار را ننداشته باشد و مجبور باشید از کاربر بالاتری کمک بگیریم.

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

1. **type**: نوع اتصال (محلی یا از راه دور).
2. **database**: نام دیتابیس یا دیتابیس‌هایی که دسترسی به آنها مجاز است.
3. **user**: کاربر یا کاربران مجاز برای دسترسی.
4. **address**: آدرس IP یا محدوده‌ای از آدرس‌های IP که اجازه دسترسی دارند.
5. **method**: روش احراز هویت.

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

```sql
CREATE TABLESPACE mytablespace LOCATION '/path/to/directory';
```

در این دستور:
- `mytablespace`: 

نام Tablespace جدیدی که می‌خواهید ایجاد کنید.
- `/path/to/directory`:

 مسیر دایرکتوری‌ای که قبلاً در سیستم فایل ایجاد کرده‌اید و PostgreSQL باید به آن دسترسی داشته باشد.

بعد از ایجاد Tablespace، می‌توانید جداول یا ایندکس‌های خود را در این Tablespace قرار دهید. برای مثال، برای ایجاد یک جدول در Tablespace جدید، می‌توانید از دستور زیر استفاده کنید:

```sql
CREATE TABLE mytable (
    id serial PRIMARY KEY,
    data text
) TABLESPACE mytablespace;
```

این دستور یک جدول جدید به نام `mytable` ایجاد می‌کند و آن را در Tablespace `mytablespace` قرار می‌دهد.


در این دایرکتوری، PostgreSQL فایل‌هایی ایجاد خواهد کرد که داده‌های جداول و ایندکس‌هایی که در این Tablespace قرار داده شده‌اند، ذخیره می‌کند. این فایل‌ها شامل بلوک‌های داده و سایر اطلاعات مرتبط با دیتابیس خواهند بود.

اطمینان حاصل کنید که کاربر PostgreSQL (معمولاً `postgres`) به این دایرکتوری دسترسی نوشتن دارد تا بتواند فایل‌ها را ایجاد و مدیریت کند. 