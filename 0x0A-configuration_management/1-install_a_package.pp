# Installing flask using puppet

package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_flask':
  command => 'pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/usr/local/bin'],
  unless  => 'pip3 show flask | grep Version | grep -q 2.1.0',
  require => Package['python3-pip'],
}

