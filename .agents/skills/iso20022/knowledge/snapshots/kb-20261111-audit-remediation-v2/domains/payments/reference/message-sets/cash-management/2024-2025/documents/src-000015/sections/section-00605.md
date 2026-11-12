---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["36 camt.104.001.01 CreateMemberV01", "36.4 Message Building Blocks", "36.4.3 ValueSet <ValSet>", "36.4.3.3 CommunicationAddress <ComAdr>"]
file_pages: [781, 782]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.104.001.01"]
---

# 36.4.3.3 CommunicationAddress <ComAdr>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 781 to 782.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 781

```text
36.4.3.3  CommunicationAddress <ComAdr>
Presence: [0..1]
Definition: Number, or virtual address, used for communication.
CommunicationAddress <ComAdr> contains the following CommunicationAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostalAddress <PstlAdr> [1..1] ± 781
   PhoneNumber <PhneNb> [1..1] Text 781
   FaxNumber <FaxNb> [0..1] Text 781
   EmailAddress <EmailAdr> [0..1] Text 781
36.4.3.3.1  PostalAddress <PstlAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains one of the following elements (see "LongPostalAddress1Choice"
on page 839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 840
Or}   Structured <Strd> [1..1] ± C3 840
36.4.3.3.2  PhoneNumber <PhneNb>
Presence: [1..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
36.4.3.3.3  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
36.4.3.3.4  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max256Text" on page 889
36.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 781 February 2025
```

## File page 782

```text
Impacted by: C4 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 782 February 2025
```

