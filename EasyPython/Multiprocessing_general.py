def test_gevent():
    import gevent
    hosts = ['www.crappytaxidermy.com', 'www.walterpottertaxidermy.com',
             'www.antique-taxidermy.com']
    jobs = [gevent.spawn(gevent.socket.gethostbyname, host) for host in hosts]
    _ = gevent.joinall(jobs, timeout=5)
    for job in jobs:
        print(job.value)


if __name__ == '__main__':

    test_gevent()
