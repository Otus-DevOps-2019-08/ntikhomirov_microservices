##### Содержание
[Домашня работа №15](#HW15)    

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
