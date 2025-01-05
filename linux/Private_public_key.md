# Private & Public Key

کلیدهای خصوصی (Private Key) و عمومی (Public Key) در رمزنگاری کلید عمومی (Public Key Cryptography) استفاده می‌شوند. این تکنیک به دو کلید نیاز دارد: یک کلید خصوصی که باید به صورت محرمانه نگهداری شود، و یک کلید عمومی که می‌تواند به اشتراک گذاشته شود. این کلیدها به صورت ریاضی به یکدیگر مرتبط هستند و از آنها برای رمزنگاری و امضای دیجیتال استفاده می‌شود.


>> `Private` Key : on __`Local`__ system

>> `Public` Key :  on __`Remote`__ System



### توضیحات مختصر
- **کلید خصوصی (Private Key)**: این کلید باید به صورت امن نگهداری شود و تنها دارنده آن می‌تواند از آن استفاده کند. برای رمزگشایی داده‌ها یا امضای دیجیتال استفاده می‌شود.
- **کلید عمومی (Public Key)**: این کلید می‌تواند به دیگران به اشتراک گذاشته شود. برای رمزنگاری داده‌ها یا تأیید امضای دیجیتال استفاده می‌شود.

### مراحل ایجاد کلیدهای عمومی و خصوصی و استفاده از آنها در سیستم لوکال و ریموت

## 1. ایجاد کلیدهای عمومی و خصوصی
برای ایجاد کلیدهای عمومی و خصوصی، می‌توانید از ابزار `ssh-keygen` استفاده کنید.

**دستور:**
```sh
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# یا فقط دستور زیر را بنویسیم
ssh-keygen 
```

**توضیحات:**
- `-t rsa`: نوع الگوریتم کلید (در اینجا RSA).
- `-b 4096`: طول کلید (4096 بیت).
- `-C "your_email@example.com"`: کامنت برای کلید (معمولاً ایمیل شما).

**خروجی:**
```plaintext
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):
# نام فایل و مسیر را میتوانیم اتخاب کنیم اگر انتاب نکنیم دیفالت می گذارد

Enter passphrase (empty for no passphrase):
Enter same passphrase again:
# میتوانیم پسورد بگذاریم و یا ننگذاریم

Your identification has been saved in /home/user/.ssh/id_rsa.
Your public key has been saved in /home/user/.ssh/id_rsa.pub.
The key fingerprint is:
SHA256:xyz12345 your_email@example.com
The key's randomart image is:
+---[RSA 4096]----+
|     ...         |
|      . o o      |
|       o B       |
|      . o + .    |
|     . . S +     |
|    E = + o .    |
|     o O * .     |
|      + * = o    |
|       o.o+ .    |
+----[SHA256]-----+
```
حالا دو کلید زیر در مسیر `/home/user/.ssh` ساخته می شوند
>> `id_rsa`     : private key
 
>> `id_rsa.pub` : public key



## 2. حالا وقت آن هست کلید عمومی را به سرور ریموت بفرستیم
برای کپی کردن کلید عمومی به سیستم ریموت، می‌توانید از `ssh-copy-id` استفاده کنید.

**دستور:**
```sh
ssh-copy-id user@remote_host
# مثلا
ssh-copy-id sajad@38.24.91.125
```

**توضیحات:**
- `user@remote_host`: نام کاربر و آدرس سیستم ریموت.

**خروجی:**
```plaintext
/usr/bin/ssh-copy-id: INFO: Source of key(s) to be installed: "/home/user/.ssh/id_rsa.pub"
The authenticity of host 'remote_host (192.168.1.100)' can't be established.
ECDSA key fingerprint is SHA256:xyz12345.
Are you sure you want to continue connecting (yes/no)? yes
user@remote_host's password:
Number of key(s) added: 1

Now try logging into the machine, with: "ssh 'user@remote_host'"
and check to make sure that only the key(s) you wanted were added.
```

## 3. اتصال به سیستم ریموت با استفاده از کلید خصوصی
اکنون می‌توانید با استفاده از کلید خصوصی به سیستم ریموت متصل شوید.

**دستور:**
```sh
ssh user@remote_host
# مثلا
ssh sajad@38.24.91.125
```

**توضیحات:**
- `user@remote_host`: نام کاربر و آدرس سیستم ریموت.

**خروجی:**
```plaintext
Welcome to Ubuntu 20.04.1 LTS (GNU/Linux 5.4.0-42-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

Last login: Thu Jul 23 15:42:19 2020 from 192.168.1.2
sajad@38.24.91.125:~$
```

این مراحل به شما امکان می‌دهد که کلیدهای عمومی و خصوصی را ایجاد کنید و از آنها برای اتصال امن به سیستم ریموت استفاده کنید. 