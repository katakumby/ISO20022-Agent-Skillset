---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer- Additional Examples", "Partial Transfer"]
content_origin: "source-transcription"
---

# Partial Transfer

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Portfolio Transfer- Additional Examples / Partial Transfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4669** Partial Transfer

**P4670** Description

**P4671** [1]	An AccountHoldingInformation message is sent by the old plan manager (transferor/ceding party), BDAPLULL, to the new plan manager (transferee/acquiring party), PEFILULL, to provide information about assets managed on behalf of the client, Upton Sinclair, account 300001. 

**P4672** There is one asset: 1200 units of ISIN LU1111111111, Ethical Green Fund. This ISIN can be transferred via the transfer agent, TATALULL.

**P4673** [2]	Subsequently, PEFILULL sends a PortfolioTransferInstruction message to BDAPLULL, specifying a partial transfer of 800 units of ISIN LU1111111111. The units are to be transferred to PEFILULL's account, 555555 at the transfer agent, TATALULL

**P4674** [3]	BDAPLULL then sends a PortfolioTransferConfirmation to confirm its intent to transfer 800 units. The fund units will be received into PEFILULL's account, 555555 at the transfer agent, TATALULL. The units will be delivered from the BDAPLULL's account 222222 at TATALULL

**P4675** The Messages

