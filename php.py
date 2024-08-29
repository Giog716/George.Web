<!-- contact-form.php -->

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $nume = htmlspecialchars($_POST['nume']);
    $email = htmlspecialchars($_POST['email']);
    $mesaj = htmlspecialchars($_POST['mesaj']);

    $to = "your-email@example.com"; // Înlocuiește cu adresa ta de email
    $subject = "Mesaj de la $nume";
    $body = "Nume: $nume\nEmail: $email\nMesaj:\n$mesaj";
    $headers = "From: $email";

    if (mail($to, $subject, $body, $headers)) {
        echo "Mesaj trimis cu succes!";
    } else {
        echo "Eroare la trimiterea mesajului. Te rugăm să încerci din nou.";
    }
}
?>
