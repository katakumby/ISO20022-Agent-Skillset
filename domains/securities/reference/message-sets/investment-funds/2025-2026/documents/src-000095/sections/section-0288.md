---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer- Additional Examples", "Multiple transfer places - 2"]
content_origin: "source-transcription"
---

# Multiple transfer places - 2

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Portfolio Transfer- Additional Examples / Multiple transfer places - 2.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4642** Multiple transfer places - 2

**P4643** Description

**P4644** [1]	An AccountHoldingInformation message is sent by the old plan manager (transferor/ceding party), BDAPLULL, to the new plan manager (transferee/acquiring party), PEFILULL, to provide information about assets managed on behalf of the client, Janice Green, account 200001. 

**P4645** There is one asset: 900 units of ISIN LU22222222, Ethical Blue Fund. This ISIN can be transferred via the transfer agent, TATALULL or through the CSD, CSDALULL.

**P4646** [2]	Subsequently, PEFILULL sends a PortfolioTransferInstruction message to BDAPLULL, specifying that the asset is to transfer via the CSD, CSDALULL. PEFILULL provides its account information at CSDALULL. PEFILULL uses the custodian, GLOBLULL. The account of GLOBLULL at CSDALULL is 444444.

**P4647** [3]	BDAPLULL then sends a PortfolioTransferConfirmation to confirm its intent to transfer. The transfer will take place at CSDALULL. BDAPLULL uses the custodian WWYMLULL. The account of WWYMLULL at CSDALILL is 777777. 

**P4648** The Messages

