##### Содержание
[Домашня работа №15](#HW15)    
[Домашня работа №16](#HW16)    
[Домашня работа №17](#HW17)
[Домашня работа №18](#HW18)

<a name="HW15"></a>
## Примечание к ДЗ№15
1. Машина в облаки Goole
2.
```
[root@jenkins tihomirovnv]# cat /etc/redhat-release
CentOS Linux release 7.7.1908 (Core)
```

3.
```
[root@jenkins tihomirovnv]# docker version
Client:
 Version:         1.13.1
 API version:     1.26
 Package version: docker-1.13.1-103.git7f2769b.el7.centos.x86_64
 Go version:      go1.10.3
 Git commit:      7f2769b/1.13.1
 Built:           Sun Sep 15 14:06:47 2019
 OS/Arch:         linux/amd64

Server:
 Version:         1.13.1
 API version:     1.26 (minimum version 1.12)
 Package version: docker-1.13.1-103.git7f2769b.el7.centos.x86_64
 Go version:      go1.10.3
 Git commit:      7f2769b/1.13.1
 Built:           Sun Sep 15 14:06:47 2019
 OS/Arch:         linux/amd64
 Experimental:    false

```

```
[root@jenkins tihomirovnv]# docker-compose --version
docker-compose version 1.18.0, build 8dd22a9
```

```
[root@jenkins tihomirovnv]# /usr/local/bin/docker-machine -version
docker-machine version 0.16.0, build 702c267f
```

4. docker ps -a (произвожу тестирования ansible roles molecule+docker, вижу ее остатки )
```
-bash-4.2$ docker ps -a
CONTAINER ID        IMAGE                   COMMAND                  CREATED             STATUS                  PORTS               NAMES
9e72053ca3cb        molecule_local/ubuntu   "bash -c 'while tr..."   46 hours ago        Up 46 hours                                 ubuntu_16_04
ba649db911cb        hello-world             "/hello"                 2 days ago          Exited (0) 2 days ago                       flamboyant_curran
1a3d0c361965        hello-world             "/hello"                 2 days ago          Exited (0) 2 days ago                       cocky_carson
de0a26de4cba        hello-world             "/hello"                 2 days ago          Exited (0) 2 days ago                       pensive_wozniak
8064f3f6680e        hello-world             "/hello"                 3 days ago          Exited (0) 3 days ago                       elegant_stonebraker
```

5. Все используемые докеры в системе
```
-bash-4.2$ docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
molecule_local/ubuntu   latest              969d783d278f        2 days ago          131 MB
molecule_local/centos   7                   7e595de0760b        2 days ago          231 MB
docker.io/centos        7                   5e35e350aded        2 weeks ago         203 MB
docker.io/ubuntu        latest              775349758637        3 weeks ago         64.2 MB
docker.io/hello-world   latest              fce289e99eb9        10 months ago       1.84 kB
```
6. Собираем образы
```
docker build -t reddit:latest .

....
---> 7d8ee5f66e40
Removing intermediate container 314b4844570a
Step 15/15 : CMD /start.sh
---> Running in 3405fec63143
---> 64cfdc12d792
Removing intermediate container 3405fec63143
Successfully built 64cfdc12d792
```
7. Смотрим образы
```
[root@jenkins docker-monolith]# docker images
REPOSITORY              TAG                 IMAGE ID            CREATED             SIZE
reddit                  latest              64cfdc12d792        2 minutes ago       958 MB
<none>                  <none>              a05eeed10b58        3 hours ago         948 MB
<none>                  <none>              48855d405ecb        3 hours ago         947 MB
<none>                  <none>              7eb05b1399d5        3 hours ago         947 MB
<none>                  <none>              4924af78e040        3 hours ago         947 MB
<none>                  <none>              488ded718b88        3 hours ago         602 MB
<none>                  <none>              58cf4ba88dc1        4 hours ago         647 MB
molecule_local/ubuntu   latest              969d783d278f        4 days ago          131 MB
docker.io/ubuntu        16.04               5f2bf26e3524        3 weeks ago         123 MB
docker.io/ubuntu        18.04               775349758637        3 weeks ago         64.2 MB
docker.io/ubuntu        latest              775349758637        3 weeks ago         64.2 MB
```    


<a name="HW16"></a>
## Примечание к ДЗ№16
1. Машина в облаки Goole  
2. Создание сети  
```
-bash-4.2$ docker network create reddit
53eaea264e25c3fe68cfe7eaece1b87efaa8cbca32c3ae794e1a02fd755a6837
```  

3. Команды по работе с контейнерами
```
docker run -d --network=reddit --network-alias=post_db --network-alias=comment_db mongo:latest
docker run -d --network=reddit --network-alias=post nvtikhomirov/post:1.0
docker run -d --network=reddit --network-alias=comment nvtikhomirov/comment:1.0
docker run -d --network=reddit -p 9292:9292 nvtikhomirov/ui:1.0
```  

4. Задания со ⭐  
Запустите контейнеры с другими сетевыми алиасами (так работать не будет)
```
docker run -d --network=reddit --network-alias=post_db_test --network-alias=comment_db_test mongo:latest
docker run -d --network=reddit --network-alias=post_test nvtikhomirov/post:1.0
docker run -d --network=reddit --network-alias=comment_test nvtikhomirov/comment:1.0
docker run -d --network=reddit -p 9292:9292 nvtikhomirov/ui:1.0
```   
Указываем через агрумент -e переменные окружения  
```
docker run -d --network=reddit --network-alias=post_db_test --network-alias=comment_db_test mongo:latest -v reddit_db:/data/db
docker run -d -e POST_DATABASE_HOST=post_db_test --network=reddit --network-alias=post_test nvtikhomirov/post:1.0
docker run -d -e COMMENT_DATABASE_HOST=comment_db_test --network=reddit --network-alias=comment_test nvtikhomirov/comment:1.0
docker run -d -e POST_SERVICE_HOST=post_test -e COMMENT_SERVICE_HOST=comment_test --network=reddit -p 9292:9292 nvtikhomirov/ui:1.0
```
```
-bash-4.2$ docker images
REPOSITORY             TAG                 IMAGE ID            CREATED             SIZE
nvtikhomirov/ui        1.1                 728dd4cf6605        9 minutes ago       458 MB
nvtikhomirov/ui        1.0                 b697c8f0d109        2 days ago          783 MB

```  
Образ на Alpine
```
bash-4.2$ docker images
REPOSITORY                     TAG                 IMAGE ID            CREATED             SIZE
nvtikhomirov/ui                1.2                 67d25e9c0ac0        11 seconds ago      77.5 MB
nvtikhomirov/ui                1.1                 728dd4cf6605        45 minutes ago      458 MB
nvtikhomirov/ui                1.0                 b697c8f0d109        2 days ago          783 MB

```  
Alpine подсказывает каких пакетов нету и какие версии нужны ЫЫ!


<a name="HW17"></a>
## Примечание к ДЗ№17   
1. Если есть старые сети с таким же наименованием - ЭТО БЕДА (сначало удаляем)
   ```
   docker network rm reddit
   ```
2. Версию docker-compose

<a name="HW18"></a>  
## Примечание к ДЗ№18

1. Все накликал мышой в морде cloud  
2. Настроил nginx как реверс прокси (использую две машинки, где ngin+realIP(otus.nt33.ru) и gitlab только локальный адрес )  
3. Зашел через otus.nt33.ru установил нужные пакеты (docker,compose и {admin_tools})  
4. Поправил в файле docker-compose.yml нужный url  (не смог разобраться почему эта зараза иногда подставляет вместо https http)
5. Так как использовал CentOS нашел приключения с selinux
6. Ошибка 502 иногда не означает что gitlab плохо, это всего может означать почитай логи и чуть-чуть подожди  

Задачи со * не выполнял.  

 
