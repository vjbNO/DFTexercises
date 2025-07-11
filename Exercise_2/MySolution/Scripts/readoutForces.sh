#/!bin!bash

for i in Mg O;
do
	for j in x y z;
	do
		cd replaced_${i}_${j}
		#extract energy and copy into new file
		grep -A 3 "TOTAL-FORCE" OUTCAR | grep -v "TOTAL-FORCE" >> ../Forces 
		cd ../
	done
done

