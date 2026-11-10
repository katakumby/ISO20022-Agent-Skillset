---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.5 SecuritiesBalanceType7Choice", "82.1.5.5.2 Proprietary <Prtry>"]
file_pages: [2853]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.5.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2853 to 2853.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2853

```text
82.1.5.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Sub-balance expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.5.6  SubBalanceType12Choice
Definition: Choice of format for the sub-balance.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2853
Or}   Proprietary <Prtry> [1..1] ± 2854
82.1.5.6.1  Code <Cd>
Presence: [1..1]
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Datatype: "SecuritiesBalanceType7Code" on page 3293
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2853 August 2026
```

