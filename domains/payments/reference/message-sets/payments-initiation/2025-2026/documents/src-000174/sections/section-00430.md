---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.17 Regulatory Reporting", "6.1.17.1 RegulatoryReporting10", "6.1.17.1.3 Details <Dtls>", "6.1.17.1.3.1 Type <Tp>"]
file_pages: [581]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.17.1.3.1 Type <Tp>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 581 to 581.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 581

```text
Constraints
• ReportingCodeAndInformationRule
Reporting code or information must be present. Both may be present.
Following Must be True
    /ReportingCode Must be present
 Or    /Information[*] Must be present
6.1.17.1.3.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of the information supplied in the regulatory reporting details.
Type <Tp> contains one of the following RegulatoryReportingType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 581
Or}   Proprietary <Prtry> [1..1] Text 581
6.1.17.1.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of regulatory reporting, in a coded form.
Datatype: "ExternalRegulatoryReportingType1Code" on page 597
6.1.17.1.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of regulatory reporting, in a proprietary form.
Datatype: "Max35Text" on page 609
6.1.17.1.3.2  Date <Dt>
Presence: [0..1]
Definition: Date related to the specified type of regulatory reporting details.
Datatype: "ISODate" on page 603
6.1.17.1.3.3  Country <Ctry>
Presence: [0..1]
Definition: Country related to the specified type of regulatory reporting details.
Impacted by: C18 "Country"
Datatype: "CountryCode" on page 590
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 581 March 2026
```

