#/!bin!bash

for i in {4..16};
do
	mkdir testKdens_$i
	cp jobscript POSCAR INCAR KPOINTS POTCAR testKdens_$i
	cd testKdens_$i
	echo $i' '$i' '$i >> KPOINTS
	echo '0 0 0' >> KPOINTS
	#send to cluster
	sbatch jobscript
	cd ../
done

