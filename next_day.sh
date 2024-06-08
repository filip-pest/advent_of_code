#! /bin/bash

get_file_extension () {
	case "$language" in
		"python") 
			echo ".py"
		;;
		*) 
			echo "0"
		;;
	esac
}

get_next_day () {
	local directories=($(ls))
	local next_day_number=1
	for directory in ${directories[@]}; do
		if [[ "${directory}" == *"day"* ]]; then
			if [[ "${directory}" == *${next_day_number}* ]]; then
				next_day_number=$((next_day_number+1))
			fi
		fi
	done
	if [ ${next_day_number} -gt 10 ]; then
		echo "${next_day_number}"
	else
		echo "0${next_day_number}"
	fi
}

create_files () {
	touch "day${day_number}-1${extension}"
	touch "day${day_number}-2${extension}"
	touch "test-input.txt"
	touch "input.txt"
}


language=$1
year=$2
extension=`get_file_extension`
if [ ${extension} == 0 ]; then
	echo "${language} <-- Language is not supported yet!"
	exit
fi
cd $year
day_number=`get_next_day`
mkdir day${day_number}
cd day${day_number}
create_files
