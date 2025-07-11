#/!bin!bash

for i in Mg O;
do
	for j in x y z;
	do
		mkdir replaced_${i}_${j}
		#cp jobscript POSCAR INCAR KPOINTS POTCAR replaced_${i}_${j}
		cd replaced_${i}_${j}
		#I adapted this later by hand! need to replace each position once
		echo '2.1060 2.1060 2.1060' >> POSCAR
		echo '0.0000 0.0000 0.0000' >> POSCAR
		#send to cluster
		sbatch jobscript
		cd ../
	done
done



