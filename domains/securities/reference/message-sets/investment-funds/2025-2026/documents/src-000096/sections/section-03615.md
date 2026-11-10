---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.28 Miscellaneous", "66.1.28.27 InsuranceType2Choice", "66.1.28.27.1 Code <Cd>"]
file_pages: [4865]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.28.27.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4865 to 4865.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4865

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4865
Or}   Proprietary <Prtry> [1..1] ± 4865
66.1.28.27.1  Code <Cd>
Presence: [1..1]
Definition: Type of insurance contract expressed as a code.
Datatype: "Insurance1Code" on page 5311
CodeName Name Definition
LIFE LifeInsurance Life insurance.
PDIS PermanentDisabilityInsurance Permanent disability insurance.
66.1.28.27.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of insurance contract expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.28.28  LinkedMessage1Choice
Definition: Reference to a message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PreviousReference <PrvsRef> [1..1] ± 4865
Or   OtherReference <OthrRef> [1..1] ± 4866
Or}   RelatedReference <RltdRef> [1..1] ± 4866
66.1.28.28.1  PreviousReference <PrvsRef>
Presence: [1..1]
Definition: Linked previous reference.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4865 May 2026
```

