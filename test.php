
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<h1>hello babe</h1>
	<?php
		$command = escapeshellcmd('python python/req_movies_poster.py');
		$output = shell_exec($command);
		echo $output;
	?>
</body>
</html>
