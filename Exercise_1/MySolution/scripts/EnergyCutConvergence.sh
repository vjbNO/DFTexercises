#/!bin!bash

for i in {1..8};
do
	mkdir testEnConv_$i
	cp jobscript POSCAR INCAR KPOINTS POTCAR testEnConv_$i
	cd testEnConv_$i
	#write new energy cut into INCAR file
	echo 'ENCUT='$((300+i*50)) >> INCAR
	#send to cluster
	sbatch jobscript
	cd ../
done

