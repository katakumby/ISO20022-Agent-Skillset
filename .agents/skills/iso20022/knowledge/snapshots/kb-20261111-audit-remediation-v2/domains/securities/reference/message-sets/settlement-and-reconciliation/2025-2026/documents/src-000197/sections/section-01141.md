---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.49 TradeOriginator3Choice", "35.1.16.49.2 Proprietary <Prtry>"]
file_pages: [1588]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.49.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1588 to 1588.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1588

```text
CodeName Name Definition
INVE Investor Party, either an individual or
organisation, whose assets are being
invested.
TAGT TransfertAgent Party appointed by the fund
management company. It updates
records of investor accounts to reflect
the daily investor purchases,
redemptions, switches, transfers, and re-
registrations. It ensures the timely
settlement of transactions, and may
provide tax information to the investor
and/or to its intermediaries. It may
calculate, collect, and rebate
commissions. It prepares and distributes
confirmations reflecting transactions,
resulting in unit or cash account
movements to the investor or the
investor's intermediary. It responds to
inquiries concerning account status, and
processes the income distribution.
35.1.16.49.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trading party capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.50  ModificationCancellationAllowed4Choice
Definition: Choice of format for the modification cancellation information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1588
Or}   Proprietary <Prtry> [1..1] ± 1589
35.1.16.50.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether a third party is allowed to modify or cancel the transaction.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1588 March 2026
```

