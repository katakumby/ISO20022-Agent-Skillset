---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "AccountManagementStatusReport acmt.006.001.07 – Received"]
content_origin: "source-transcription"
---

# AccountManagementStatusReport acmt.006.001.07 – Received

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Account Management  / AccountManagementStatusReport acmt.006.001.07 – Received.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1612** AccountManagementStatusReport acmt.006.001.07 – Received

**P1613** Description

**P1614** An AccountManagementStatusReport message is sent by an account servicer to the account owner in order to indicate the status of an account modification instruction. 

**P1615** This AccountManagementStatusReport message indicates that the status of the account modification instruction referenced as 123456-3 has been received (RECE) and is acknowledged.

**P1616** Message Instance

**P1617** <AcctMgmtStsRpt>

**P1618** 	<MsgId>

**P1619** 		<Id>123456-6</Id>

**P1620** 		<CreDtTm>2020-01-14T13:10:00</CreDtTm>

**P1621** 	</MsgId>

**P1622** 	<RltdRef>

**P1623** 		<Ref>123456-3</Ref>

**P1624** 	</RltdRef>

**P1625** 	<StsRpt>

**P1626** 		<Sts>

**P1627** 			<Sts>RECE</Sts>

**P1628** 		</Sts>

**P1629** 	</StsRpt>

**P1630** </AcctMgmtStsRpt>

