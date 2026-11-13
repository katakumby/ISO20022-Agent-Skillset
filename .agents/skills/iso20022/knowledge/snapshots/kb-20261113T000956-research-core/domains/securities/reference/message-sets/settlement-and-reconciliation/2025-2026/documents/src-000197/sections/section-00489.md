---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>", "22.4.9.4 TerminationDate <TermntnDt>"]
file_pages: [750]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.9.4 TerminationDate <TermntnDt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 750 to 750.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 750

```text
22.4.9.4  TerminationDate <TermntnDt>
Presence: [0..1]
Definition: Closing date/time or maturity date/time of the transaction.
TerminationDate <TermntnDt> contains one of the following elements (see "TerminationDate6Choice"
on page 1436 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1437
Or}   Code <Cd> [1..1]  1437
{Or     Code <Cd> [1..1] CodeSet 1437
Or}     Proprietary <Prtry> [1..1] ± 1437
22.4.9.5  RateType <RateTp>
Presence: [0..1]
Definition: Specifies whether the rate is fixed or variable.
RateType <RateTp> contains one of the following elements (see "RateType35Choice" on page 1747
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1748
Or}   Proprietary <Prtry> [1..1] ± 1748
22.4.9.6  LegalFramework <LglFrmwk>
Presence: [0..1]
Definition: Legal framework of the transaction.
LegalFramework <LglFrmwk> contains one of the following elements (see "LegalFramework3Choice"
on page 1622 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1622
Or}   Proprietary <Prtry> [1..1] ± 1623
22.4.9.7  MaturityDateModification <MtrtyDtMod>
Presence: [0..1]
Definition: Indicates whether the maturity date of the securities financing transaction may be modified.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 750 March 2026
```

