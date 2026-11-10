---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.41 CRSStatus4", "66.1.30.41.2 Source <Src>", "66.1.30.41.2.1 Code <Cd>"]
file_pages: [5037]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.41.2.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5037 to 5037.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5037

```text
Source <Src> contains one of the following CRSSource1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5037
Or}   Proprietary <Prtry> [1..1] ± 5037
66.1.30.41.2.1  Code <Cd>
Presence: [1..1]
Definition: Source of the Common Reporting Standard (CRS) status expressed as a code.
Datatype: "CRSSourceStatus1Code" on page 5292
CodeName Name Definition
CALC Calculated Source of the Common Reporting
Standard (CRS) status is calculated.
DECL Declared Source of the Common Reporting
Standard (CRS) status is as declared by
the investor.
66.1.30.41.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Source of Common Reporting Standard (CRS) status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.41.3  ExceptionalReportingCountry <XcptnlRptgCtry>
Presence: [0..1]
Definition: Reporting country for the CRS status when there is an exception at the country level.
Impacted by: C12 "Country"
Datatype: "CountryCode" on page 5290
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.30.42  PartyRole2Choice
Definition: Choice of formats for the specification of the role.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5037 May 2026
```

