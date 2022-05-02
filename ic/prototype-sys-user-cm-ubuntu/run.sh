groupadd -g 1111 ckuser
useradd -u 2222 -g ckuser --create-home --shell /bin/bash ckuser
echo "ckuser:ckuser" | chpasswd
adduser ckuser sudo
echo "ckuser   ALL=(ALL)  NOPASSWD:ALL" >> /etc/sudoers
