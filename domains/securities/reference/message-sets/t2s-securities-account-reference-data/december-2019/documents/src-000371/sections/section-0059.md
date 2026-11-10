---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000371"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["Business Examples", "Securities Account Audit Trail Report - reda.037.001.01"]
content_origin: "source-transcription"
---

# Securities Account Audit Trail Report - reda.037.001.01

Source: [src-000371](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAccountReferenceData_v2.docx`. Locator: heading path Business Examples / Securities Account Audit Trail Report - reda.037.001.01.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P633** Securities Account Audit Trail Report - reda.037.001.01

**P634** Description

**P635** The following Securities Account Audit Trail Report represents the answer to the Securities Account Audit Trail Query described in the chapter 7.8. In this case, the securities account with identification SECACCCSDPXXYYAAA had only one change performed by the user USER1 and approved by the user USER2 on 2019-01-03T17:59:00 regarding the change of the Negative Position from the value False to the new value True. 

**P636** Message Instance

**P637** <Document>

**P638** 	<SctiesAcctAudtTrlRpt>

**P639** 		 <MsgHdr>

**P640** 			<MsgId>NONREF</MsgId>

**P641** 			<OrgnlBizInstr>

**P642** 				<MsgId>SAMPLESACATRQUE</MsgId>

**P643** 			</OrgnlBizInstr>

**P644** 		</MsgHdr>

**P645** 		<RptOrErr>

**P646** 			<SctiesAcctAudtTrlRpt>

**P647** 				<SctiesAcctAudtTrlOrErr>

**P648** 					<AudtTrl>

**P649** 						<FldNm>NegativePosition</FldNm>

**P650** 						<OdFldVal>False</OdFldVal>

**P651** 						<NewFldVal>True</NewFldVal>

**P652** 						<OprTmStmp>2019-01-03T17:59:00</OprTmStmp>

**P653** 						<InstgUsr>USER1</InstgUsr>

**P654** 						<ApprvgUsr>USER2</ApprvgUsr>

**P655** 					</AudtTrl>

**P656** 				</SctiesAcctAudtTrlOrErr>

**P657** 				<SctiesAcctId>

**P658** 					<Id>SECACCCSDPXXYYAAA</Id>

**P659** 				</SctiesAcctId>

**P660** 			</SctiesAcctAudtTrlRpt>

**P661** 		</RptOrErr>

**P662** 	</SctiesAcctAudtTrlRpt>

**P663** </Document>

