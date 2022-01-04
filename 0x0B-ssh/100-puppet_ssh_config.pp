# This code runs an ssh command
include stdlib

file_line { 'creating the config':
ensure       => 'present',
line         => 'PasswordAuthentication no',
path         => '~/.ssh/config',
line         => 'IdentityFile ~/.ssh/school'
}
