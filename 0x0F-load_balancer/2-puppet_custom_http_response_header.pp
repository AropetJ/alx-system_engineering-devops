# Update system
exec { 'update_system':
  command => '/usr/bin/apt-get update',
  refreshonly => true,
}

# Install Nginx
package { 'nginx':
  ensure => 'installed',
  require => Exec['update_system'],
}

# Define the content for the default HTML file
file { '/var/www/html/index.html':
  content => 'Hello World!',
  require => Package['nginx'],
}

# Configure Nginx settings
file { '/etc/nginx/sites-available/default':
  ensure  => 'file',
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Define custom Nginx header using Augeas
augeas { 'nginx_custom_header':
  context => '/files/etc/nginx/sites-available/default/http/server',
  changes => [
    'set add_header[last()+1] X-Served-By $hostname',
    'save',
  ],
  require => File['/etc/nginx/sites-available/default'],
  notify  => Service['nginx'],
}

# Ensure Nginx service is running and enable it
service { 'nginx':
  ensure    => 'running',
  enable    => true,
  subscribe => File['/etc/nginx/sites-available/default'],
}
