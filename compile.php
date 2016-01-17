<?php 

$fileName = './v.1';

$lines = file($fileName);

$newDef = false;

foreach ($lines as $line) {
	$line2 = trim($line);

    
	if(!isset($line2[0])){
		continue;
	}
	
	switch ($line2[0]) {
		case '#':
			$newDef = false;
			print "\t\"\"\"\n\tpass\n";
			print "\n$line\n";
			break;
		case '|':
			print "    $line";
			break;
		default:
			if ($newDef) {
				print "    \"\"\"\n    pass\n";
			}
			$newDef = true;
			$def =  trim(explode(':', $line)[0]);
			print "\ndef p_{$def}(p):\n    \"\"\"\n    {$line}";
			break;
	}

}

print "    \"\"\"\n    pass\n";
