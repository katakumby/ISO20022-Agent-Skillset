---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "GetAccountDetails acmt.004.001.06 "]
content_origin: "source-transcription"
---

# GetAccountDetails acmt.004.001.06 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Account Management  / GetAccountDetails acmt.004.001.06 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1567** GetAccountDetails acmt.004.001.06 

**P1568** Description

**P1569** A GetAccountDetails message, is sent by an account owner to an account servicer in order to instruct the return of registered information about an existing account.

**P1570** This GetAccountDetails message is instructing the return of the following selected account information: investment account characteristics, account parties and investment plan for the account bearing the number XYZ123456789. 

**P1571** Message Instance

**P1572** <GetAcctDtls>

**P1573** 	<MsgId>

**P1574** 		<Id>123456-4</Id>

**P1575** 		<CreDtTm>2020-01-15T09:30:30</CreDtTm>

**P1576** 	</MsgId>

**P1577** 	<InvstmtAcctSelctn>

**P1578** 		<AcctId>XYZ123456789</AcctId>

**P1579** 	</InvstmtAcctSelctn>

**P1580** 	<SelctdInfTp>

**P1581** 		<InvstmtAcct>true</InvstmtAcct>

**P1582** 		<AcctPties>true</AcctPties>

**P1583** 		<Intrmies>false</Intrmies>

**P1584** 		<InvstmtPlan>true</InvstmtPlan>

**P1585** 		<CshSttlm>false</CshSttlm>

**P1586** 		<SvcLvlAgrmt>false</SvcLvlAgrmt>

**P1587** 	</SelctdInfTp>

**P1588** </GetAcctDtls>

