<?php

include_once("")


$nome = filter_input(INPUT_POST, 'nome', FILTER_SANITIZE_STRING);
$email = filter_input(INPUT_POST, 'email', FILTER_SANITIZE_EMAIL);

//echo "nome, $nome <br>";
//echo "E-mail, $email <br>";