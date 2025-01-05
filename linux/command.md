## راهنمای دستورات لینوکس

این راهنما دستورات اساسی لینوکس را به همراه نحوه استفاده آنها به صورت دسته‌بندی شده برای مراجعه سریع ارائه می‌دهد.
شامل :

+ عملیات فایل و دایرکتوری
+ مجوزهای فایل
+ مشاهده و ویرایش فایل‌ها
+ اطلاعات سیستم
+ شبکه و اتصال به سرور
+ مدیریت فرآیندها و تاریخچه دستورات
+ سایر دستورات مفید

# 1. عملیات فایل و دایرکتوری

- **`ls`**: نمایش محتویات دایرکتوری.

  ```bash
  ls        # دیدن محتویات یک مسیر 
  ls -l     # لیست تفصیلی
  ls *.txt  #  دیدن همه فایلها با پسوند txt
  ls -ltch  # دیدن فایلها با مخصات بیشتر
  ```
- **فایل‌ها و دایرکتوری‌های مخفی**: برای نمایش فایل‌ها و دایرکتوری‌های مخفی (که با نقطه شروع می‌شوند) از گزینه `-a` استفاده کنید.

  ```bash
  ls -a
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
- **`man`**:دیدن دستور العمل هر  command

  ```bash
  man ls
  man cd
  ```
- **`whereis`**:دیدن محل ذخیره شدن فایل اجرایی هر  command

  ```bash
  whereis ls
  whereis cd
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

دیدن همه فایل های که نامشان با `file` شروع می شود

```bash
cat file*


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

آپدیت لیست رپو  نام ها- ایدکس ها- ادرس دانلود- و .. در سیستم اوکال `source.list` :
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
>> آفلاین نصب می کنیم
>>

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

# 9. :دستورات مربوط به ادمین

## `useradd`

```bash
sudo <command>  #دستورات بعد از sudoبا دسترسی ادمین اجرا می شوند

sudo useradd <username> #افزودن کاربر جدید 
sudo useradd -m <username> # افزودن کاربر جدید و ساخت هوم دایرکتوری

sudo useradd <username> -e 10-10-24 # افزودنن کاربر جدیدهمراه با تاریخ انقضا
sudo useradd <username> -g <groupname>  # افزودن کاربر جدید همراه با اضافه کردن به گروه مشخص
```

<hr>

## `groupadd`

```bash
sudo groupadd <groupname>
# ایجاد یک گروه جدید با نام مشخص
sudo groupadd developers

# ایجاد یک گروه جدید با GID مشخص
sudo groupadd -g <GID> <groupname>
sudo groupadd -g 1050 finance

# ایجاد گروه سیستمی (گروهی با GID کمتر از 1000)
sudo groupadd -r <groupname>
sudo groupadd -r system_group

# نمایش نسخه دستور groupadd
groupadd --version

# ایجاد گروه با تنظیمات پیش‌فرض (با توجه به فایل /etc/login.defs)
sudo groupadd <groupname>

#برای حذف یک گروه 
sudo groupdel <groupname>

```

فایل‌های مرتبط:

`/etc/group`: فایل حاوی لیست گروه‌ها در سیستم.
`/etc/login.defs`: فایل پیکربندی پیش‌فرض برای ایجاد کاربران و گروه‌ها.

<hr>

## `passwd`

دستور `passwd` برای مدیریت رمز عبور کاربران در سیستم‌های لینوکسی استفاده می‌شود

```bash
passwd
# تغییر رمز عبور کاربر فعلی

# تغییر رمز عبور یک کاربر دیگر (نیاز به دسترسی ریشه یا sudo)
sudo passwd <username>

# قفل کردن حساب کاربری (غیرفعال کردن رمز عبور کاربر)
sudo passwd -l <username>
sudo passwd -l john

# باز کردن قفل حساب کاربری
sudo passwd -u <username>

# حذف رمز عبور کاربر (امکان ورود بدون رمز عبور)
sudo passwd -d <username>
sudo passwd -d jane

# تنظیم تاریخ انقضای رمز عبور کاربر
sudo passwd -e <username>

# تغییر تعداد روزهای انقضا و اطلاع از انقضای رمز عبور
sudo passwd -n <minimum_days> -x <maximum_days> -w <warning_days> <username>

# (رمز عبور کاربر "john" پس از 90 روز منقضی می‌شود و 10 روز قبل از انقضا هشدار داده می‌شود.)
sudo passwd -x 90 -w 10 john


# مشاهده اطلاعات مربوط به رمز عبور کاربر (فقط توسط کاربر ریشه)
sudo passwd -S <username>

```

`-l` : قفل کردن حساب (Lock). 
`-u` : باز کردن قفل حساب (Unlock).
`-d` : حذف رمز عبور.
`-e` : مجبور کردن کاربر به تغییر رمز عبور در ورود بعدی.
`-n` : تنظیم تعداد روزهای حداقل برای تغییر رمز عبور.
`-x` : تنظیم تعداد روزهای حداکثر برای انقضای رمز عبور.
`-w` : تعداد روزهای اطلاع‌رسانی قبل از انقضای رمز عبور.
`-S` : نمایش وضعیت رمز عبور کاربر.

<hr>

## `usermode`

دستور `-aG` باعث می‌شود که کاربر به یک گروه اضافه شود بدون اینکه از گروه‌های دیگر حذف شود. (append Group)

```bash

sudo usermod -aG <groupname> <username>
# افزودن یک کاربر به گروه مشخص

# افزودن کاربر به گروه docker (برای استفاده از داکر بدون نیاز به sudo)
sudo usermod -aG docker <username>

# تغییر نام کاربری
sudo usermod -l <new_username> <old_username>

# قفل کردن حساب کاربری
sudo usermod -L <username>

# باز کردن قفل حساب کاربری
sudo usermod -U <username>

# تغییر پوشه خانگی (home directory) کاربر
sudo usermod -d /new/home/directory <username>

# تغییر پوشه خانگی و انتقال فایل‌های موجود به پوشه جدید
sudo usermod -d /new/home/directory -m <username>

# تغییر UID کاربر
sudo usermod -u <new_uid> <username>

# تغییر GID گروه اصلی کاربر
sudo usermod -g <new_gid> <username>

```

<hr>

## `groupmod`

دستور `groupmod` برای تغییر تنظیمات گروه‌های موجود در سیستم‌های لینوکسی استفاده می‌شود.

```bash
sudo groupmod -n <new_groupname> <old_groupname>
# تغییر نام یک گروه
sudo groupmod -n engineers developers


# تغییر GID یک گروه
sudo groupmod -g <new_GID> <groupname>
sudo groupmod -g 2000 finance

# تغییر نام و GID گروه به‌طور همزمان
sudo groupmod -n <new_groupname> -g <new_GID> <old_groupname>
sudo groupmod -n admins -g 1500 staff

```

<hr>

## `chown`

دستور `chown` برای تغییر مالکیت (owner) و گروه (group) فایل‌ها و دایرکتوری‌ها در لینوکس استفاده می‌شود.

```bash
sudo chown <new_owner> <file_or_directory>
# تغییر مالک فایل یا دایرکتوری
sudo chown alice file.txt


# تغییر گروه فایل یا دایرکتوری
sudo chown :<new_group> <file_or_directory>
sudo chown :developers /var/www/

# تغییر هم‌زمان مالک و گروه فایل یا دایرکتوری
sudo chown <new_owner>:<new_group> <file_or_directory>
sudo chown alice:developers project.zip

# تغییر مالک و گروه همه فایل‌ها و دایرکتوری‌های داخل یک مسیر به‌صورت بازگشتی
sudo chown -R <new_owner>:<new_group> <directory>
sudo chown -R bob:staff /home/bob/

# تغییر فقط مالکیت فایل‌ها (بدون تغییر گروه)
sudo chown --changes <new_owner> <file_or_directory>

# تغییر مالک و گروه یک مسیر خاص و نمایش جزئیات تغییرات
sudo chown --verbose <new_owner>:<new_group> <file_or_directory>

```

<hr>

## `chmod`

دستور `chmod` برای تغییر مجوزهای دسترسی (Permissions) فایل‌ها و دایرکتوری‌ها در سیستم‌های لینوکسی استفاده می‌شود.

```bash
ls -l # دیدن مجوز دسترسی ها

chmod [options] <permissions> <file_or_directory>
# تغییر مجوزها به صورت عددی (مثلاً 755)
chmod 755 <file_or_directory>

# تغییر مجوزها به صورت نمادین (مثلاً افزودن مجوز اجرا برای مالک)
chmod u+x <file_or_directory>

# حذف مجوز نوشتن از گروه
chmod g-w <file_or_directory>

# تنظیم مجوزها برای همه کاربران (مالک، گروه و دیگران)
chmod a+r <file_or_directory>

```

نمادهای مربوط به مجوزها:

سه بخش اصلی مجوزها:
`u`: مالک (user)
`g`: گروه (group)
`o`: دیگران (others)
`a`: همه (all)

نوع دسترسی:
`r`:4: خواندن (read)
`w`:2: نوشتن (write)
`x`:1: اجرا (execute)

عملیات:
`+`: افزودن مجوز
`-`: حذف مجوز
`=`: تنظیم مجوز به‌طور دقیق

مثال:

```bash
chmod u+x script.sh
# به فایل مجوز اجرا برای مالک اضافه می‌شود.

chmod g-w file.txt
# مجوز نوشتن از گروه برای فایل حذف می‌شود.

chmod 744 file.txt
# این دستور به مالک مجوز خواندن، نوشتن، و اجرا، و به دیگران فقط مجوز خواندن می‌دهد.

chmod u=rwx,g=rx,o=r file.txt
#این دستور مجوزها را به‌طور دقیق برای فایل به این شکل تنظیم می‌کند:
# مالک: خواندن، نوشتن، و اجرا (rwx)
# گروه: خواندن و اجرا (rx)
# دیگران: خواندن (r)

```

<hr>

## `chgrp`

دستور `chgrp` در لینوکس برای تغییر گروه مالک (Group Ownership) فایل‌ها و دایرکتوری‌ها استفاده می‌شود.

```bash
sudo chgrp <groupname> <file_or_directory>
# تغییر گروه یک فایل یا دایرکتوری
sudo chgrp developers file.txt  # file
sudo chgrp staff /var/www       # dir

# تغییر گروه فایل‌ها و دایرکتوری‌ها به صورت بازگشتی
sudo chgrp -R <groupname> <directory>
sudo chgrp -R admins /home/project

# نمایش جزئیات تغییر گروه‌ها
sudo chgrp --verbose <groupname> <file_or_directory>
sudo chgrp --verbose users report.txt

```

### ترکیب با دستورات دیگر:

ترکیب با `chown`: تغییر مالک و گروه هم‌زمان:

```bash
sudo chgrp developers file.txt
sudo chmod 775 file.txt

sudo chown user:developers file.txt

```

# 10.سایر دستورات مفید:

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
---

# 10.`cp`

برای انتقال فایل از یک محیط به محیط دیگر


`-i`

1. **Interactive (درخواست تأیید قبل از بازنویسی):**
کپی دایرکتوری‌ها و محتویاتشان به صورت بازگشتی.

```sh
cp -i SOURCE DESTINATION
cp -i file1.txt file2.txt
```
`-r`

2. **Recursive (کپی بازگشتی دایرکتوری‌ها):**
  ```sh
  cp -r SOURCE DESTINATION
  cp -r dir1/ dir2/
  ```
`-v`

3. **Verbose (نمایش فایل‌های کپی‌شده):**
```sh
cp -v SOURCE DESTINATION
cp -v file1.txt file2.txt
```
`-f`

4. **Force (اجبار به بازنویسی فایل‌ها بدون تأیید):**
```sh
cp -f SOURCE DESTINATION
cp -f file1.txt file2.txt
```
`-u`

5. **Update (کپی فقط فایل‌های جدیدتر یا ناموجود در مقصد):**
```sh
cp -u SOURCE DESTINATION
cp -u file1.txt file2.txt
```
`-p`

6. **Preserve (حفظ ویژگی‌های فایل):**
```sh
cp -p SOURCE DESTINATION
cp -p file1.txt file2.txt
```
`-a`

7. **Archive (کپی به صورت بایگانی):**

سایر ویژگی های ان فایل مانند سطوح دسترسی و مالکیت را نیز حفط می کند.
```sh
cp -a SOURCE DESTINATION
cp -a dir1/ dir2/
```

# 11.`mv`

برای انتقال فایل از یک محیط به محیط دیگر

`-i`

1. **Interactive (درخواست تأیید قبل از بازنویسی):**

تأیید قبل از بازنویسی فایل‌های موجود.
```sh
mv -i SOURCE DESTINATION
mv -i file1.txt file2.txt
```
`-v`

2. **Verbose (نمایش فایل‌های جابجا شده):**

نمایش فایل‌های جابجا شده در طول عملیات جابجایی.
```sh
mv -v SOURCE DESTINATION
mv -v file1.txt file2.txt
```
`-f`

3. **Force (اجبار به بازنویسی فایل‌ها بدون تأیید):**

اجبار به بازنویسی فایل‌ها بدون درخواست تأیید.
```sh
mv -f SOURCE DESTINATION
mv -f file1.txt file2.txt
```

`-u`

4. **Update (جابجایی فقط فایل‌های جدیدتر یا ناموجود در مقصد):**

جابجایی فقط فایل‌هایی که جدیدتر از فایل‌های موجود در مقصد هستند یا در مقصد وجود ندارند.
```sh
mv -u SOURCE DESTINATION
mv -u file1.txt file2.txt
```

---

# `find`

دستور `find` در لینوکس برای جستجوی فایل‌ها و دایرکتوری‌ها بر اساس معیارهای مختلف مانند نام، نوع، اندازه، زمان تغییر و غیره استفاده می‌شود. این دستور یکی از ابزارهای قدرتمند و انعطاف‌پذیر برای مدیریت فایل‌ها در سیستم‌عامل‌های شبه‌یونیکس است.

## `-name`

1. **Search by Name (جستجو براساس نام):**

جستجو فایل‌ها و دایرکتوری‌ها براساس نام.
   ```sh
   find /path -name "filename"
   find /home/user -name "file.txt"
   ```
## `-type`

2. **Search by Type (جستجو براساس نوع):**

جستجو فایل‌ها یا دایرکتوری‌ها براساس نوع.
   ```sh
   find /path -type TYPE
   find /home/user -type f  # For files
   find /home/user -type d  # For directories
   ```
## `-size`

3. **Search by Size (جستجو براساس اندازه):**

جستجو فایل‌ها براساس اندازه.
   ```sh
   find /path -size SIZE
   find /home/user -size +100M  # Files larger than 100MB
   ```

## `-mtime`

4. **Search by Modification Time (جستجو براساس زمان تغییر):**

جستجو فایل‌ها براساس زمان آخرین تغییر.
   ```sh
   find /path -mtime N
   find /home/user -mtime -7  # Files modified in the last 7 days
   ```


## `-exec`

5. **Execute Command (اجرای دستور بر روی نتایج جستجو):**

اجرای دستور خاص بر روی نتایج جستجو.
   ```sh
   find /path -name "filename" -exec COMMAND {} \;
   find /home/user -name "*.log" -exec rm {} \;  # Delete all .log files
   ```

## `-perm`

6. **Search by Permissions (جستجو براساس مجوزها):**

جستجو فایل‌ها براساس مجوزهای دسترسی.
   ```sh
   find /path -perm MODE
   find /home/user -perm 644  # Files with 644 permissions
   ```
