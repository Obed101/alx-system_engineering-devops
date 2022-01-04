# This code runs an ssh command

file_line { 'creating the config':
ensure       => 'present',
line         => 'PasswordAuthentication no',
path         => '~/.ssh/config',
line         => 'IdentityFile ~/.ssh/school'
}
