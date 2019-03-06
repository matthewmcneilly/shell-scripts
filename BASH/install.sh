# install of program from a list (text file)
# does package name matter across distro 
# what if package name is different 
# what if package name not found 
# if this is a concern have different text files 
    # log as it goes 
    # when complete log
    # if error log 
# what if the program is already installed 

# CHECK WHAT DISTRO is used 
# If distro is Redhat (Fedora, Centos, RHEL)
if [ -f /etc/redhat-release ] ; then
echo "Distro if Rehat"
distro="Redhat"
pkgmngr="yum"
# If distro is Debian (Ubuntu, Mint, Debian)
elif [ -f /etc/debian_version ] ; then
echo "Distro is Debian"
distro="Debian"
pkgmngr="apt"
# If distro not found 
else 
echo "Distro not recognised"
distro="Unknown"
fi

# Print out current distro 
echo $distro
# Print out package manager 
echo $pkgmngr

# Read in each line of programs text file 
textfile="programs.txt"
while IFS= read -r var
do
  echo "$var"
done < "$textfile"









