#!/usr/local/bin/perl
##
## Start setting up options here:

## Your path to where you want your files uploaded.
## Note: NO trailing slash
$basedir = "/u/web/cometd/Xfer/tid2";

## Do you wish to allow all file types?  yes/no (no capital letters)
$allowall = "no";

## If the above = "no"; then which is the only extention to allow?
## Remember to have the LAST 4 characters i.e. .ext
$theext = ".zip";

## The page you wish it to forward to when done:
## I.E. http://www.mydomainname.com/thankyou.html
$donepage = "http://www.cometdesign.com/Xfer/tid2";



################################################
################################################
## DO NOT EDIT OR COPY BELOW THIS LINE        ##
################################################
################################################

use CGI; 
$onnum = 1;

while ($onnum != 11) {
my $req = new CGI; 
my $file = $req->param("FILE$onnum"); 
if ($file ne "") {
my $fileName = $file; 
$fileName =~ s!^.*(\\|\/)!!; 
$newmain = $fileName;
if ($allowall ne "yes") {
if (lc(substr($newmain,length($newmain) - 4,4)) ne $theext){
$filenotgood = "yes";
}
}
if ($filenotgood ne "yes") { 
open (OUTFILE, ">$basedir/$fileName"); 
print "$basedir/$fileName<br>";
while (my $bytesread = read($file, my $buffer, 1024)) { 
print OUTFILE $buffer; 
} 
close (OUTFILE); 
}
}
$onnum++;
}

print "Content-type: text/html\n";
print "Location:$donepage\n\n";
