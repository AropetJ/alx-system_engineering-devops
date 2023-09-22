# A puppet manifest that kills a process named killmenow.

exec { 'killmenow':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
}

# Suppress the "executed successfully" notice
notify { 'process_killed':
  message => 'The process killmenow has been terminated.',
  before  => Exec['your_command_here'],
}

# Ensure that Puppet displays only the "Finished catalog run" notice
notify { 'finished_run':
  message   => 'Finished catalog run',
  subscribe => Exec['killmenow'],
}

