---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["Business Examples", "Security Activity Advice - reda.009.001.01"]
content_origin: "source-transcription"
---

# Security Activity Advice - reda.009.001.01

Source: [src-000377](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path Business Examples / Security Activity Advice - reda.009.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P859** Security Activity Advice - reda.009.001.01

**P860** Description

**P861** The Security Activity Advice message provides information on changes occurred for securities reference data during the business day. In this example, it shows one change occurred on 2020-09-01 to the security SECXXXYYYZZ1 regarding the classification type.

**P862** System date: 2020-09-01

**P863** Security Identification ID: SECXXXYYYZZ1

**P864** Field changed: ClassificationType

**P865** Old Filed Value: ESFUFR

**P866** New Field Value: ESFTFR

**P867** Message Instance

**P868** <Document>

**P869** 		<SctyActvtyAdvc>

**P870** 		<MsgHdr>

**P871** 			<MsgId>NONREF</MsgId>

**P872** 		</MsgHdr>

**P873** 		<Pgntn>

**P874** 			<PgNb>1</PgNb>

**P875** 			<LastPgInd>true</LastPgInd>

**P876** 		</Pgntn>

**P877** 		<SctyActvty>

**P878** 			<SysDt>2020-09-01</SysDt>

**P879** 			<Chng>

**P880** 				<FinInstrmId>

**P881** 					<ISIN>SECXXXYYYZZ1</ISIN>

**P882** 				</FinInstrmId>

**P883** 				<FldNm>ClassificationType</FldNm>

**P884** 				<OdFldVal>ESFUFR</OdFldVal>

**P885** 				<NewFldVal>ESFTFR</NewFldVal>

**P886** 				<OprTmStmp>2020-09-01T09:10:10</OprTmStmp>

**P887** 			</Chng>

**P888** 		</SctyActvty>

**P889** 	</SctyActvtyAdvc>

**P890** </Document>

