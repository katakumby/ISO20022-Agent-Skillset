---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "32.4 Message Building Blocks", "32.4.2.10 QueryInformation <QryInf>", "32.4.2.10.1 QueryType <QryTp>"]
file_pages: [804]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.009.001.09"]
---

# 32.4.2.10.1 QueryType <QryTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 804 to 804.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 804

```text
QueryInformation <QryInf> contains the following AdditionalInformation25 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [0..1] ± 804
   Query <Qry> [1..1] Text 804
   QueryReason <QryRsn> [0..1] Text 804
   RejectionReason <RjctnRsn> [0..1]  804
{Or     Code <Cd> [1..1] CodeSet 805
Or}     Proprietary <Prtry> [1..1] ± 807
32.4.2.10.1  QueryType <QryTp>
Presence: [0..1]
Definition: Type of query.
QueryType <QryTp> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
32.4.2.10.2  Query <Qry>
Presence: [1..1]
Definition: Description of the query.
Datatype: "Max350Text" on page 5403
32.4.2.10.3  QueryReason <QryRsn>
Presence: [0..1]
Definition: Reason for the query.
Datatype: "Max350Text" on page 5403
32.4.2.10.4  RejectionReason <RjctnRsn>
Presence: [0..1]
Definition: Reason the instruction was rejected.
RejectionReason <RjctnRsn> contains one of the following RejectedReason33Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 805
Or}   Proprietary <Prtry> [1..1] ± 807
Approved by the Securities SEG on 27 January 2026 sese.009.001.09
RequestForTransferStatusReportV09
Investment Funds - Maintenance 2025 - 2026 804 May 2026
```

