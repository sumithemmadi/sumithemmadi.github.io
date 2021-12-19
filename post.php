<?php
header('Location: /#contact');

$myfile = fopen("log.txt","a");

foreach($_POST as $variable => $value){
    fwrite($myfile,$variable);
    fwrite($myfile,"=");
    fwrite($myfile,$value);
    fwrite($myfile,"\r\n");
}

fwrite($myfile,"\r\n");
fclose($myfile);

?>

