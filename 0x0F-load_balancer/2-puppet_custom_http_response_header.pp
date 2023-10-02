# Update system
exec { 'update_system':
  command     => '/usr/bin/apt-get update',
  refreshonly => true,
}

# Install Nginx and set up the custom HTTP header
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update_system'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx settings using a file resource
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
}

# Use Exec to append custom HTTP header
exec { 'add_custom_header':
  command => 'echo "    add_header X-Served-By $hostname;" >> /etc/nginx/sites-available/default',
  unless  => 'grep -q "X-Served-By \$hostname;" /etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enable it
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  require   => Package['nginx'],
  subscribe => [File['/etc/nginx/sites-available/default'], Exec['add_custom_header']],
}
