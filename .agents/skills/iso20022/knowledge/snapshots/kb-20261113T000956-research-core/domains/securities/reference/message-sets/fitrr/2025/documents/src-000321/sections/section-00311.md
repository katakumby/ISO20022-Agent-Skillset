---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.12 Rate", "22.1.12.5 InterestRate8Choice"]
file_pages: [362]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.12.5 InterestRate8Choice

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 362 to 362.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 362

```text
Datatype: "Max25Text" on page 455
22.1.12.5  InterestRate8Choice
Definition: Choice between a fixed rate and a variable rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Fixed <Fxd> [1..1] Rate 362
Or}   Floating <Fltg> [1..1] ± 362
22.1.12.5.1  Fixed <Fxd>
Presence: [1..1]
Definition: Interest Rate is fixed.
Datatype: "PercentageRate" on page 454
22.1.12.5.2  Floating <Fltg>
Presence: [1..1]
Definition: Interest rate is a variable / floating rate, based on an index.
Floating <Fltg> contains the following elements (see "FloatingInterestRate8" on page 363 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceRate <RefRate> [1..1] ± 364
   Term <Term> [0..1] ± 364
22.1.12.6  FloatingInterestRate6
Definition: Provides the index used to define the rate and the basis point spread.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceRate <RefRate> [1..1] ± 362
   Term <Term> [1..1] ± 363
   BasisPointSpread <BsisPtSprd> [1..1] Quantity C8 363
22.1.12.6.1  ReferenceRate <RefRate>
Presence: [1..1]
Definition: Identifies the reference index for the debt instrument.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
362 July 2025
```

