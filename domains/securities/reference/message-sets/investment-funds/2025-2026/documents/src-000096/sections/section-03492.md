---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.26 InvestmentFundOrder", "66.1.26.9 PensionOrder1", "66.1.26.9.1 Type <Tp>"]
file_pages: [4742]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.26.9.1 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4742 to 4742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4742

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  4742
{Or     Code <Cd> [1..1] CodeSet 4742
Or}     Proprietary <Prtry> [1..1] ± 4742
   AdditionalInformation <AddtlInf> [0..*] ± 4743
66.1.26.9.1  Type <Tp>
Presence: [1..1]
Definition: Order attached to the pension policy, plan or scheme.
Type <Tp> contains one of the following PensionOrderType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4742
Or}   Proprietary <Prtry> [1..1] ± 4742
66.1.26.9.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of order attached to the pension policy, plan or scheme expressed as a code.
Datatype: "PensionOrderType1Code" on page 5339
CodeName Name Definition
EARM Earmark Pension policy, plan or scheme has
been earmarked (set aside.)
SHAR Sharing Sharing order for the pension policy,
plan or scheme has been issued by a
court.
66.1.26.9.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of order attached to the pension policy, plan or scheme expressed as a proprietary
code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4742 May 2026
```

