<?php
    $data =  ' Aleksandra Rewersa';
    $data2 =  ' Aleksandra Rewers';
    echo hash('md5', $data);
    echo '
';
    echo hash('sha256', $data2);
    echo '
';
    echo hash('haval255,5', $data2);

?>
