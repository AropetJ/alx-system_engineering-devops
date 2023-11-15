# Uses strace to find out why Apache is returning a 500 error

exec {'fixes 500 error':
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
  provider => shell
}
