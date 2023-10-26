import sys

if len(sys.argv) != 6:  
	print("Usage: python3 xyzshift.py input.xyz output.xyz dx dy dz")
	sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]
dx = float(sys.argv[3])
dy = float(sys.argv[4])
dz = float(sys.argv[5])

# Read the file and convert each line into correct format
formatted_lines = []
with open(input_file, "r") as file:
	lines = file.readlines()

num_atoms = int(lines[0])
formatted_lines.append(str(num_atoms)+"\n") 
formatted_lines.append("Generated by xyzshift.py \n") 

for line in lines[2:]:
	parts = line.split()
	if len(parts) == 4:
		symbol, x, y, z = parts
  		x = float(x) + dx
  		y = float(y) + dy
    	z = float(z) + dz
    	formatted_line = f"{symbol}   {x:.6f}   {y:.6f}   {z:.6f}\n"
    	formatted_lines.append(formatted_line)

with open(output_file, "w") as file:
	file.writelines(formatted_lines)
