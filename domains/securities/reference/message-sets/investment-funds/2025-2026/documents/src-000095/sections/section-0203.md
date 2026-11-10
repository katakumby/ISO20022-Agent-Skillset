---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "RequestForAccountManagementStatusReport acmt.005.001.06 "]
content_origin: "source-transcription"
---

# RequestForAccountManagementStatusReport acmt.005.001.06 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Account Management  / RequestForAccountManagementStatusReport acmt.005.001.06 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1589** RequestForAccountManagementStatusReport acmt.005.001.06 

**P1590** Description

**P1591** A RequestForAccountManagementStatusReport message is sent by an account owner to an account servicer in order to request the status of previously sent AccountModificationInstruction message for which an AccountDetailsConfirmation message has not yet been received. 

**P1592** This RequestForAccountManagementStatusReport message requests the status of an AccountModificationInstruction message with message identification 123456-12, for account number 66666666.

**P1593** Message Instance

**P1594** <ReqForAcctMgmtStsRpt>

**P1595** 	<MsgId>

**P1596** 		<Id>123456-25</Id>

**P1597** 		<CreDtTm>2020-01-14T13:00:00</CreDtTm>

**P1598** 	</MsgId>

**P1599** 	<ReqDtls>

**P1600** 		<LkdRef>

**P1601** 			<PrvsRef>

**P1602** 				<Ref>123456-12</Ref>

**P1603** 				<MsgNm>acmt.003</MsgNm>

**P1604** 			</PrvsRef>

**P1605** 		</LkdRef>

**P1606** 		<StsReqTp>ACCM</StsReqTp>

**P1607** 		<InvstmtAcct>

**P1608** 			<AcctId>66666666</AcctId>

**P1609** 		</InvstmtAcct>

**P1610** 	</ReqDtls>

**P1611** </ReqForAcctMgmtStsRpt>

