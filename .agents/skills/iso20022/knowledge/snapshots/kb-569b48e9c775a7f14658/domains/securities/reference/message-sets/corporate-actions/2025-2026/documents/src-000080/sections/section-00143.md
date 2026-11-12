---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.25 CashMovementDetails <CshMvmntDtls>", "3.4.11.25.2 ContractualPaymentIndicator <CtrctlPmtInd>"]
file_pages: [205]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.25.2 ContractualPaymentIndicator <CtrctlPmtInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 205 to 205.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 205

```text
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
3.4.11.25.2  ContractualPaymentIndicator <CtrctlPmtInd>
Presence: [0..1]
Definition: Specifies exceptions to contractual payment service.
Datatype: "Payment2Code" on page 1227
CodeName Name Definition
ACTU ActualPayment The cash payment occurs or will occur
upon receipt of proceeds from the issuer.
3.4.11.25.3  NonEligibleProceedsIndicator <NonElgblPrcdsInd>
Presence: [0..1]
Definition: Specifies information regarding outturn resources that cannot be processed by the Central
Securities Depository (CSD). Special delivery instruction is required from the account owner for the
corporate action outcome to be credited.
NonEligibleProceedsIndicator <NonElgblPrcdsInd> contains one of the following
NonEligibleProceedsIndicator5Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 205
Or}   Proprietary <Prtry> [1..1] ± 205
3.4.11.25.3.1  Code <Cd>
Presence: [1..1]
Definition: Standard code to specify information regarding the non eligibility of the outturn resources.
Datatype: "NonEligibleProceedsIndicator2Code" on page 1222
CodeName Name Definition
NELC NonEligibleCurrency Currency not eligible for settlement in the
Central Securities Depository (CSD).
ACLI AccountLimitation Participant's account limitation.
ONEL OtherNonEligibility Other source of non eligibility.
NELS NonEligibleSecurity Security not eligible in the Central
Securities Depository (CSD).
3.4.11.25.3.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Proprietary identification to specify information regarding the non eligibility of the outturn
resources.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 205 February 2026
```

