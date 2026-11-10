---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.4 Balance", "9.1.4.2 SecuritiesSubBalanceTypeAndQuantityBreakdown3", "9.1.4.2.1 Type <Tp>"]
file_pages: [200]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.4.2.1 Type <Tp>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 200 to 200.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 200

```text
9.1.4.2.1  Type <Tp>
Presence: [1..1]
Definition: Specifies the securities sub balance type indicator (example restriction type for a market
infrastructure).
Type <Tp> contains one of the following elements (see "SecuritiesBalanceType6Choice" on page 197
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 197
Or}   Proprietary <Prtry> [1..1] ± 199
9.1.4.2.2  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown32" on
page 262 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 263
   LotQuantity <LotQty> [0..1] ± 263
   SecuritiesSubBalanceType <SctiesSubBalTp> [0..1] ± 263
9.1.5 Date Period
9.1.5.1  Period7Choice
Definition: Choice between date and date-time for the specification of a period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 200
Or}   FromDateToDate <FrDtToDt> [1..1] ± 201
9.1.5.1.1  FromDateTimeToDateTime <FrDtTmToDtTm>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 200 September 2025
```

