---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["Business Examples", "Security Maintenance Status Advice - reda.029.001.01", "Security Maintenance Status Advice - reda.029.001.01 – Rejected example"]
content_origin: "source-transcription"
---

# Security Maintenance Status Advice - reda.029.001.01 – Rejected example

Source: [src-000377](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path Business Examples / Security Maintenance Status Advice - reda.029.001.01 / Security Maintenance Status Advice - reda.029.001.01 – Rejected example.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P588** Security Maintenance Status Advice - reda.029.001.01 – Rejected example

**P589** Description

**P590** In this example the Securities Maintenance Status Advice reports that the Securities Maintenance Request has been rejected, specifying the rejection reason.

**P591** Original Message ID: SAMPLEUPDSEC001

**P592** Status: REJT

**P593** Reason: ERRU001 MAINTENANCE REJECTED

**P594** Message Instance

**P595** <Document>

**P596** 	<SctyMntncStsAdvc>

**P597** 		<MsgHdr>

**P598** 			<MsgId>NONREF</MsgId>

**P599** 			<OrgnlBizInstr>

**P600** 				<MsgId>SAMPLEUPDSEC001</MsgId>

**P601** 			</OrgnlBizInstr>

**P602** 		</MsgHdr>

**P603** 		<PrcgSts>

**P604** 			<Prtry>

**P605** 				<PrtrySts>

**P606** 					<Id>REJT</Id>

**P607** 					<Issr>T2S</Issr>

**P608** 					<SchmeNm>SMSS</SchmeNm>

**P609** 				</PrtrySts>

**P610** 				<PrtryRsn>

**P611** 					<Rsn>

**P612** 						<Id>REJT</Id>

**P613** 						<Issr>T2S</Issr>

**P614** 						<SchmeNm>SMSR</SchmeNm>

**P615** 					</Rsn>

**P616** 					<AddtlRsnInf>ERRU001 MAINTENANCE REJECTED</AddtlRsnInf>

**P617** 				</PrtryRsn>

**P618** 			</Prtry>

**P619** 		</PrcgSts>

**P620** 	</SctyMntncStsAdvc>

**P621** </Document>

