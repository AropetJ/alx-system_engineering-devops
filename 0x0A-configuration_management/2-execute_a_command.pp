# A puppet manifest that kills a process named killmenow.

exec { 'killmenow':
  command     => 'pkill -f "killmenow"',
  path        => '/usr/bin:/usr/sbin:/bin:/sbin',
  refreshonly => true,
}

# Notify['process_killed'] -> Exec['your_command_here'
notify { 'process_killed':
  message => 'The "killmenow" process has been terminated.',
  before  => Exec['your_command_here'],
}

