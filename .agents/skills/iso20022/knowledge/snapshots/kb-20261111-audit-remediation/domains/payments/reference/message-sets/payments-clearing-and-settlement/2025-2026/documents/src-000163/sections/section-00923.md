---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.17 Regulatory Reporting", "10.1.17.1 RegulatoryReporting10", "10.1.17.1.2 Authority <Authrty>", "10.1.17.1.2.1 Name <Nm>"]
file_pages: [1218]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.17.1.2.1 Name <Nm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1218 to 1218.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1218

```text
10.1.17.1.2.1  Name <Nm>
Presence: [0..1]
Definition: Name of the entity requiring the regulatory reporting information.
Datatype: "Max140Text" on page 1244
10.1.17.1.2.2  Country <Ctry>
Presence: [0..1]
Definition: Country of the entity that requires the regulatory reporting information.
Impacted by: C10 "Country"
Datatype: "CountryCode" on page 1226
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
10.1.17.1.3  Details <Dtls>
Presence: [0..*]
Definition: Set of elements used to provide details on the regulatory reporting information.
Impacted by: C40 "ReportingCodeAndInformationRule"
Details <Dtls> contains the following StructuredRegulatoryReporting5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1]  1219
{Or     Code <Cd> [1..1] CodeSet 1219
Or}     Proprietary <Prtry> [1..1] Text 1219
   Date <Dt> [0..1] Date 1219
   Country <Ctry> [0..1] CodeSet C10 1219
   ReportingCode <RptgCd> [0..1] Text 1219
   Amount <Amt> [0..1] Amount C2, C12 1220
   Information <Inf> [0..*] Text 1220
Constraints
• ReportingCodeAndInformationRule
Reporting code or information must be present. Both may be present.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1218 March 2026
```

