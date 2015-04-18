<?php
	$arr = array('Hello','World!','Beautiful','Day!');
	echo implode(" ",$arr);
	echo "\n";
	$input = "AB  B C   D";
	$words = preg_split('/\s+/', $input);
	array_shift($words);
	 var_dump($words);
		echo "\n";

?>