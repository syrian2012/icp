# icp
icp (internet copy) - Fastest way to copy files/directories over the internet based on SSH.

# how it works
simply edit your .bashrc file inside your home directory and copy content of code to add in .bashrc file inside it or simply run the follwing it will do the job for you:<br>
cat code_in_bashrc >> ~/.bashrc

to take function you need to logout and login again or start a new shell

her what should it function

Usage: icp -p port -c cores source_directory destination_server destination_directory

source_directory: The directory on the local machine to copy.
destination_server: The server to copy the files to.
destination_directory: The directory on the destination server to copy the files to.
-p (optional): The SSH port to use. Defaults to 22 if not provided.
-c (optional): The number of cores to use. Defaults to 4 if not provided.
NOTE: 'cores' should be the lower number of cores available between the source and destination server.

Example: icp -p 22 -c 4 /home/user/mydir example.com /var/www/mydir

after that logout and login again to your shell and the icp will be functional

enjoy
