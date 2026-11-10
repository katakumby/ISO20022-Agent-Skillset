---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000377"]
source_editions: ["june-2021"]
message_ids: []
heading_path: ["Business Examples", "Securities Audit Trail Report - reda.034.001.01"]
content_origin: "source-transcription"
---

# Securities Audit Trail Report - reda.034.001.01

Source: [src-000377](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesReferenceData_v2.docx`. Locator: heading path Business Examples / Securities Audit Trail Report - reda.034.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P915** Securities Audit Trail Report - reda.034.001.01

**P916** Description

**P917** The following Securities Audit Trail Report represents the answer to the Securities Audit Trail Query described in the chapter 7.10. In this case, the security with identification SECXXXYYYZZ1 had only one change performed by the user USER1 and approved by the user USER2 on 2020-02-15T13:45:00, regarding the change of the short name from the value “Sample ES, FIR” to the new value “Sample ES”. 

**P918** Message Instance

**P919** <Document>

**P920** 	<SctiesAudtTrlRpt>

**P921** 		<MsgHdr>

**P922** 			<MsgId>NONREF</MsgId>

**P923** 			<OrgnlBizInstr>

**P924** 				<MsgId>SAMPLEATQSEC001</MsgId>

**P925** 			</OrgnlBizInstr>

**P926** 	</MsgHdr>

**P927** 	<RptOrErr>

**P928** 		<SctiesAudtTrlRpt>

**P929** 				<SctiesAudtTrlOrErr>

**P930** 					<AudtTrl>

**P931** 						<FldNm>ShortName</FldNm>

**P932** 						<OdFldVal>Sample ES, FIR</OdFldVal>

**P933** 						<NewFldVal>Sample ES</NewFldVal>

**P934** 						<OprTmStmp>2020-02-15T13:45:00</OprTmStmp>

**P935** 						<InstgUsr>USER1</InstgUsr>

**P936** 						<ApprvgUsr>USER2</ApprvgUsr>

**P937** 					</AudtTrl>

**P938** 				</SctiesAudtTrlOrErr>

**P939** 				<FinInstrmId>

**P940** 					<ISIN>SECXXXYYYZZ1</ISIN>

**P941** 				</FinInstrmId>

**P942** 			</SctiesAudtTrlRpt>

**P943** 		</RptOrErr>

**P944** 	</SctiesAudtTrlRpt> 

**P945** </Document>

