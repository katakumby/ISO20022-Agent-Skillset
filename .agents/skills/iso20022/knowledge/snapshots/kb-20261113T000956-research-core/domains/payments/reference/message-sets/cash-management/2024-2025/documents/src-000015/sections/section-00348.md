---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.4 Message Building Blocks", "13.4.2 ReportOrError <RptOrErr>", "13.4.2.1 Report <Rpt>", "13.4.2.1.2 MemberOrError <MmbOrErr>", "13.4.2.1.2.1 Member <Mmb>", "13.4.2.1.2.1.6 ContactReference <CtctRef>", "13.4.2.1.2.1.6.3 CommunicationAddress <ComAdr>"]
file_pages: [492]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.4.2.1.2.1.6.3 CommunicationAddress <ComAdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 492 to 492.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
13.4.2.1.2.1.6.3  CommunicationAddress <ComAdr>
Presence: [1..1]
Definition: Number, or virtual address, used for communication.
CommunicationAddress <ComAdr> contains the following CommunicationAddress10 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostalAddress <PstlAdr> [1..1] ± 492
   PhoneNumber <PhneNb> [1..1] Text 492
   FaxNumber <FaxNb> [0..1] Text 492
   EmailAddress <EmailAdr> [0..1] Text 492
13.4.2.1.2.1.6.3.1  PostalAddress <PstlAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains one of the following elements (see "LongPostalAddress1Choice"
on page 839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 840
Or}   Structured <Strd> [1..1] ± C3 840
13.4.2.1.2.1.6.3.2  PhoneNumber <PhneNb>
Presence: [1..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
13.4.2.1.2.1.6.3.3  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
13.4.2.1.2.1.6.3.4  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max2048Text" on page 888
13.4.2.1.2.1.7  CommunicationAddress <ComAdr>
Presence: [0..1]
Definition: Number, or virtual address, used for communication.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 492 February 2025
```

