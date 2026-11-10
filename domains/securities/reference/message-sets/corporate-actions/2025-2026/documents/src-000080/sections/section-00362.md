---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.3 NonEligibleProceedsIndicator <NonElgblPrcdsInd>"]
file_pages: [488]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.3 NonEligibleProceedsIndicator <NonElgblPrcdsInd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 488 to 488.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 488

```text
CodeName Name Definition
ACTU ActualPayment The cash payment occurs or will occur
upon receipt of proceeds from the issuer.
CONT ContractualPayment The cash payment occurs or will occur in
advance of receipt of proceeds from the
issuer and based on a contractual
agreement established with the account
servicer.
7.4.13.23.3  NonEligibleProceedsIndicator <NonElgblPrcdsInd>
Presence: [0..1]
Definition: Specifies information regarding outturn resources that cannot be processed by the Central
Securities Depository (CSD). Special delivery instruction is required from the account owner for the
corporate action outcome to be credited.
NonEligibleProceedsIndicator <NonElgblPrcdsInd> contains one of the following elements (see
"NonEligibleProceedsIndicator3Choice" on page 916 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 916
Or}   Proprietary <Prtry> [1..1] ± 916
7.4.13.23.4  IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd>
Presence: [0..1]
Definition: Proceeds are taxable according to the information provided by the issuer / offeror.
IssuerOfferorTaxabilityIndicator <IssrOfferrTaxbltyInd> contains one of the following
IssuerOfferorTaxabilityIndicator2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 488
Or}   Proprietary <Prtry> [1..1] ± 488
7.4.13.23.4.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify information regarding the issuer / offeror taxability status.
Datatype: "IssuerTaxability2Code" on page 1218
CodeName Name Definition
TXBL Taxable The relevant proceeds are taxable.
7.4.13.23.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification to specify information regarding the issuer / offeror taxability status.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 488 February 2026
```

