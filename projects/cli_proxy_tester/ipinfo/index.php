<?php
    header('Content-type: application/json');

    $client_information = array(
        "ip" => $_SERVER['REMOTE_ADDR'], 
        "xff" => $_SERVER['HTTP_X_FORWARDED_FOR'],
        "useragent" => $_SERVER['HTTP_USER_AGENT']
    );

    echo json_encode($client_information);
?>