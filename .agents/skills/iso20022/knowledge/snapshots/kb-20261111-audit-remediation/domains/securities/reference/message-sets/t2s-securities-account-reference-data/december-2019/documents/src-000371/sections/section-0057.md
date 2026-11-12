---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Activity Advice - reda.035.001.01"]
content_origin: "source-transcription"
---

# Securities Account Activity Advice - reda.035.001.01

Source: [src-000371](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path Business Examples / Securities Account Activity Advice - reda.035.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P577** Securities Account Activity Advice - reda.035.001.01

**P578** Description

**P579** The Securities Account Activity Advice message provides information on changes occurred for securities account reference data during the business day. In this example, it shows one change occurred on 2019-02-01 to the securities account SECACCCSDPXXYYAAA regarding the hold indicator value.

**P580** System date: 2019-02-01

**P581** Securities Account Identification ID: SECACCCSDPXXYYAAA

**P582** Field changed: HoldReleaseDefault

**P583** Old Filed Value: False

**P584** New Field Value: True

**P585** Timestamp of the Update performed: 2019-02-01T16:10:10

**P586** Message Instance

**P587** <Document>

**P588** 	<SctiesAcctActvtyAdvc>

**P589** 		<MsgHdr>

**P590** 			<MsgId>SAMPLESACSTA</MsgId>

**P591** 		</MsgHdr>

**P592** 		<Pgntn>

**P593** 			<PgNb>1</PgNb>

**P594** 			<LastPgInd>true</LastPgInd>

**P595** 		</Pgntn>

**P596** 		<SctiesAcctActvty>

**P597** 			<SysDt>2019-02-01</SysDt>

**P598** 			<Chng>

**P599** 				<SctiesAcctId>

**P600** 					<Id>SECACCCSDPXXYYAAA</Id>

**P601** 				</SctiesAcctId>

**P602** 				<FldNm>HoldReleaseDefault</FldNm>

**P603** 				<OdFldVal>False</OdFldVal>

**P604** 				<NewFldVal>True</NewFldVal>

**P605** 				<OprTmStmp>2019-02-01T16:10:10</OprTmStmp>

**P606** 			</Chng>

**P607** 		</SctiesAcctActvty>

**P608** 	</SctiesAcctActvtyAdvc>

**P609** </Document>

