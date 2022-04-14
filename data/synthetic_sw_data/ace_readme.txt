ftp://spdf.gsfc.nasa.gov/pub/data/omni/high_res_omni/sc_specific/format.txt

This file gives the common format of the 1-min, spacecraft-specific data
sets created in the process of creating the High Resolution OMNI (HRO)
data set.  It applies to both the ACE, Wind and IMP 8 data sets shifted
to the bow shock nose, to the ACE data shifted to Wind, and to the unshifted
Wind data set.  The content of these data set is much more fully explained at
 http://omniweb.gsfc.nasa.gov/html/HROdocum.html

The common format for the spacecraft-specific data sets is as follows. 
Of the 37 words, words 8-15, 23-28, and 32-34 are 1-min averages formed 
over native-time-resolution data.

Word		        Format   	Comment
		       
Year		         I4		1995 ... 2010
Day		         I4		1 ... 365 or 366
Hour		         I3		0 ... 23
Minute		         I3		0 ... 59 at start of average
# of points in IMF avgs  I4      
Percent interp.	         I4		 See footnote A below
CP/MV Flag	         F4.1		 See footnote A below
Timeshift, sec	         I6
Phase_frnt_nrml, X	 F6.2		GSE components of unit vector,
Phase_frnt_nrml, Y	 F6.2			X comp. always > 0.
Phase_frnt_nrml, Z	 F6.2
Scalar B, nT	         F8.2
Bx, nT (GSE, GSM)	 F8.2
By, nT (GSE)	         F8.2
Bz, nT (GSE)	         F8.2
By, nT (GSM)	         F8.2	        Determined from post-shift GSE components
Bz, nT (GSM)	         F8.2	        Determined from post-shift GSE components
RMS, timeshift, sec	 I7
RMS, Phase front normal  F6.2	        See footnote B below
RMS, Scalar B, nT	 F8.2
RMS, Field vector, nT    F8.2		 See footnote B below
# of points in plasma avgs I4
Flow speed, km/s	 F8.1
Vx Velocity, km/s, GSE   F8.1
Vy Velocity, km/s, GSE   F8.1
Vz Velocity, km/s, GSE   F8.1
Proton Density, n/cc	 F7.2
Temperature, K	         F9.0
X(s/c), GSE, Re	         F8.2		Position of spacecraft
Y(s/c), GSE, Re	         F8.2
Z(s/c), GSE, Re	         F8.2
X(target), GSE, Re	 F8.2		Position of bow shock nose or Wind
Y(target), GSE, Re	 F8.2
Z(target), GSE, Re	 F8.2
RMS(target), Re	         F8.2		 See footnote B below
DBOT1, sec	         I7		 See footnote C below		
DBOT2, sec	         I7		 See footnote C below

The data may be read with the format statement:
(I4,I4,2I3,2I4,F4.1,I7,3F6.2,6F8.2,I7,F6.2,2F8.2,I4,4F8.1,F7.2,F9.0,3F8.2,4F8.2,2I7)

Footnote A:

Percent interp: The percent (0-100) of the points contributing 
to the 1-min magnetic field averages whose phase front normal 
(PFN) was interpolated because neither the MVAB-0 nor Cross 
Product shift techniques yielded a PFN that satisfied its 
respective tests (see above for these).

CP/MV flag: The fraction (0-1) of the points, that contribute to 
the 1-min magnetic field averages and that are not based on 
interpolated PFN's, whose PFN was based on the MVAB-0 method.

If in a given 1-min magnetic field average, there are n points with 
CP-based PFN's, p points with MVAB-0 PFN's and q points with 
interpolated PFN's, then Percent interp = 100 * q/(n+p+q) and 
CP/MV flag = p/(p+n) (or = 9.9 if p+n = 0)

Footnote B:

Note that standard deviations for the three vectors are given as 
the square roots of the sum of squares of the standard deviations 
in the component averages. The component averages are given 
in the records but not their individual standard deviations.

Footnote C: 

The DBOT (Duration Between Observing Times) 
words: For a given record, we take the 1-min average time shift 
and estimate, using the solar wind velocity and the location of the 
observing spacecraft, the time at which the corresponding 
observation would have been made at the spacecraft. Then we 
take the difference between this time and the corresponding time 
of the preceding 1-min record and define this as DBOT1. This 
difference would be one minute in the absence of PFN and/or 
flow velocity variations. When this difference becomes negative, 
we have apparent out-of- sequence arrivals of phase planes. 
That is, if plane A is observed before plane B at the spacecraft, 
plane B is predicted to arrive at the target before plane A. 
Searching for negative DBOT enables finding of such cases.

DBOT2 is like DBOT1 except that the observation time for 
the current 1-min record is compared to the latest (most time-
advanced) previous observation time and not to the observation 
time of the previous record. Use of DBOT2 helps to find extended
intervals of out-of-sequence arrivals.

We do not capture out-of-sequence-arrival information at 
15-s resolution but only at 1-min resolution. The standard 
deviation in the 1-min averaged time shifts may be used to 
help find cases of out-of-sequence 15-s data. 
--------------------------------------------------------------

