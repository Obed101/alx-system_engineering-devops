# This code kills the killmenow process

exec { 'killmenow':
command	=> 'pkill -15 killenow',
provider => 'shell'
}
