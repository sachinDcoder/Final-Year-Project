<?php
	//echo "Helo";

	require_once "config.php";

	try {
		$accessToken = $helper->getAccessToken();
		echo $accessToken;
	} catch (\Facebook\Exceptions\FacebookResponseException $e) {
		echo "Response Exception: " . $e->getMessage();
		exit();
	} catch (\Facebook\Exceptions\FacebookSDKException $e) {
		echo "SDK Exception: " . $e->getMessage();
		exit();
	}

	if (!$accessToken) {
		header('Location: login.php');
		exit();
	}

	$oAuth2Client = $FB->getOAuth2Client();
	if (!$accessToken->isLongLived())
	{
		$accessToken = $oAuth2Client->getLongLivedAccessToken($accessToken);
		$file = fopen("access_token.txt","w");
		fwrite($file, $accessToken);
		fclose($file);
	}

	$file = fopen("access_token.txt","w");
	fwrite($file, $accessToken);
	fclose($file);
		
	$response = $FB->get("/me?fields=id, first_name, last_name, email, picture.type(large), birthday, gender, location", $accessToken);
	$userData = $response->getGraphNode()->asArray();
	echo '<pre>'; print_r($userData); echo '</pre>';
	$_SESSION['userData'] = $userData;
	$node = $response->getGraphNode();
	echo '<pre>'; print_r($userData['birthday']); echo '</pre>';
	$fbirthday = $node->getField('birthday');
	//var_dump($fbirthday);
	$_SESSION['access_token'] = (string) $accessToken;
	header('Location: index.php');
	exit();
	
?>

