# Define the input file with gene partitions
input_partition_file = "partitions.txt"  # Replace with your file name

# Define the output Nexus file
output_nexus_file = "partitions_cp.nex"  # Replace with your desired output file name

# Open the output Nexus file for writing
with open(output_nexus_file, "w") as nexus_file:
    nexus_file.write("#nexus\n")
    nexus_file.write("begin sets;\n")

    # Read the input partition file
    with open(input_partition_file, "r") as partition_file:
        for line in partition_file:
            line = line.strip()
            if not line:
                continue  # Skip empty lines

            # Split the line into partition name and positions
            partition_name, positions = map(str.strip, line.split("="))
            positions = positions.split("-")

            # Replace hyphens with underscores in the partition name
            partition_name = partition_name.replace("-", "_")

            # Create separate partitions for each codon position
            for i, codon_position in enumerate(["1st", "2nd", "3rd"]):
                start = int(positions[0]) + i
                end = int(positions[1])
                charset_name = f"{partition_name}_{codon_position}"
                partition_line = f"charset {charset_name} = {start}-{end}\\3;\n"
                nexus_file.write(partition_line)

    nexus_file.write("end;\n")

print(f"Converted partitions to Nexus format and saved to '{output_nexus_file}'.")
