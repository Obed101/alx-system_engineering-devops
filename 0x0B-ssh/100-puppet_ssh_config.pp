# This code runs an ssh command
include stdlib

file_line { 'creating the config':
ensure       => 'present',
line         => 'PasswordAuthentication no',
path         => '/etc/ssh/ssh_config',
line         => 'IdentityFile ~/.ssh/school'
}

file_line { 'The identity file':
ensure => 'present',
path   => '/etc/ssh/ssh_config',
line   => 'IdentityFile ~/.ssh/school'
}
