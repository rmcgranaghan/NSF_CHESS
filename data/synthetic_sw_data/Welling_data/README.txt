These files are the input files and output files for the extreme sudden
storm commencement simulations using the Space Weather Modeling Framework.

MODEL AND INPUT FILES:

The SWMF may be obtained from the Center for Space Environment Modeling:
http://csem.engin.umich.edu/tools/swmf/
The SWMF comes with thorough documentation describing installation, execution,
and every input parameter available.

Run parameters are provided in the PARAM.* files.  The file PARAM.in_init is
used to initialize the code and run the preconditioning phase (first 5:45:00
of the simulation.)  The file PARAM.in_restart begins the simulation of the
storm sudden impulse and activates high time resolution output.

The solar input files are given as simple ASCII files named imf_extreme_*.dat.
The format and variable names of these files can be found in the SWMF user
manual.

RESULTS:
Output files may be visualized and examined using either the IDL package
provided alongside the SWMF or using the Spacepy python software package.
Spacepy is freely available at https://github.com/spacepy/spacepy

There are two sets of results: one for the northward IMF shock (bzN_*) and one
for the southward IMF shock (bzS_*).  Files are stored in tarballs which can
be unpacked using the tar command, e.g., 

> tar -xzvf bzN_mhd_slices.tgz

The contained files use either simple ascii formatting or SWMF-formatted binary.
The binary files will require one of the two libraries above for reading.
There are three types of output files:

Ionosphere files (ionosphere.tgz) contains ionospheric electrodynamic
information such as currents and conductances.

Magnetometer grid files (magnetometers.tgz) contain second-resolution
virtual magnetometer data across the northern hemisphere.  Each file contains
one epoch; time is given in the file name.  The surface perturbation is given
in North-East-Down magnetic coordinates.  It is broken down by total
perturbation and by contribution from major current sources (magnetospheric,
FAC, Hall, Pedersen.)  More information can be found in:

Welling, D. (2019). Magnetohydrodynamic Models of B and Their Use in GIC Estimates. In J. L. Gannon, A. Swidinsky, & Z. Xu. (Eds.), Geomagnetically Induced Currents from the Sun to the Power Grid (in press) (Geophysica, pp. 43–65). American Geophysical Union (AGU). https://doi.org/10.1002/9781119434412.ch3

MHD Slice output (mhd_slices) contain a series of files that are 2D Y=0 and Z=0
slices through the MHD magnetosphere (GSM coordinates).  Files with "MHD" in
the name contain MHD state variables such as mass density, magnetic field,
velocity, etc.  Files with "RAY" in the name contain ray tracing results that
report on the state of the field line that threads the computational cell
and lists the latitude and longitude of the field footprint.  More information
on these output files can be found in the SWMF manual.
