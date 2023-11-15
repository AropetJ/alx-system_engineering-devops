# fix our stack so that we get to 0 requests failed

exec {'set a file limit for Nginx by modifying the configuration file':
  onlyif  => 'test -f /etc/default/nginx',
  command => 'sed -i "s/15/2000/g" /etc/default/nginx',
  path    => '/bin/:/sbin/:/usr/bin/:/usr/sbin/'
}
