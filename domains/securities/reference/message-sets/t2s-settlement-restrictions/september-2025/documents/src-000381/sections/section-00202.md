---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.14 Miscellaneous", "9.1.14.17 AutomaticBorrowing7Choice", "9.1.14.17.2 Proprietary <Prtry>"]
file_pages: [246]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.14.17.2 Proprietary <Prtry>

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 246 to 246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 246

```text
CodeName Name Definition
RTRN Return Return of stocks should take place.
9.1.14.17.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 224 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 224
   Issuer <Issr> [1..1] Text 224
   SchemeName <SchmeNm> [0..1] Text 224
9.1.14.18  Number22Choice
Definition: Choice number format.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 246
Or}   Long <Lng> [1..1] ± 246
9.1.14.18.1  Short <Shrt>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Exact3NumericText" on page 343
9.1.14.18.2  Long <Lng>
Presence: [1..1]
Definition: Number of maximum 35 text, with the possibility to provide an issuer for the number
identification.
Long <Lng> contains the following elements (see "GenericIdentification1" on page 226 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 226
   SchemeName <SchmeNm> [0..1] Text 226
   Issuer <Issr> [0..1] Text 226
9.1.14.19  InterestComputationMethodFormat4Choice
Definition: Choice between a standard code or proprietary code to specify the type of interest
computation method.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 246 September 2025
```

