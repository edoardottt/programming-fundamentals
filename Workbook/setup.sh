echo "Workbook setup..."


for pyfile in $(ls utils)
do
	echo $pyfile
    find . -type d -maxdepth 2 -exec cp $pyfile {}\;
done

echo "Done!"