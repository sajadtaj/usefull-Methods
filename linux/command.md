## راهنمای دستورات لینوکس

این راهنما دستورات اساسی لینوکس را به همراه نحوه استفاده آنها به صورت دسته‌بندی شده برای مراجعه سریع ارائه می‌دهد.
شامل :

+ عملیات فایل و دایرکتوری
+  مجوزهای فایل
+ مشاهده و ویرایش فایل‌ها
+ اطلاعات سیستم
+ شبکه و اتصال به سرور
+ مدیریت فرآیندها و تاریخچه دستورات
+  سایر دستورات مفید 



# 1. عملیات فایل و دایرکتوری
- **`ls`**: نمایش محتویات دایرکتوری.
  ```bash
  ls -l  # لیست تفصیلی
  ```
- **`cd`**: تغییر دایرکتوری.
  ```bash
  cd /home/user  # دایرکتوری مطلق
  cd new_folder  # دایرکتوری نسبی
  ```
- **`pwd`**: نمایش دایرکتوری کاری فعلی.
  ```bash
  pwd
  ```
- **`mkdir`**: ایجاد یک دایرکتوری جدید.
  ```bash
  mkdir new_folder
  ```
- **`rmdir`**: حذف یک دایرکتوری خالی.
  ```bash
  rmdir old_folder
  ```
- **`rm`**: حذف فایل‌ها یا دایرکتوری‌ها.
  ```bash
  rm file.txt
  ```
- **`touch`**: ایجاد یک فایل خالی.
  ```bash
  touch newfile.txt
  ```
- **`stat`**: نمایش اطلاعات دقیق یک فایل یا دایرکتوری.
  ```bash
  stat file.txt
  ```
- **فایل‌ها و دایرکتوری‌های مخفی**: برای نمایش فایل‌ها و دایرکتوری‌های مخفی (که با نقطه شروع می‌شوند) از گزینه `-a` استفاده کنید.
  ```bash
  ls -a
  ```

# 2. مجوزهای فایل
- **`chmod`**: تغییر مجوزهای فایل.
  ```bash
  chmod 755 script.sh
  ```
- **`chown`**: تغییر مالک و گروه فایل.
  ```bash
  chown user:group file.txt
  ```
- **`chgrp`**: تغییر مالکیت گروه یک فایل.
  ```bash
  chgrp groupname file.txt
  ```

# 3. مشاهده و ویرایش فایل‌ها
**`cat`**: نمایش محتویات فایل.

```bash
cat file*
```
دیدن همه فایل های که نامشان با `file` شروع می شود
```bash

```

- **دستورات مرتبط با `grep`**: جستجو در خروجی دستورات با استفاده از `pipe`.
```bash 
ls -l | grep "pattern"  
```
- **دستگاه شمارش کلمات (`wc`)**: شمارش خطوط، کلمات و کاراکترها در یک فایل.
```bash 
wc file.txt  
```

# 4. اطلاعات سیستم
- **`top`**: نمایش فرآیندهای در حال اجرا به صورت زنده.
- **`df`**: نمایش استفاده از فضای دیسک.
```bash 
df -h  
```
- **`free`**: نمایش استفاده از حافظه.
```bash 
free -m  
```
- **`uname -a`**: نمایش اطلاعات سیستم.
```bash 
uname -a  
```
- **`hostnamectl`**: نمایش یا تنظیم نام میزبان سیستم.
```bash 
hostnamectl  
```
- **نام کاربری جاری (`whoami`)**:
```bash 
whoami  
```
- **نمایش کاربران وارد شده (`who`)**:
```bash 
who  
```

# 5. شبکه و اتصال به سرور
- **`ssh username@hostname`**: اتصال به یک ماشین خارجی با پروتکل SSH.
```bash 
ssh user@hostname  
```
- **دستورات `wget` و `curl`: برای دانلود فایل‌ها از اینترنت.**
```bash 
wget http://example.com/file.zip  
```
```bash 
curl -O http://example.com/file.zip  
```

# 6. مدیریت فرآیندها و تاریخچه دستورات
**دستورات مدیریت فرآیندها (`bg`, `fg`, `jobs`)**:

 کار پس‌زمینه:

```bash 
bg 
```

کار پیش‌زمینه:

```bash 
fg 
```

لیست کارها:

```bash 
jobs 
```
      
**تاریخچه دستورات (`history`)**:

```bash 
history  
```

## 7. متغیرها و محیط برنامه نویسی شل
- **متغیرها (`variables`)**:
```bash 
VAR=value  
```
 **متغیرهای ویژه (`special variables`)**:

 `$?`: کد خروج آخرین دستور اجرا شده.

 `$$`: شناسه فرآیند جاری.

- **تنظیم متغیر محیطی (`export`)**:
```bash 
export VAR=value  
```
- **حذف متغیر (`unset`)**:
```bash 
unset VAR  
```
- **استفاده از `source .`: بارگذاری مجدد تنظیمات شل.**
```bash 
source ~/.bashrc  
```

# 8. مدیریت بسته‌ها (Package Management)
### برای توزیع‌های مبتنی بر Debian (مانند Ubuntu):

آپدیت لیست رپو های در سیستم اوکال `source.list` :
‍‍‍
```bash
apt update
```

دید اطلاعات(`info`) در خصوص آن پکیج
```bash
apt info package_name
```

آپگرید پکیج های موجود
```bash
apt upgrade
```

پکیج های صب شده بروی سیستم
```bash
apt list --installed
```

- **نصب بسته‌ها (`apt`, `apt-get`, `dpkg`)**
```bash 
sudo apt install package_name  
```
```bash 
sudo apt-get remove package_name  
```


برای نصب برنامه های که در انتهای آنها پسونند ‍`.deb` داریم بصورت افلاین :

```bash 
# i = --install
dpkg -i package.deb  
```

### مثال:

>> ابتدا پکیج را دالود می کیم و سپس  آنرا بصورت 
آفلاین نصب می کنیم
### نکته : dpkg چون از افلاینن نصب میکند اگر dependency موجود نباشد به خطا میخورد

```bash
# Download postgresql
# curl -o yourname.deb Address
# download all from Address to -> pg17main.deb
curl -0 pg17main.deb  https://apt.postgresql.org/pub/repos/apt/pool/main/p/postgresql-17/postgresql-17_17.2-1.pgdg%2B1_amd64.deb

#install
dpkg -i pg17main.deb

# Show All dependency of 
dpkg --contents pg17main.deb
```

*دیدن لیست رپو های انلای موجود برای یک پکیج وقتی میخواهیم یک پکیج را پیدا و سپس نسخه ماسب را نصب کنیم*

```bash
apt search --names-only postgre |grep post
```

### دانلود پکیج ها بدون نصب

**دانلود پکیج و نیازمندی های آن بدون نصب (مثلا سب دانلود کنیم تا فردا نصب کنیم)**

```bash
apt-get install--downlad-only  <package_name>
```

دانلود فقط خود برنامه 
```bash
apt-get download <package_name>
```


### پاک کردن پکیج ها
پکیج مورد ننظر پاک می شود اما نیازمندی های آن که نصب شده باقی می ماند.
‍‍‍
```bash
apt-get remove <package_name>
```

پاک کردنن پکیج های dependency که بخاطر یک پکیج دیگر نصب شده اند و الان دیگر به آنها نیازی نیست:


```bash
apt-get autoremove <package_name>
```

پاک کردن همه نیازممندی های درون سیستم که بلا استفاده هستند.

```bash
apt-get autoremove 
```

## سایر دستورات مفید:

**دستور `sleep`: برای تأخیر در اجرای دستورات.**

```bash 
sleep 5   # تأخیر به مدت پنج ثانیه
```
**دستور `man`: برای مشاهده راهنمای دستورات.**

```bash 
man ls   # مشاهده راهنمای دستور ls
```
**فلگ `-i‍`  حساسیت کوچکی و بزرگی عبارات را نادیده میگیرد**

```bash
# find sajad SAJAD Sajad SaJaD
find -i sajad  
```