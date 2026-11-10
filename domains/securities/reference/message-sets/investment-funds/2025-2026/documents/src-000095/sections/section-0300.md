---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer- Additional Examples", "Cash All "]
content_origin: "source-transcription"
---

# Cash All 

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Portfolio Transfer- Additional Examples / Cash All .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4682** Cash All 

**P4683** Description

**P4684** [1]	An AccountHoldingInformation message is sent by the old plan manager (transferor/ceding party), BDAPLULL, to the new plan manager (transferee/acquiring party), PEFILULL, to provide information about assets managed on behalf of the client, Upton Sinclair, account 300001. 

**P4685** There are two assets:

**P4686** [1] 	400 units of ISIN LU11111111, Ethical Green Fund. The ISIN can be transferred via the transfer agent, TATALULL.

**P4687** [2]	700 units if ISIN LU2222222222, Ethical Red Fund. The ISIN can be transferred via the transfer agent, TATALULU

**P4688** [2]	Subsequently, PEFILULL sends a PortfolioTransferInstruction message to BDAPLULL, specifying that all the assets are to be liquidated and transferred as EUR cash. 

**P4689** The cash for both assets is to be paid to the account of PEFILULL at BARCLULL. The payment reference specified is PORT-X1-001-PAYM. The cash is to be paid to IBAN LU85324906366027 at BARCLULL. The subsequent cash payment instruction/s are not shown.

