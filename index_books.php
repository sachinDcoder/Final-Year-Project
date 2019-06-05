<?php
	$command = escapeshellcmd('C:\Users\hp\Anaconda3\python python/knn.py');
	$output = shell_exec($command);
	//echo "hey";
	//echo $output;
?> 


<?php
	session_start();

	if (!isset($_SESSION['access_token'])) {
		header('Location: login.php');
		exit();
	}
?>


<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>User Profile</title>
	<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta/css/bootstrap.min.css" integrity="sha384-/Y6pD6FV/Vv2HJnA6t+vslU6fwYXjCFtcEpHbNJ0lyAFsXTsjBbfaDjzALeQsN6M" crossorigin="anonymous">
	<link rel="stylesheet" href="style.css">
</head>
<body>
	<header class="text-right fixed">
		<nav>
			<ul>
				
				<li><a href="index.php">Movies</a></li>
				<li><a href="index_books.php">Books</a></li>
				<li><a href="about.php">About</a></li>
				<li class="logout"><a href="logout.php">Logout</a></li>
				<li class="logo"><img style="height:60px; width:60px" src="<?php echo $_SESSION['userData']['picture']['url'] ?>"  size=20px></li>
			</ul>
			
		</nav>
		
	</header>
	<div class="container" style="margin-top: 100px">
		<div class="row text-center">
			<div class="col mb-5">
				<h1>Recommender System</h1>
			</div>
		</div>
		<!-- <div class="row">
			<div class="col text-right">
				<a href="logout.php">Logout</a>
			</div>
		</div> -->
		<!-- <div class="row justify-content-center">
			<div class="col-md-3">
				<img src="<?php echo $_SESSION['userData']['picture']['url'] ?>">
			</div>
		
			<div class="col-md-9">
				<table class="table table-hover table-bordered">
					<tbody>
						<tr>
							<td>ID</td>
							<td><?php echo $_SESSION['userData']['id'] ?></td>
						</tr>
						<tr>
							<td>First Name</td>
							<td><?php echo $_SESSION['userData']['first_name'] ?></td>
						</tr>
						<tr>
							<td>Last Name</td>
							<td><?php echo $_SESSION['userData']['last_name'] ?></td>
						</tr>
						<tr>
							<td>Email</td>
							<td><?php echo $_SESSION['userData']['email'] ?></td>
						</tr>
					</tbody>
				</table>
			</div>
		</div> -->
		
		<div class="row" style="margin-top: 40px">
			<div class="col-7">
				<h2>Personalized only for you!(Recommendations)</h2>
			</div>
			<!-- <div class="col-5 text-right">
				<a href="index.php">Click Here to get recommended movies</a>
			</div> -->
		</div>
		<div class="row" style="margin-top: 40px">
			<?php
				$command = escapeshellcmd('python python/req_books_poster.py');
				$output = shell_exec($command);
				echo $output;
			?>
		</div>

	</div>
</body>
</html>
