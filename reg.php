<?php
	$connection = mysqli_connect("localhost", "root", ""); 
	$db = mysqli_select_db("user_db", $connection); 
	if(isset($_POST['submit']))
	{ 
		$name = $_POST['name'];
		$email = $_POST['email'];
		$age = $_POST['age'];
		$password = $_POST['password'];
		if($name !='' || $email !='')
		{
			$query = mysqli_query("insert into user(name, email, password, age) values ('$name', '$email', '$password', '$age')");
			echo "<br/><br/><span>Data Inserted successfully...!!</span>";
		}
		else
		{
			echo "<p>Insertion Failed <br/> Some Fields are Blank....!!</p>";
		}
	}
	mysqli_close($connection); 
?>