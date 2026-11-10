---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer- Additional Examples", "Multiple transfer places - 1"]
content_origin: "source-transcription"
---

# Multiple transfer places - 1

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Portfolio Transfer- Additional Examples / Multiple transfer places - 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4629** Multiple transfer places - 1

**P4630** Description

**P4631** [1]	An AccountHoldingInformation message is sent by the old plan manager (transferor/ceding party), BDAPLULL, to the new plan manager (transferee/acquiring party), PEFILULL, to provide information about assets managed on behalf of the client, Janice Green, account 200001. 

**P4632** There is one asset: 700 units of ISIN LU1111111111, Ethical Green Fund. This ISIN can be transferred via the transfer agent, TATALULL or through the CSD, CSDALULL.

**P4633** [2]	Subsequently, PEFILULL sends a PortfolioTransferInstruction message to BDAPLULL, specifying that the asset is to transfer via the transfer agent, TATALULL. PEFILULL provides its account information at TATALULL. PEFILULL uses the custodian, GLOBLULL. The account of GLOBLULL at TATALULL is 555555.

**P4634** [3]	BDAPLULL then sends a PortfolioTransferConfirmation to confirm its intent to transfer. The transfer will take place at TATALULL and the relevant delivery account information is provided. 

**P4635** The Messages

