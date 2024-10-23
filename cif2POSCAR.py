# to run: python3 cif2POSCAR.py
from pymatgen.core import Structure

my_struc = Structure.from_file(input("name of file (ie ./input_geometry.cif): "))

# make an nxnxn supercell
n = int(input("size n of supercell for nxnxn: ")) # get desired (cubic) dimension as int
my_struc.make_supercell(n)

# write supercell to POSCAR format with specified filename
my_struc.to(fmt="poscar", filename=input("name of dump file (ie ./POSCAR or /home/output_POSCAR): ")) # dumps to same dir as file