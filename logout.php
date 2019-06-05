<?php
	session_start();
	
	unset($_SESSION['userData']);
	unset($_SESSION['access_token']);

	session_unset();
	session_destroy();

	header('Location: login.php');
?>