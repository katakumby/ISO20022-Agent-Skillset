---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Regulatory Reporting", "6.1.17.1 RegulatoryReporting10", "6.1.17.1.2 Authority <Authrty>", "6.1.17.1.2.1 Name <Nm>"]
file_pages: [580]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17.1.2.1 Name <Nm>

Source: [src-000174](../../../../../../../../../evidence/omitted/577241d5215d98d6ed689f57.md). Locator: one-based file pages 580 to 580.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 580

```text
Definition: Entity requiring the regulatory reporting information.
Authority <Authrty> contains the following RegulatoryAuthority2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 580
   Country <Ctry> [0..1] CodeSet C18 580
6.1.17.1.2.1  Name <Nm>
Presence: [0..1]
Definition: Name of the entity requiring the regulatory reporting information.
Datatype: "Max140Text" on page 608
6.1.17.1.2.2  Country <Ctry>
Presence: [0..1]
Definition: Country of the entity that requires the regulatory reporting information.
Impacted by: C18 "Country"
Datatype: "CountryCode" on page 590
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
6.1.17.1.3  Details <Dtls>
Presence: [0..*]
Definition: Set of elements used to provide details on the regulatory reporting information.
Impacted by: C34 "ReportingCodeAndInformationRule"
Details <Dtls> contains the following StructuredRegulatoryReporting5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  581
{Or     Code <Cd> [1..1] CodeSet 581
Or}     Proprietary <Prtry> [1..1] Text 581
   Date <Dt> [0..1] Date 581
   Country <Ctry> [0..1] CodeSet C18 581
   ReportingCode <RptgCd> [0..1] Text 582
   Amount <Amt> [0..1] Amount C2, C19 582
   Information <Inf> [0..*] Text 582
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 580 March 2026
```

