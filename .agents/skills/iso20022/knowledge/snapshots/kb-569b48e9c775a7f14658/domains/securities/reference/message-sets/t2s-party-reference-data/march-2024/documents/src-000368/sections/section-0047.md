---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
source_ids: ["src-000368"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Business Examples", "Party Query - reda.015.001"]
content_origin: "source-transcription"
---

# Party Query - reda.015.001

Source: [src-000368](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_PartyReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_PartyReferenceData_2023_2024_v2.docx`. Locator: heading path Business Examples / Party Query - reda.015.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P511** Party Query - reda.015.001

**P512** Description

**P513** The PartyQuery (reda.015) message can be used to perform the following queries:

**P514** Party Reference Data Query;

**P515** Party List Query;

**P516** Restricted Party Query. 

**P517** In this example the NCB NCBAXXYYAAA performs a Party List Query, used to query all the party under the NCB data scope.

**P518** Message Instance

**P519** <Document>

**P520** 	<PtyQry>

**P521** 		<MsgHdr>

**P522** 			<MsgId>SAMPLEPTYLISQUE</MsgId>

**P523** 			<ReqTp>

**P524** 				<Prtry>

**P525** 					<Id>PYLI</Id>

**P526** 				</Prtry>

**P527** 			</ReqTp>

**P528** 		</MsgHdr>

**P529** 		<SchCrit>

**P530** 			<RspnsblPtyId>

**P531** 				<Id>

**P532** 					<AnyBIC>NCBAXXYYAAA</AnyBIC>

**P533** 				</Id>

**P534** 			</RspnsblPtyId>

**P535** 		</SchCrit>

**P536** 	</PtyQry>

**P537** </Document>

**P538**   


