<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Log In</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
</head>
<body>

	<div class="container" style="margin-top: 100px">
		<div class="row justify-content-center">
			<div class="col-md-6 col-md-offset-3" align="center">
				<img src="images/logo.png" width="200" height="200"><br><br>
				<form action="reg.php" method="post">
					<input type="text" name="name" placeholder="Name" required class="form-control"><br>
					<input type="text" name="email" placeholder="Email" required class="form-control"><br>
					<input name="password" type="password" placeholder="Password" required class="form-control"><br>
					<input name="confirm_password" type="password" placeholder="Re-Enter Password" required class="form-control"><br>
					<input name="age" placeholder="Age" required class="form-control"><br>
					
					<input type="submit" value="Sign Up" class="btn btn-primary">
					
				</form>
			</div>
		</div>
	</div>

</body>
</html>

