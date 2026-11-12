---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.19 PurposeCode9Choice", "7.1.19.19.2 Proprietary <Prtry>"]
file_pages: [309]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.19.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 309 to 309.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 309

```text
Definition: Specifies the type of securities account.
Datatype: "SecuritiesAccountPurposeType1Code" on page 645
CodeName Name Definition
MARG Margin Account is used when financing is done
by the broker.
SHOR ShortSale Account is used for short sale orders.
ABRD Abroad Account is located in a financial
institution outside the country where the
transaction is taking place.
CEND Centralised Account and all its related positions are
held in one location.
DVPA CashDVP Account is used for settlement upon
delivery, or a collection on a delivery
basis.
PHYS Physical Account is used for physical domestic
safekeeping.
7.1.19.19.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the execution priority of the instruction with a proprietary scheme.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.20  Reversible2Choice
Definition: Choice between a code or a data source scheme to determine the closing of the securities
lending contract.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 309
Or}   Proprietary <Prtry> [1..1] ± 310
7.1.19.20.1  Code <Cd>
Presence: [1..1]
Definition: Closing of the securities lending contract is identified using a code.
Datatype: "Reversible1Code" on page 645
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 309 February 2025
```

