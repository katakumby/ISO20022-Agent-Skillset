---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "3.4 Message Building Blocks", "3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>", "3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>", "3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>", "3.4.3.7.12.10 MandateRelatedInformation <MndtRltdInf>", "3.4.3.7.12.10.1 DirectDebitMandate <DrctDbtMndt>", "3.4.3.7.12.10.1.9 Reason <Rsn>", "3.4.3.7.12.10.1.9.1 Code <Cd>"]
file_pages: [214]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.002.001.15"]
---

# 3.4.3.7.12.10.1.9.1 Code <Cd>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 214 to 214.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 214

```text
Definition: Reason for the direct debit mandate to allow the user to distinguish between different
mandates for the same creditor.
Reason <Rsn> contains one of the following MandateSetupReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 214
Or}   Proprietary <Prtry> [1..1] Text 214
3.4.3.7.12.10.1.9.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the mandate setup, as published in an external reason code list.
Datatype: "ExternalMandateSetupReason1Code" on page 595
3.4.3.7.12.10.1.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 610
3.4.3.7.12.10.1.10  TrackingDays <TrckgDays>
Presence: [0..1]
Definition: Specifies the number of days the direct debit instruction must be tracked.
Datatype: "Exact2NumericText" on page 607
3.4.3.7.12.10.2  CreditTransferMandate <CdtTrfMndt>
Presence: [1..1]
Definition: Specific credit transfer mandate data.
Approved by the Payments SEG on 12 January 2026 pain.002.001.15
CustomerPaymentStatusReportV15
Payments Initiation - Maintenance 2025 - 2026 214 March 2026
```

