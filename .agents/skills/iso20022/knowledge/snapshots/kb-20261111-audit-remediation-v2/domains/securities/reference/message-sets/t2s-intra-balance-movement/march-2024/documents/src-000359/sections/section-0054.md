---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Modification Query - camt.080.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Modification Query - camt.080.001

Source: [src-000359](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Modification Query - camt.080.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1120** Intra-balance Movement Modification Query - camt.080.001

**P1121** Description

**P1122** In this example Party A (PBPTYBICXXX) requests a full details list of Amendment Instruction on Intra-balance Movements by using an Intra-Balance Movement Modification Query with the following search criteria:  

**P1123** T2S Dedicated Cash Account number: “9000000123”; 

**P1124** Creation Date of the Amendment Instructions: January 9th 2015. 

**P1125** Message instance

**P1126** <Document>

**P1127** 	<IntraBalMvmntModQry>

**P1128** 		<Id>

**P1129** 			<Id>ID0Q0F001133</Id>

**P1130** 		</Id>

**P1131** 		<QryDef>

**P1132** 			<QryTp>FULL</QryTp>

**P1133** 			<SchCrit>

**P1134** 				<CshAcct>

**P1135** 					<EQ>

**P1136** 						<Othr>

**P1137** 							<Id>9000000123</Id>

**P1138** 						</Othr>

**P1139** 					</EQ>

**P1140** 				</CshAcct>

**P1141** 				<CreDtTm>

**P1142** 					<Dt>

**P1143** 						<EQDt>2015-01-09</EQDt>

**P1144** 					</Dt>

**P1145** 				</CreDtTm>

**P1146** 			</SchCrit>

**P1147** 		</QryDef>

**P1148** 	</IntraBalMvmntModQry>

**P1149** </Document>

