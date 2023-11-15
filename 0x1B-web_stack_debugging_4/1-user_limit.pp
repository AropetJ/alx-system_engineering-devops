# Changes the OS configuration so that it is possible to login with the holberton
# user and open a file without any error message.

exec { '1-replace':
  command  => 'sudo sed -i \'s/nofile 5/nofile 30000/\' /etc/security/limits.conf',
  provider => shell,
}
exec { '2-replace':
  command  => 'sudo sed -i \'s/nofile 4/nofile 10000/\' /etc/security/limits.conf',
  provider => shell,
}
