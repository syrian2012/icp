icp - Fastest way to copy files/directories over the internet based on SSH.

how it works

This package copies files over network and internet by compression data from the sender and decompression it by the receiver.
In this way you achieve two benefits: faster and save traffic bandwidth
test it on a huge amount of data it will be save 30 to 70 percent based on data type.

Usage: icp -p port -c cores source_directory destination_server destination_directory

source_directory: The directory on the local machine to copy. destination_server: The server to copy the files to. destination_directory: The directory on the destination server to copy the files to. -p (optional): The SSH port to use. Defaults to 22 if not provided. -c (optional): The number of cores to use. Defaults to 4 if not provided. NOTE: 'cores' should be the lower number of cores available between the source and destination server.

Example: icp -p 22 -c 4 /home/user/mydir example.com /var/www/mydir

enjoy with Love Mohammad Haidar
