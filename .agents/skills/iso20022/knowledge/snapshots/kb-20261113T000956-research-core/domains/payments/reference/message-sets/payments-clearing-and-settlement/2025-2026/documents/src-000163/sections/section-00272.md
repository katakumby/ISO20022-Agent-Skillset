---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.10 MandateRelatedInformation <MndtRltdInf>", "4.4.3.27.10.1 DirectDebitMandate <DrctDbtMndt>", "4.4.3.27.10.1.9 Reason <Rsn>", "4.4.3.27.10.1.9.1 Code <Cd>"]
file_pages: [390]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.10.1.9.1 Code <Cd>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 390 to 390.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 390

```text
Definition: Reason for the direct debit mandate to allow the user to distinguish between different
mandates for the same creditor.
Reason <Rsn> contains one of the following MandateSetupReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 390
Or}   Proprietary <Prtry> [1..1] Text 390
4.4.3.27.10.1.9.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the mandate setup, as published in an external reason code list.
Datatype: "ExternalMandateSetupReason1Code" on page 1231
4.4.3.27.10.1.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 1246
4.4.3.27.10.1.10  TrackingDays <TrckgDays>
Presence: [0..1]
Definition: Specifies the number of days the direct debit instruction must be tracked.
Datatype: "Exact2NumericText" on page 1243
4.4.3.27.10.2  CreditTransferMandate <CdtTrfMndt>
Presence: [1..1]
Definition: Specific credit transfer mandate data.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
390 March 2026
```

