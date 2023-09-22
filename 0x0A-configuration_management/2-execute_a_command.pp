# A puppet manifest that kills a process named killmenow.
exec { 'pkill killmenow':
  path => '/usr/sbin:/usr/bin:/bin'
}

