from flask import Flask
import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=815fa4db-dc03-4c70-869a-a9cc13f33084.bs2io90l08kqb1od8lcg.databases.appdomain.cloud;PORT=30367;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=mfk63399;PWD=XErGj3Qzp8lniA3U",'','')

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
print("Connected to IBM DB2 Database Successfully")


 