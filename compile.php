<?php 

$fileName = './rules.y';

$lines = file($fileName);

$newDef = false;

foreach ($lines as $line) {
	$line = trim($line);

	if(!isset($line[0])){
		continue;
	}
	
	switch ($line[0]) {
		case '#':
			$newDef = false;
			print "\t\"\"\"\n\tpass\n";
			print "\n######################################\n$line\n###\n";
			break;
		case '|':
			print "\t\t$line\n";
			break;
		default:
			if ($newDef) {
				print "\t\"\"\"\n\tpass\n";
			}
			$newDef = true;
			$def =  trim(explode(':', $line)[0]);
			print "\ndef p_{$def}(p):\n\t\"\"\"\n\t{$line}\n";
			break;
	}

}

print "\t\"\"\"\n\tpass\n";