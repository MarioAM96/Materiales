<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nombre = $_POST["nombre"];

    // Ejecutar el script de Python con los datos del formulario como argumentos
    $comando = escapeshellcmd('python3 app.py ' . escapeshellarg($nombre) . ' ' . escapeshellarg($lugar) . ' ' . escapeshellarg($tiempo));
    
    // Ejecutar el comando y capturar la salida (opcional)
    $output = shell_exec($comando);
    
    // Imprimir la salida del script de Python (si deseas mostrar algo)
    echo "<pre>$output</pre>";
}
?>
