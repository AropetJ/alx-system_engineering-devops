# A puppet manifest to deny password authentication

include stdlib

file_line { "Remove password authenticatin":
  ensure => present,
  path   => "/etc/ssh/ssh_config",
  line   => "PasswordAuthentication no",
}

file_line { "Copy private key from":
  ensure => present,
  path   => "/etc/ssh/ssh_config",
  line   => "IdentityFile ~/.ssh/school"
}
