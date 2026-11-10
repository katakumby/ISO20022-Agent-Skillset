---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "Account Closing", "Message 2 - AccountManagementStatusReport acmt.006.001.07"]
content_origin: "source-transcription"
---

# Message 2 - AccountManagementStatusReport acmt.006.001.07

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Account Management  / Account Closing / Message 2 - AccountManagementStatusReport acmt.006.001.07.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1677** Message 2 - AccountManagementStatusReport acmt.006.001.07

**P1678** Description

**P1679** The account service responds with an AccountManagementStatusReport to report the AccountModificationInstruction has been received (RECE). Subsequently, the account servicer may send an AccountManagementStatusReport to report the AccountModificationInstruction has been validated and accepted (ACCP) but this is not shown.

**P1680** Message Instance

**P1681** <AcctMgmtStsRpt>

**P1682** 	<MsgId>

**P1683** 		<Id>CA572001</Id>

**P1684** 		<CreDtTm>2020-01-05T09:03:00</CreDtTm>

**P1685** 	</MsgId>

**P1686** 	<RltdRef>

**P1687** 		<Ref>FD43001</Ref>

**P1688** 	</RltdRef>

**P1689** 	<StsRpt>

**P1690** 		<Sts>

**P1691** 			<Sts>RECE</Sts>

**P1692** 		</Sts>

**P1693** 		<AcctId>111111</AcctId>

**P1694** 	</StsRpt>

**P1695** </AcctMgmtStsRpt>

