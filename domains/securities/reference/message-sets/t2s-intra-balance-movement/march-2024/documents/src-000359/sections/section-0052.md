---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Query - camt.078.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Query - camt.078.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Query - camt.078.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P760** Intra-balance Movement Query - camt.078.001

**P761** Description

**P762** In this example a T2S actor has sent to T2S an Intra-Balance Movement Query requesting the full details of all movements for the dedicated cash account ‘9000000123’ where the Restriction Reference is equal to ‘567459’.

**P763** Message instance

**P764** <Document>

**P765**        <IntraBalMvmntQry>

**P766** 		<Id>

**P767** 			<Id>ID0Q0F001122</Id>

**P768** 		</Id>

**P769** 		<QryDef>

**P770** 			<QryTp>FULL</QryTp>

**P771** 			<SchCrit>

**P772** 				<CshAcct>

**P773** 					<EQ>

**P774** 						<Othr>

**P775** 							<Id>9000000123</Id>

**P776** 						</Othr>

**P777** 					</EQ>

**P778** 				</CshAcct>

**P779** 				<CshSubBalId>

**P780** 					<Id>567459</Id>

**P781** 				</CshSubBalId>

**P782** 			</SchCrit>

**P783** 		</QryDef>

**P784** 	</IntraBalMvmntQry>

**P785** </Document>

