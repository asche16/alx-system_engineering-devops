#This script increases number of worker_processes
exec { 'increase nginx worker processes':
  command => "sed -i '$ i/* soft    nofile  1000' /etc/security/limits.conf;
sed -i '$ i/* hard    nofile  100000' /etc/security/limits.conf;",
  path    => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin'
  }
