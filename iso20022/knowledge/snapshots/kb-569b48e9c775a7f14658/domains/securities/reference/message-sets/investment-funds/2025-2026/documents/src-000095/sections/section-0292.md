---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Portfolio Transfer- Additional Examples", "Restricted Security and Conversion"]
content_origin: "source-transcription"
---

# Restricted Security and Conversion

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Portfolio Transfer- Additional Examples / Restricted Security and Conversion.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P4655** Restricted Security and Conversion

**P4656** Description

**P4657** [1]	An AccountHoldingInformation message is sent by the old plan manager (transferor/ceding party), BDAPLULL, to the new plan manager (transferee/acquiring party), PEFILULL, to provide information about assets managed on behalf of the client, Upton Sinclair, account 300001. 

**P4658** There is one asset: 400 units of ISIN LU1234567890. This ISIN is designated as a 'restricted ISIN' and two alternatives, ISIN LU8888888888 and ISIN LU9999999999 are proposed.

**P4659** The ISINs can be transferred via the transfer agent, TATALULL.

**P4660** [2]	Subsequently, PEFILULL sends a PortfolioTransferInstruction message to BDAPLULL, specifying that the ISIN LU1234567890 is to be converted to ISIN LU9999999999 and the asset is to transfer via PEFILULL's account at it custodian, GLOBLULL. The account of GLOBLULL at TATALULL is 444444.

**P4661** [3]	BDAPLULL then sends a PortfolioTransferConfirmation to confirm its intent to transfer. The fund units will be received into GLOBLULL's account 444444 at TATALULL. The units will be delivered from the WWYMLULL's account 222222 at TATALULL. 

**P4662** The Messages

