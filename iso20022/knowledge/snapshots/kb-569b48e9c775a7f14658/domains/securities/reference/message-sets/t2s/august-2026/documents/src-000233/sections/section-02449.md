---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.2 Message Datatypes", "82.2.2 CodeSet", "82.2.2.78 InterestType3Code"]
file_pages: [3260]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.2.2.78 InterestType3Code

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3260 to 3260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3260

```text
CodeName Name Definition
same as to the 30th calendar day of the
same month. This means that the 31st is
assumed to be the 30th and 28 Feb (or
29 Feb for a leap year) is assumed to be
equivalent to 30 Feb. It is a variation of
the 30E/360 (or Eurobond basis) method
where the last day of February is always
assumed to be the 30th, even if it is the
last day of the maturity coupon period.
A014 Actual365NL Method whereby interest is calculated
based on the actual number of accrued
days in the interest period, excluding any
leap day from the count, and a 365-day
year.
NARR Narrative Other method than A001-A020. See
Narrative.
82.2.2.78  InterestType3Code
Definition: Indicates whether interest rate is fixed, variable or other.
Type: CodeSet
CodeName Name Definition
ZCPN ZeroCoupon Indicates that the type of interest is a
zero coupon.
FIXD Fixed Indicates that the type of interest is fixed.
FLRN FloatingRateNote Indicates that the type of interest is a
floating rate note.
DUAL DualBasis Indicates that the type of interest is a
dual basis.
INDE Index Indicates that the type of interest is
index.
DSCO Discounted Indicates that the type of interest is
discounted.
82.2.2.79  InvestorRestrictionType1Code
Definition: Specifies to whom or what the restriction applies.
Type: CodeSet
CodeName Name Definition
LERE LegalResident Restriction applies to a legal resident.
CITI Citizen Restriction applies to a citizen.
INDV Individual Restriction applies to an individual.
82.2.2.80  InvestorType1Code
Definition: Specifies the type of investor.
Type: CodeSet
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3260 August 2026
```

