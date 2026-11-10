---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["Business Examples", "Cash Account Audit Trail Query / Report", "reda.040.001.01 CashAccountAuditTrailReport"]
content_origin: "source-transcription"
---

# reda.040.001.01 CashAccountAuditTrailReport

Source: [src-000350](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Locator: heading path Business Examples / Cash Account Audit Trail Query / Report / reda.040.001.01 CashAccountAuditTrailReport.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P333** reda.040.001.01 CashAccountAuditTrailReport

**P334** Description

**P335** A CashAccountAuditTrailQuery message is sent by an account servicer, to an institution in response to a cash account audit trail query.

**P336** Message Instance

**P338** <CshAcctAudtTrlRpt>

**P339** 	<MsgHdr>

**P340** 		<MsgId>NONREF</MsgId>

**P341** 		<OrgnlBizInstr>

**P342** 			<MsgId>SAMPLECSHATRQUE</MsgId>

**P343** 		</OrgnlBizInstr>

**P344** 	</MsgHdr>

**P345** 	<RptOrErr>

**P346** 		<CshAcctAudtTrlRpt>

**P347** 			<CshAcctAudtTrlOrErr>

**P348** 				<AudtTrl>

**P349** 					<FldNm>CeilingNotificationAmount</FldNm>

**P350** 					<OdFldVal>500000</OdFldVal>

**P351** 					<NewFldVal>1000000</NewFldVal>

**P352** 					<OprTmStmp>2018-01-03T17:59:00</OprTmStmp>

**P353** 					<InstgUsr>USERTWOEYES</InstgUsr>

**P354** 				</AudtTrl>

**P355** 			</CshAcctAudtTrlOrErr>

**P356** 			<CshAcctId>

**P357** 				<Id>

**P358** 					<Othr>

**P359** 						<Id>ACC001</Id>

**P360** 					</Othr>

**P361** 				</Id>

**P362** 			</CshAcctId>

**P363** 		</CshAcctAudtTrlRpt>

**P364** 	</RptOrErr>

**P365** </CshAcctAudtTrlRpt>

