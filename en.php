<?php

print "\n";
print " 01) Encode Md4\n";
print " 02) Encode Md5\n";
print " 03) Encode Sha1\n";
print " 04) Encode Base64\n";
print " 05) Encode All Type\n\n";
echo " Menu : ";
$input = trim(fgets(STDIN));
if ($input == '01' OR $input == '1'){
    echo " Input String : ";
    $base = trim(fgets(STDIN));
    echo " Encode Md4 : ",crypt('md4',$base);
    print "\n\n";
}
elseif ($input == '02' OR $input == '2'){
    echo " Input String : ";
    $base = trim(fgets(STDIN,256));
    echo " Encode Md5 : ",md5($base);
    print "\n\n";
}
elseif ($input == '03' OR $input == '3'){
    echo " Input String : ";
    $base = trim(fgets(STDIN));
    echo " Encode Sha1 : ",sha1($base);
    print "\n\n";
}
elseif ($input == '04' OR $input == '4'){
    echo " Input String : ";
    $base = trim(fgets(STDIN));
    echo " Encode Md5 : ",base64_encode($base);
    print "\n\n";
}
elseif ($input == '05' OR $input == '5'){
    echo " Input String : ";
    $base = trim(fgets(STDIN));
    print " █ Length █████ Type █████████████ Encode █████████████\n";
    foreach (hash_algos() as $v){
        $r = hash($v, $base, false);
        printf("    %3d         %-12s       %s\n\n", strlen($r), $v, $r);
    }
    print "\n\n";
}

?>