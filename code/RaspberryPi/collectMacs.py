with open('/home/pi/Desktop/mac.txt') as f:
	word= f.read().split()
	for x in word:
		if len(x) == 17:
			j = open('/var/www/html/index.php', 'a+')
			print(j.readlines())
			if not x in j:
				j.write('<?php echo'+ "'"+ x + " ' "+ '; ?>')
			j.close()