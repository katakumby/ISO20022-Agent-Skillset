---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.12 Rate", "22.1.12.6 FloatingInterestRate6", "22.1.12.6.2 Term <Term>"]
file_pages: [363]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.12.6.2 Term <Term>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 363 to 363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
ReferenceRate <RefRate> contains one of the following elements (see
"BenchmarkCurveName6Choice" on page 356 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ISIN <ISIN> [1..1] IdentifierSet 356
Or   Index <Indx> [1..1] CodeSet 356
Or}   Name <Nm> [1..1] Text 358
22.1.12.6.2  Term <Term>
Presence: [1..1]
Definition: Term of the index/benchmark of a floating rate bond. The term shall be expressed in days,
weeks, months or years.
Term <Term> contains the following elements (see "InterestRateContractTerm2" on page 358 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [1..1] CodeSet 358
   Value <Val> [1..1] Quantity C7 359
22.1.12.6.3  BasisPointSpread <BsisPtSprd>
Presence: [1..1]
Definition: Number of basis points above (if positive) or below (if negative) the underlying reference rate
to calculate the actual interest rate applicable for a given period at issuance of the floating rate
instrument.
Usage:
Used to express differences in interest rates, for example, a difference of 0.10% is equivalent to a
change of 10 basis points.
Impacted by: C8 "NumberRule"
Datatype: "Max5Number" on page 453
Constraints
• NumberRule
If Number is negative, then Sign must be present.
22.1.12.7  FloatingInterestRate8
Definition: Provides the index used to define the rate and optionally the basis point spread.
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
363 July 2025
```

