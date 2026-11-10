---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "AccountManagementStatusReport acmt.006.001.07 – Rejected"]
content_origin: "source-transcription"
---

# AccountManagementStatusReport acmt.006.001.07 – Rejected

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Account Management  / AccountManagementStatusReport acmt.006.001.07 – Rejected.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1631** AccountManagementStatusReport acmt.006.001.07 – Rejected

**P1632** Description

**P1633** In this example, an AccountManagementStatusReport message is sent by an account servicer to the account owner in order to indicate the status of an account modification instruction (reference Mod-123456) is rejected. 

**P1634** The modification instruction is rejected because it is not compliant with service level agreement (NSLA) because it contains a modification to the withdrawal investment plan and this is not allowed.

**P1635** Message Instance

**P1636** <AcctMgmtStsRpt>

**P1637** 	<MsgId>

**P1638** 		<Id>123456-7</Id>

**P1639** 		<CreDtTm>2020-01-16T11:20:00</CreDtTm>

**P1640** 	</MsgId>

**P1641** 	<RltdRef>

**P1642** 		<Ref>Mod-123456</Ref>

**P1643** 	</RltdRef>

**P1644** 	<StsRpt>

**P1645** 		<Sts>

**P1646** 			<Rjctd>

**P1647** 				<Rsn>

**P1648** 					<Cd>NSLA</Cd>

**P1649** 				</Rsn>

**P1650** 				<AddtlRsnInf>Withdrawal investment modifications not allowed </AddtlRsnInf>

**P1651** 			</Rjctd>

**P1652** 		</Sts>

**P1653** 	</StsRpt>

**P1654** </AcctMgmtStsRpt>

