"""
sudo code

for this exercise pleae bare in mind that I do not have a linux machine
I am using my apple. so the following will apply to a unix system which
could be different from linux

read the user input and determine what is being passed.
    use an if then elif to determine what is passing with a final elif to
    throw an error if he is not passing the right type and number of parameter

if he is not passing the -h option and not using a path then
    use the python os utility to do
    cd ~           cd to the home directory
    df > outfile   execute a diff and direct the output to file
    use re.search  on outfile to replace the spaces between the colum with a column :
    use cut -d: -f 2-4   this will give you the three column you need.
    writhe the output to standout


if he is passing the -h option and not using a path then
    use python os utility to do
    cd ~                cd to the home directory
    df h > outfile      execute a diff and direct the output to file
    use re.search       on outfile to replace the spaces between the colum with a column :
    use cut -d: -f 2-4  this will give you the three column you need.
    writhe the output to standout

if he is not passing the -h option and is using a path then
    use python os utility to do read the path into a variable call it path_var
    cd path_var          cd to the path_var directory
    df > outfile         execute a diff and direct the output to file
    use re.search        on outfile to replace the spaces between the colum with a column :
    use cut -d: -f 2-4   this will give you the three column you need.
    writhe the output to standout

if he is passing the -h option and is using a path then
    use python os utility to do read the path into a variable call it path_var
    cd path_var          cd to the path_var directory
    df -h > outfile      execute a diff and direct the output to file
    use re.search        on outfile to replace the spaces between the colum with a column :
    use cut -d: -f 2-4   this will give you the three column you need.
    writhe the output to standout

"""