# Update system
exec { 'update system':
        command => '/usr/bin/apt-get update',
}

# Install Nginx and set up the custom HTTP header
package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

# Configure Nginx settings using a file resource
exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Use Exec to append custom HTTP header
exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

# Ensure Nginx service is running and enable it
service {'nginx':
	ensure => running,
	require => Package['nginx']
}
