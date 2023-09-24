# A resource type to manage SSH client configuration
define ssh_config {
    file_line { "ssh_config_$title":
        path   => '/etc/ssh/ssh_config',  # Path to the SSH client config file
        line   => $value,
        match  => "^$title\\s",
        ensure => present,
  }
}

# Configure SSH to use the private key and refuse password authentication
ssh_config { 'IdentityFile':
  value => 'IdentityFile ~/.ssh/school',
}

ssh_config { 'PasswordAuthentication':
  value => 'PasswordAuthentication no',
}

