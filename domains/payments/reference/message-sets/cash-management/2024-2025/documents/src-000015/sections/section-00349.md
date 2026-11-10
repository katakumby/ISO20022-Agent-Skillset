---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.2 MemberOrError <MmbOrErr>", "13.4.2.1.2.1 Member <Mmb>", "13.4.2.1.2.1.7 CommunicationAddress <ComAdr>", "13.4.2.1.2.1.7.1 PostalAddress <PstlAdr>"]
file_pages: [493]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.2.1.7.1 PostalAddress <PstlAdr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 493 to 493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 493

```text
CommunicationAddress <ComAdr> contains the following CommunicationAddress10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostalAddress <PstlAdr> [1..1] ± 493
   PhoneNumber <PhneNb> [1..1] Text 493
   FaxNumber <FaxNb> [0..1] Text 493
   EmailAddress <EmailAdr> [0..1] Text 493
13.4.2.1.2.1.7.1  PostalAddress <PstlAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains one of the following elements (see "LongPostalAddress1Choice"
on page 839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 840
Or}   Structured <Strd> [1..1] ± C3 840
13.4.2.1.2.1.7.2  PhoneNumber <PhneNb>
Presence: [1..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
13.4.2.1.2.1.7.3  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
13.4.2.1.2.1.7.4  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max2048Text" on page 888
13.4.2.1.2.2  BusinessError <BizErr>
Presence: [1..1]
Definition: Reason the requested business information is not given.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 493 February 2025
```

