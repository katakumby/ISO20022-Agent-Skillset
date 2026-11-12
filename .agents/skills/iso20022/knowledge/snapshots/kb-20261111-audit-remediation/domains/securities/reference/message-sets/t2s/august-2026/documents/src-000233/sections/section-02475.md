---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.144 SecuritiesPaymentStatus1Code"]
file_pages: [3294]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.144 SecuritiesPaymentStatus1Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3294 to 3294.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3294

```text
CodeName Name Definition
COLA EligibleForCollateralPurposes Balance of securities that are eligible for
use for collateral purposes.
OTHR Unclassified Other. See Narrative.
CLEN TaxExempt Tax-exempt financial instruments are to
be settled.
DIRT NonTaxExempt Taxable financial instruments are to be
settled.
NOMI Registered Balance of financial instruments that are
registered (in nominee name or in the
name of the beneficial owner).
SPOS StreetPosition Balance of financial instruments that
remain registered in the name of the
prior beneficial owner.
UNRG Unregistered Balance of securities that could not be
registered due to foreign ownership
limitation.
ISSU Issued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has been received.
QUAS QuasiIssued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has not yet been
received.
82.2.2.144  SecuritiesPaymentStatus1Code
Definition: Specifies the state of payment of a security at a particular time.
Type: CodeSet
CodeName Name Definition
FULL FullyPaid Security is fully paid.
NILL NillPaid Security is nill paid.
PART PartiallyPaid Security is partially paid.
82.2.2.145  SecuritiesSettlementStatus1Code
Definition: Provides the status of settlement of an instruction.
Type: CodeSet
CodeName Name Definition
PEND Pending Instruction is pending. Settlement at the
instructed settlement date is still
possible.
PENF Failing Instruction is failing. Settlement at the
instructed settlement date is no longer
possible.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3294 August 2026
```

