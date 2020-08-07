<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
<title>ADD</title>
</head>

<body>
<?php
   include_once('mysql-fix.php');
   include_once('conn.php');

   $User = $_POST['Name'];
   $Password = $_POST['Code'];

   $query = "INSERT INTO Product (Name, Code) VALUES ('$User', '$Password');";
   $result = mysql_query($query);
   if (!$result) {
      die("<p>Errore nella query: ".mysql_error()."</p>");
   }
        mysql_close();
   echo "<p>{PASSWORD ERRATA}</p>";
?>
</body>
</html>
