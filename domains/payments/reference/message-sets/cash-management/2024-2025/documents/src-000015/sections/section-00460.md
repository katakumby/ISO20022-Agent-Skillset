---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["23 camt.025.001.09 ReceiptV09", "23.4 Message Building Blocks", "23.4.2 ReceiptDetails <RctDtls>", "23.4.2.3 RequestHandling <ReqHdlg>", "23.4.2.3.1 Status <Sts>"]
file_pages: [619]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.025.001.09"]
---

# 23.4.2.3.1 Status <Sts>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 619 to 619.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 619

```text
RequestHandling <ReqHdlg> contains the following RequestHandling4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Status <Sts> [1..1]  619
{Or     Code <Cd> [1..1] CodeSet 619
Or}     Proprietary <Prtry> [1..1] Text 619
   StatusReason <StsRsn> [0..1]  C5 620
     Originator <Orgtr> [0..1] ± 620
     Reason <Rsn> [0..1]  621
{Or       Code <Cd> [1..1] CodeSet 622
Or}       Proprietary <Prtry> [1..1] Text 622
     AdditionalInformation <AddtlInf> [0..*] Text 622
   Description <Desc> [0..1] Text 622
Constraints
• DescriptionRule
If Description is present, then Status/Code is not allowed.
On Condition
    /Status/Code is present
Following Must be True
    /Description Must be absent
23.4.2.3.1  Status <Sts>
Presence: [1..1]
Definition: Specifies the status of the request, for example the result of the schema validation or a
business processing result/error.
Status <Sts> contains one of the following RequestStatus1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 619
Or}   Proprietary <Prtry> [1..1] Text 619
23.4.2.3.1.1  Code <Cd>
Presence: [1..1]
Definition: Request status, as published in an external request status code set.
Datatype: "ExternalRequestStatus1Code" on page 856
23.4.2.3.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Request status, in a proprietary form.
Approved by the Payments SEG on 04 February 2025 camt.025.001.09 ReceiptV09
Cash Management - Maintenance 2024 - 2025 619 February 2025
```

