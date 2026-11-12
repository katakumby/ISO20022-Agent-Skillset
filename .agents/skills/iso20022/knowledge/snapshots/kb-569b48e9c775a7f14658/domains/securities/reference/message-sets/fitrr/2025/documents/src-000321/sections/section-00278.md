---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.5 Financial Instrument", "22.1.5.6 FinancialInstrument53"]
file_pages: [328]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.5.6 FinancialInstrument53

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 328 to 328.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 328

```text
22.1.5.6  FinancialInstrument53
Definition: Specify the ISIN(s) and / or LEI(s) that are present in a basket.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..*] IdentifierSet 328
   LEI <LEI> [0..*] IdentifierSet 328
Constraints
• BasketInstrumentUniquenessRule
Where an underlying instrument basket is populated, all ISINs or LEIs must be unique.
• OneElementPresentRule
At least one of 5 elements must be present.
Following Must be True
    /ISIN[*] Must be present
 Or    /LEI[*] Must be present
22.1.5.6.1  ISIN <ISIN>
Presence: [0..*]
Definition: Identifies the financial instrument using an ISIN.
Datatype: "ISINOct2015Identifier" on page 450
22.1.5.6.2  LEI <LEI>
Presence: [0..*]
Definition: The LEI code of the issuer where the instrument is referring to an issuer rather than one
single instrument.
Datatype: "LEIIdentifier" on page 451
22.1.5.7  FinancialInstrument58
Definition: Specifies underlying instruments or index a derivative has.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 328
   Name <Nm> [1..1] ± 328
22.1.5.7.1  ISIN <ISIN>
Presence: [0..1]
Definition: Identification of the index on which the financial instrument is based.
Datatype: "ISINOct2015Identifier" on page 450
22.1.5.7.2  Name <Nm>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
328 July 2025
```

