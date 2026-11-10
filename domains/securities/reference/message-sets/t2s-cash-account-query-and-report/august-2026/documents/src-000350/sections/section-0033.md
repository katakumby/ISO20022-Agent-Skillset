---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000350"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["Business Examples", "Cash Account Activity Advice", "reda.038.001.01 CashAccountActivityAdvice"]
content_origin: "source-transcription"
---

# reda.038.001.01 CashAccountActivityAdvice

Source: [src-000350](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart1_Target2Securities_CashAccountQueryAndReport_v2.docx`. Locator: heading path Business Examples / Cash Account Activity Advice / reda.038.001.01 CashAccountActivityAdvice.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P282** reda.038.001.01 CashAccountActivityAdvice

**P283** Description

**P284** A CashAccountActivityAdvice statement is sent by an account servicer, to an institution requesting information on changes applied to cash accounts.

**P285** Message Instance

**P286** <CshAcctActvtyAdvc>

**P287** 	<MsgHdr>

**P288** 		<MsgId>SAMPLECSHSTA</MsgId>

**P289** 	</MsgHdr>	<CshAcctActvty>

**P290** 		<SysDt>2011-02-01</SysDt>

**P291** 		<Chng>

**P292** 			<CshAcctId>

**P293** 				<Id>

**P294** 					<Othr>

**P295** 						<Id>5678</Id>

**P296** 					</Othr>

**P297** 				</Id>

**P298** 			</CshAcctId>

**P299** 			<FldNm>T2SDCA.FloorNotificationAmount</FldNm>

**P300** 				<OdFldVal>500000</OdFldVal>

**P301** 				<NewFldVal>1000000</NewFldVal>

**P302** 				<OprTmStmp>2011-02-01T15:23:10</OprTmStmp>

**P303** 		</Chng>

**P304** 	</CshAcctActvty>

**P305** </CshAcctActvtyAdvc>

