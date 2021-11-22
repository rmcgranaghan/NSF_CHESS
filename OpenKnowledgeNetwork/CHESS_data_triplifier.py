# Cogan Shimizu



import re, time
t = time.time()

import rdflib
from rdflib.namespace import DC, RDF, RDFS, XMLNS, XSD, OWL

# Create the graph
g = rdflib.Graph()

# ===========================
# Namespaces
namespaces = dict()
ns = namespaces # just an alias

# These URIs are not resolvable - but will be and will point to where you can examine the ontology
namespaces["chess-ont"] = rdflib.URIRef("https://chess-science.com/ont/#")
namespaces["chess-res"] = rdflib.URIRef("https://chess-science.com/res/#")
namespaces["cdt"]       = rdflib.URIRef("http://w3id.org/lindt/custom_datatypes#") # way of describing data types (as literals)
namespaces["sosa"]      = rdflib.URIRef("http://www.w3.org/ns/sosa/")
namespaces["ssn"]       = rdflib.URIRef("http://www.w3.org/ns/ssn/")

# Default namespace, not _super_ useful
default_namespace = namespaces["chess-ont"]

# Create the prefixes
for prefix in namespaces.keys():
	g.bind(prefix, namespaces[prefix])

# ===========================
# Some utility functions
def mint_uri(name, prefix=default_namespace):
	uri = rdflib.URIRef(prefix+name)

	return uri

# ===========================
# Some sosa/ssn stuff
sosa_ssn_properties = dict()
ssp = sosa_ssn_properties # just an alias
ssp_t = [
("op", "ObservableProperty"),
("observedProperty", "observedProperty"),
("foi", "FeatureOfInterest"),
("hsr", "hasSimpleResult"),
("o", "Observation"),
("oc", "ObservationCollection"),
("hm", "hasMember"),
("pt", "phenomenomTime")
]
for x,y in ssp_t:
	ssp[x] = mint_uri(y)

# ===========================
# Some datatypes
datatypes = dict()
dts = datatypes # just an alias
dts["ucum"] = mint_uri("ucum",ns["cdt"]) # serialization of typing strings of complex units (e.g., string rep for km/s)

# ===========================
# Load in the raw data
filename = "chess_data_annotated.csv"
# filename = "chess_data_abbrv.csv"
header = ""
lines = list()
with open(filename) as f:
	header, *lines = f.readlines()
	print("Successfully loaded file: " + filename + ".")

# ===========================
# Process the header
labels = header.strip().split(",")

# Create URIs for the observable properties (calling everything observable ppties for simplicity, except for time)
ops_str = [re.sub("\(.*?\)","",x).strip().replace(" ", "_") for x in labels[1:]] #slice out unit data
ops_uri = [mint_uri(op_str, ns["chess-res"]) for op_str in ops_str]
for op_uri in ops_uri:
	g.add((
		op_uri,
		RDF.type,
		ssp["op"]))

# Create some URIs for the observation posts
# observers = labels[10:]
# for observer in observers:
# 	# Strip off parens, whitespace, replace spaces
# 	observer = observer[:-3].strip().replace(" ", "_")
# 	g.add(
# 		(mint_uri(observer),
# 		RDF.type,
# 		mint_uri("ObservationPost")))

# Get the units
units = list()
for label in labels[1:]:
	match = re.search("\(.*?\)",label)
	unit = match.group()[1:-1]
	units.append(unit)

print("Finished \"singleton\" instances.")

# ===========================
# Materialize!
'''Time (UT),Vx GSE (km/s),Vy GSE (km/s),Vz GSM (km/s),Bx GSM (nT),
   By GSM (nT),Bz GSM (nT),p_protons (#/cm^3),SMR (nT),SML (nT),
   Sullivan GIC (A),Paradise GIC (A),Bullrun GIC (A),Montgomery GIC (A),
   Rutherford GIC (A),Shelby GIC (A),Weakley GIC (A),Widowscreek1 GIC (A)'''
print("Begin processing", len(lines),"records.")
row = 0
for line in lines:
	values = line.split(",")
	# Create an Observation Collection for the row
	#  Observation Collection == set of observations that share a characteristics (e..g, time)
	oc_str = "oc" + str(row)
	oc_uri = mint_uri(oc_str, ns["chess-res"]) #create an obs collection and mint a new URI
	g.add((
		oc_uri,
		RDF.type,
		ssp["oc"]))

	# Set the phenomenom time for the row
	datetime = values[0]
	g.add((
		oc_uri,
		ssp["pt"],
		rdflib.Literal(datetime, datatype=XSD.datetime)))

	# Create the Observations for the collection - this is triplifying a whole row after datetime
	obs_n = 0
	for obs_value in values[1:10]:
		# The observation itself
		obs_str = oc_str + ".obs" + str(obs_n)
		obs_uri = mint_uri(obs_str,ns["chess-res"])
		g.add((
			obs_uri,
			RDF.type,
			ssp["o"]))

		# Link the observation to the observation collection (i.e., link to the row)
		g.add((
			oc_uri,
			ssp["hm"],
			obs_uri))

		# Link the observation to the observable property (i.e., link to the column)
		g.add((
			obs_uri,
			ssp["observedProperty"],
			ops_uri[obs_n]))

		# Link the observable property to its simple result (link the observation to its value)
		simple_result_str = obs_value + " " + units[obs_n]
		simple_result_literal = rdflib.Literal(simple_result_str, datatype=dts["ucum"])
		g.add((
			obs_uri,
			ssp["hsr"],
			simple_result_literal))
		obs_n += 1

	# increment row
	row += 1

# ===========================
# Output to file
output_filename = "output.ttl"
with open(output_filename, "w") as output:
	temp = g.serialize(format="turtle", encoding="utf-8", destination=None)
	output.write(temp.decode("utf-8"))
	print("Successfully output file: " + output_filename + ".")
	t = time.time() - t
	print("Completed in",t,"seconds.")

with open(output_filename) as f:
	print("Computing Statistics.")
	lines = f.readlines()
	filtered = [line for line in lines if line.strip() != ""]
	print(len(filtered),"were processed.")
	print("Completed in",t,"seconds")