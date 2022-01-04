# This code runs an ssh command

file { '~/.ssh/config':
ensure => 'present',
PasswordAuthentication => 'no',
IdentityFile => '~/.ssh/school'
}
