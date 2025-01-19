### مراحل ایجاد کلاستر PostgreSQL در یک مسیر متفاوت و تنظیم آن در `systemd`

#### 1. ایجاد کلاستر جدید در مسیر داده متفاوت

ابتدا باید یک کلاستر جدید PostgreSQL را در یک مسیر دلخواه ایجاد کنید. برای این کار مراحل زیر را دنبال کنید:

```bash
# ایجاد مسیر دایرکتوری داده و لاگ
mkdir  /tmp/temp_db
mkdir /tmp/temp_log

# ایجاد فایل نگهداری لاگ ای کلاستر
mkdir /tmp/temp_log/logfile
```

#### 2. اجرای کلاستر به صورت موقت برای اطمینان از صحت عملکرد
`-D` : برای مشخص کرد دیتا دایرکتوری

`-l` : برای مشحص کرد نگهداری لاگ 
```bash
/usr/lib/postgresql/14/bin/pg_ctl -D /tmp/temp_db -l /tmp/temp_log/logfile start
```

#### 3. ایجاد فایل سرویس `systemd`

برای اینکه کلاستر PostgreSQL جدید را با استفاده از `systemctl` مدیریت کنید، یک فایل سرویس جدید ایجاد کنید:

```bash
sudo nano /etc/systemd/system/<postgresql-custom>.service
```
>> postgresql-custom : نام دلخواه برای سرویس

#### 4. پیکربندی فایل سرویس

محتویات زیر را در فایل سرویس اضافه کنید:

```ini
[Unit]
Description=PostgreSQL database server for custom cluster
After=network.target

[Service]
Type=forking
User=postgres
EnvironmentFile= /tmp/temp_db/postgresql.conf
ExecStart=/usr/lib/postgresql/14/bin/pg_ctl -D /path/to/custom_db -l /path/to/custom_log/logfile start
ExecStop=/usr/lib/postgresql/14/bin/pg_ctl -D /path/to/custom_db stop
ExecReload=/usr/lib/postgresql/14/bin/pg_ctl -D /path/to/custom_db reload
PIDFile=/path/to/custom_db/postmaster.pid

[Install]
WantedBy=multi-user.target
```

#### 5. تنظیمات کانفیگ مورد نظر


```bash
nano /tmp/temp_db/postgresql.conf
```

اعمال تغییرات
```ini
#PGPORT=5432   
# تغییر به 
PGPORT=5433
```

#### 6. بارگذاری مجدد تنظیمات `systemd` و فعال‌سازی سرویس

```bash
sudo systemctl daemon-reload
sudo systemctl enable postgresql-custom
```
>> postgresql-custom : نام دلخواه برای سرویس


#### 7. شروع سرویس PostgreSQL

```bash
sudo systemctl start postgresql-custom
```
>> postgresql-custom : نام دلخواه برای سرویس


#### 8. بررسی وضعیت سرویس

برای اطمینان از اینکه سرویس به درستی اجرا شده است، وضعیت آن را بررسی کنید:

```bash
sudo systemctl status postgresql-custom
```
>> postgresql-custom : نام دلخواه برای سرویس



Output:

        postgres@TAJ:/usr/lib/postgresql/14/bin$ systemctl status postgresql-14
        ● postgresql-14.service - PostgreSQL database server for custom cluster
            Loaded: loaded (/etc/systemd/system/postgresql-14.service; enabled; vendor preset: enabled)
            Active: active (running) since Sun 2025-01-19 11:02:48 +0330; 22s ago
            Process: 99023 ExecStart=/usr/lib/postgresql/14/bin/pg_ctl -D /tmp/temp_db/ -l /tmp/temp_log/logfile start (code=exited, >
        Main PID: 99026 (postgres)
            Tasks: 7 (limit: 18180)
            Memory: 16.9M
                CPU: 46ms
            CGroup: /system.slice/postgresql-14.service
                    ├─99026 /usr/lib/postgresql/14/bin/postgres -D /tmp/temp_db
                    ├─99028 "postgres: checkpointer " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
                    ├─99029 "postgres: background writer " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
                    ├─99030 "postgres: walwriter " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" >
                    ├─99031 "postgres: autovacuum launcher " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
                    ├─99032 "postgres: stats collector " "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" "" ""
                    └─99033 "postgres: logical replication launcher " "" "" "" "" "" "" "" "" "" "" "" ""
        lines 1-16/16 (END)


        postgres@TAJ:/usr/lib/postgresql/14/bin$ ss -ntl
        State         Recv-Q        Send-Q                 Local Address:Port                 Peer Address:Port        Process        
        LISTEN        0             244                        127.0.0.1:5432                      0.0.0.0:*                          
        LISTEN        0             244                        127.0.0.1:5433                      0.0.0.0:*                          
        LISTEN        0             4096                   127.0.0.53%lo:53                        0.0.0.0:*                          
        LISTEN        0             128                        127.0.0.1:631                       0.0.0.0:*                          
        LISTEN        0             128                            [::1]:631                          [::]:*                          
        postgres@TAJ:/usr/lib/postgresql/14/bin$ 
