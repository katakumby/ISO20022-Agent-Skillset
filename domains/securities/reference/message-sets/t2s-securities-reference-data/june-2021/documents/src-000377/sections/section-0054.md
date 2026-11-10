---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["Business Examples", "Security Query - reda.010.001.01"]
content_origin: "source-transcription"
---

# Security Query - reda.010.001.01

Source: [src-000377](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path Business Examples / Security Query - reda.010.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P744** Security Query - reda.010.001.01

**P745** Description

**P746** The Security Query message can be used to perform the following queries:

**P747** Securities Reference Data Query; 

**P748** ISIN List Query;

**P749** Securities CSD Link Query; 

**P750** Securities Deviating Nominal Query.

**P751** In this example the Party CSDXCCYY001 performs a Securities Reference Data Query to request reference data about all the securities issued after “2020-01-01” and before “2020-31-12”.

**P752** Message Instance

**P753** <Document>

**P754** 	<SctyQry>

**P755** 		<MsgHdr>

**P756** 			<MsgId>SAMPLEQRYSEC001</MsgId>

**P757** 		</MsgHdr>

**P758** 		<ReqTp>

**P759** 			<Id>SECR</Id>

**P760** 			<SchmeNm>SECQ</SchmeNm>

**P761** 			<Issr>T2S</Issr>

**P762** 		</ReqTp>

**P763** 		<SchCrit>

**P764** 			<IsseDt>

**P765** 			<FrToDt>

**P766** 				<FrDt>2020-01-01</FrDt>

**P767** 				<ToDt>2020-12-31</ToDt>

**P768** 			</FrToDt>

**P769** 			</IsseDt>

**P770** 		</SchCrit>

**P771** 	</SctyQry>

**P772** </Document>

