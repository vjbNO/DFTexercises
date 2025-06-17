#/!bin!bash

for i in {0..10..1}
do
	grep "band     $i" PROCAR >> energies_band$i
done


