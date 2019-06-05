<?php
	require_once "config.php";

	if (isset($_SESSION['access_token']))
	{
		header('Location: index.php');
		exit();
	}

	$redirectURL = "http://localhost/final/fb-callback.php";
	$permissions = ['email','user_birthday','user_likes','user_posts','user_gender','user_location'];
	$loginURL = $helper->getLoginUrl($redirectURL, $permissions);
?>
<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Log In</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
	<link rel="stylesheet" href="style.css">
</head>
<body>

	<div class="container" style="margin-top: 100px">
		<div class="row justify-content-center">
			<div class="col-md-6" align="center">
				<h1 style="font-size: 100px; margin-top:100px">Recommender System</h1>
			</div>
			<div class="col-md-1" align="center">
			</div>
			<div class="col-md-5" align="center">
				<form action="validate_login.php" method="post">
					<!-- <input name="email" placeholder="Email" required class="form-control"><br>
					<input name="password" type="password" required placeholder="Password" class="form-control"><br>
					<input type="submit" value="Log In" class="btn btn-primary"> -->
					<input type="button" style="font-size: 30px; margin-top:170px" onclick="window.location = '<?php echo $loginURL ?>';" value="Log In With Facebook" class="btn btn-primary">
				</form>
			</div>
		</div>
	</div>

</body>
</html>

