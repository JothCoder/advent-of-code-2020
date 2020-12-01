#!/bin/sh

if . "./.env"
then
    echo "Loading .env";
else
    echo "Can't load .env"
    echo "\e[1;31mERROR\e[0m"
    exit 1
fi

if [ -z "${AOC_SESSION}" ]
then
    echo "Environment variable 'AOC_SESSION' has length zero"
    echo "\e[1;31mERROR\e[0m"
    exit 2
fi

if [ -z "${AOC_YEAR}" ]
then
    echo "Environment variable 'AOC_YEAR' has length zero"
    echo "\e[1;31mERROR\e[0m"
    exit 3
fi

day=$1

if [ -z "$day" ]
then
    echo "No day given (usage: ./aoc <day>)"
    echo "\e[1;31mERROR\e[0m"
    exit 4
fi

if [ "${day}" -ge 25 ] || [ "${day}" -lt 1 ]
then
    echo "The given day must be between 1 and 25"
    echo "\e[1;31mERROR\e[0m"
    exit 5
fi

day_fmtd=$(printf "%02d" "$day")

echo "Retrieving input of \e[1mAdvent of Code ${AOC_YEAR}, day ${day}\e[0m"
echo "Requesting https://adventofcode.com/${AOC_YEAR}/day/${day}/input"
echo "Writing input to 'input/day${day_fmtd}.txt'"

if (curl -b session="${AOC_SESSION}" "https://adventofcode.com/${AOC_YEAR}/day/${day}/input") 2> "/dev/null" > "input/day${day_fmtd}.txt"
then
    echo "\e[1;32mCOMPLETED\e[0m"
    exit 0
else
    echo "\e[1;31mERROR\e[0m"
    exit 6
fi