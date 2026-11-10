---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Cancellation Query - camt.082.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Cancellation Query - camt.082.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Cancellation Query - camt.082.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1256** Intra-balance Movement Cancellation Query - camt.082.001

**P1257** Description

**P1258** In this example Party A (PBPTYBICXXX) requests a list of Cancellation Instructions on Intra-balance Movements by using an Intra-Balance Movement Cancellation Query with the following search criteria: 

**P1259** T2S Dedicated Cash Account number: “9000000123”.

**P1260** Creation Date of the Cancellation Instructions: January 9th 2015.

**P1261** Cancellation Instruction(s) in Denied status.

**P1262** Response should include FULL details on the reported movements. 

**P1263** Message instance

**P1264** <Document>

**P1265**   	<IntraBalMvmntCxlQry>

**P1266**   	  <Id>

**P1267**    	   <Id>ID0Q0F001144</Id>

**P1268**    	 </Id>

**P1269**  	   <QryDef>

**P1270**   	    <QryTp>FULL</QryTp>

**P1271**   	    <SchCrit>

**P1272**   	      <PrcgSts>

**P1273**   	        <Cd>DEND</Cd>

**P1274** 	        </PrcgSts>

**P1275**  	       <CshAcct>

**P1276**  	         <EQ>

**P1277**  	           <Othr>

**P1278**   	            <Id>9000000123</Id>

**P1279**  	           </Othr>

**P1280**        	   </EQ>

**P1281**        	 </CshAcct>

**P1282** 	        <CreDtTm>

**P1283**        	   <Dt>

**P1284** 	            <EQDt>2015-01-09</EQDt>

**P1285** 	          </Dt>

**P1286** 	        </CreDtTm>

**P1287**       	</SchCrit>

**P1288**     </QryDef>

**P1289**   </IntraBalMvmntCxlQry>

**P1290** </Document>

