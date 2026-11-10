---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Business Examples", "Securities Transaction Cancellation Request Query (semt.032)"]
content_origin: "source-transcription"
---

# Securities Transaction Cancellation Request Query (semt.032)

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Business Examples / Securities Transaction Cancellation Request Query (semt.032).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1005** Securities Transaction Cancellation Request Query (semt.032)

**P1006** Description

**P1007** In this example, Party A (BNKAFRPPXXX) requests a list of Cancellation Instructions on Settlement Instructions by using a Securities Transaction Cancellation Request Query with the following search criteria: Securities Account number: “1000000123”; Creation Date of the Cancellation Instructions: March 10th 2025; Cancellation Instruction in Pending Cancellation status; Response should include full details on the reported movements 

**P1009** Message Instance

**P1011** <SctiesTxCxlReqQry>

**P1012** 		<QryDef>

**P1013** 			<QryTp>FULL</QryTp>

**P1014** 			<SchCrit>

**P1015** 				<InstrQryTp>SETT</InstrQryTp>

**P1016** 				<PrcgSts>

**P1017** 					<Cd>CANP</Cd>

**P1018** 				</PrcgSts>

**P1019** 				<SfkpgAcct>

**P1020** 					<Id>1000000123</Id>

**P1021** 				</SfkpgAcct>

**P1022** 				<CreDtTm>

**P1023** 					<Dt>

**P1024** 						<EQDt>2025-03-10</EQDt>

**P1025** 					</Dt>

**P1026** 				</CreDtTm>

**P1027** 			</SchCrit>

**P1028** 		</QryDef>

**P1029** 	</SctiesTxCxlReqQry>

