---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.49 Transfer"]
file_pages: [5256]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.49 Transfer

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5256 to 5256.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5256

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   Issuer <Issr> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4553
66.1.49 Transfer
66.1.49.1  TransferType2Choice
Definition: Choice of formats for a transfer type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5256
Or}   Proprietary <Prtry> [1..1] ± 5256
Constraints
• SECUGuideline
The code SECU (Asset) is used when a financial instrument such as units of a fund are to be
transferred.
The code SECU is also used when assets such as equities or bonds are to be transferred. The code
SECU is also used for assets such as property, moveable property and other similar types of other
asset.
66.1.49.1.1  Code <Cd>
Presence: [1..1]
Definition: Transfer type expressed as a code.
Datatype: "TransferType4Code" on page 5382
CodeName Name Definition
CASH Cash Transfer as cash.
CONV Conversion ISIN is converted to another ISIN and
then transferred.
EXCL Excluded Asset excluded from transfer.
SECU InSpecie Transfer the security as an asset in
specie, that is, 'in its actual form'.
66.1.49.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Transfer type expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5256 May 2026
```

