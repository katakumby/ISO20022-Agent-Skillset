---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.17 Regulatory Reporting", "10.1.17.1 RegulatoryReporting10", "10.1.17.1.3 Details <Dtls>", "10.1.17.1.3.1 Type <Tp>"]
file_pages: [1219]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.17.1.3.1 Type <Tp>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1219 to 1219.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1219

```text
Following Must be True
    /ReportingCode Must be present
 Or    /Information[*] Must be present
10.1.17.1.3.1  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of the information supplied in the regulatory reporting details.
Type <Tp> contains one of the following RegulatoryReportingType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1219
Or}   Proprietary <Prtry> [1..1] Text 1219
10.1.17.1.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of regulatory reporting, in a coded form.
Datatype: "ExternalRegulatoryReportingType1Code" on page 1232
10.1.17.1.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of regulatory reporting, in a proprietary form.
Datatype: "Max35Text" on page 1246
10.1.17.1.3.2  Date <Dt>
Presence: [0..1]
Definition: Date related to the specified type of regulatory reporting details.
Datatype: "ISODate" on page 1239
10.1.17.1.3.3  Country <Ctry>
Presence: [0..1]
Definition: Country related to the specified type of regulatory reporting details.
Impacted by: C10 "Country"
Datatype: "CountryCode" on page 1226
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
10.1.17.1.3.4  ReportingCode <RptgCd>
Presence: [0..1]
Definition: Specifies the nature, purpose, and reason for the transaction to be reported for regulatory
and statutory requirements in a coded form.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1219 March 2026
```

