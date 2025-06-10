<?php 

$host = 'localhost';
$usuario = 'root';
$senha = '';
$banco = 'cadastro_clientes';

$conn = new mysqli($host, $usuario, $senha, $banco);
if ($conn -> connect_error){
    die ("conexao falhou: " . $conn -> connect_error);
}

?>
