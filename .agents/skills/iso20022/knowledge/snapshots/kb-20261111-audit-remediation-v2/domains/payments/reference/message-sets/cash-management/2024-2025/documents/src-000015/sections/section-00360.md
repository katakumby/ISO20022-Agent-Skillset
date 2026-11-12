---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["14 camt.015.001.04 ModifyMemberV04", "14.4 Message Building Blocks", "14.4.3 NewMemberValueSet <NewMmbValSet>", "14.4.3.3 CommunicationAddress <ComAdr>", "14.4.3.3.3 FaxNumber <FaxNb>"]
file_pages: [504]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.015.001.04"]
---

# 14.4.3.3.3 FaxNumber <FaxNb>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 504 to 504.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 504

```text
14.4.3.3.3  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
14.4.3.3.4  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max256Text" on page 889
14.4.4 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C5 "SupplementaryDataRule"
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
Approved by the Payments SEG on 04 February 2025 camt.015.001.04 ModifyMemberV04
Cash Management - Maintenance 2024 - 2025 504 February 2025
```

