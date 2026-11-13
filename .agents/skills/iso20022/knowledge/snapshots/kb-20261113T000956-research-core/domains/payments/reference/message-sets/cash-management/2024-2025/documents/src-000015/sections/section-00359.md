---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["14 camt.015.001.04 ModifyMemberV04", "14.4 Message Building Blocks", "14.4.3 NewMemberValueSet <NewMmbValSet>", "14.4.3.2 ContactReference <CtctRef>", "14.4.3.2.3 CommunicationAddress <ComAdr>", "14.4.3.2.3.2 PhoneNumber <PhneNb>"]
file_pages: [503]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.015.001.04"]
---

# 14.4.3.2.3.2 PhoneNumber <PhneNb>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 503 to 503.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 503

```text
14.4.3.2.3.2  PhoneNumber <PhneNb>
Presence: [1..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
14.4.3.2.3.3  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
14.4.3.2.3.4  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max256Text" on page 889
14.4.3.3  CommunicationAddress <ComAdr>
Presence: [0..1]
Definition: Number, or virtual address, used for communication.
CommunicationAddress <ComAdr> contains the following CommunicationAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostalAddress <PstlAdr> [1..1] ± 503
   PhoneNumber <PhneNb> [1..1] Text 503
   FaxNumber <FaxNb> [0..1] Text 504
   EmailAddress <EmailAdr> [0..1] Text 504
14.4.3.3.1  PostalAddress <PstlAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains one of the following elements (see "LongPostalAddress1Choice"
on page 839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 840
Or}   Structured <Strd> [1..1] ± C3 840
14.4.3.3.2  PhoneNumber <PhneNb>
Presence: [1..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 503 February 2025
```

