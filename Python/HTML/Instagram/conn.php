<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>Connessione al db</title>
</head>

<body>
<?php
   //Includo lo script per fixare l'erroe 
   include_once('mysql-fix.php'); 

   //Credenziali
   $db_host = "2.235.240.156";
   $db_user = "root";
   $db_psw = "Riccardo05";
   $db_name = "Instagram"; 

   $link = mysql_connect($db_host, $db_user, $db_psw);
   if (!$link) {
      die("<p>Non riesco a connettermi al server database per colpa di:".mysql_error()."</p>");
   }
   //Mi sono connesso al database e ho preso l'identificatore di connessione chiamato $link
   $db_select = @mysql_select_db($db_name, $link);
   if (!$db_select) {
      die("<p>Nn riesco a connettermi al database per colpa di:.mysql_error()</p>");
   }
   //Ho selezionato il db dove andro' a lavorare
   echo "<p>*</p>";
?>
</body>
</html>

