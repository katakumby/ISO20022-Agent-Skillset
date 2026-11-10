---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.14 Miscellaneous", "9.1.14.13 RestrictionIdentification1", "9.1.14.13.2 Identification <Id>"]
file_pages: [243]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.14.13.2 Identification <Id>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 243 to 243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 243

```text
9.1.14.13.2  Identification <Id>
Presence: [1..1]
Definition: Restriction identification applied on the transaction.
Datatype: "Max35Text" on page 345
9.1.14.14  YieldedOrValueType1Choice
Definition: Choice of value type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 243
Or}   ValueType <ValTp> [1..1] CodeSet 243
9.1.14.14.1  Yielded <Yldd>
Presence: [1..1]
Definition: Indicates whether the price is expressed as a yield.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 342):
• Meaning When True: Yes
• Meaning When False: No
9.1.14.14.2  ValueType <ValTp>
Presence: [1..1]
Definition: Type of value in which the price is expressed.
Datatype: "PriceValueType1Code" on page 333
CodeName Name Definition
DISC Discount Price expressed as a number of
percentage points below par, for
example, a discount price of 2.0%
equals a price of 98 when par is 100.
PREM Premium Price expressed as a number of
percentage points above par, for
example, a premium price of 2.0%
equals a price of 102 when par is 100.
PARV Par Price is the face amount.
9.1.14.15  HoldIndicator6
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Indicator <Ind> [1..1] Indicator 244
   Reason <Rsn> [0..*] ± 244
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 243 September 2025
```

