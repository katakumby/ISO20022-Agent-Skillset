---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["36 camt.104.001.01 CreateMemberV01", "36.4 Message Building Blocks", "36.4.3 ValueSet <ValSet>", "36.4.3.2 ContactReference <CtctRef>", "36.4.3.2.3 CommunicationAddress <ComAdr>"]
file_pages: [780]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.104.001.01"]
---

# 36.4.3.2.3 CommunicationAddress <ComAdr>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 780 to 780.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 780

```text
CodeName Name Definition
STMG SettlementManager Party in a financial institution responsible
for the management of settlement
processing.
36.4.3.2.3  CommunicationAddress <ComAdr>
Presence: [1..1]
Definition: Number, or virtual address, used for communication.
CommunicationAddress <ComAdr> contains the following CommunicationAddress8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostalAddress <PstlAdr> [1..1] ± 780
   PhoneNumber <PhneNb> [1..1] Text 780
   FaxNumber <FaxNb> [0..1] Text 780
   EmailAddress <EmailAdr> [0..1] Text 780
36.4.3.2.3.1  PostalAddress <PstlAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
PostalAddress <PstlAdr> contains one of the following elements (see "LongPostalAddress1Choice"
on page 839 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 840
Or}   Structured <Strd> [1..1] ± C3 840
36.4.3.2.3.2  PhoneNumber <PhneNb>
Presence: [1..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
36.4.3.2.3.3  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 890
36.4.3.2.3.4  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max256Text" on page 889
Approved by the Payments SEG on 04 February 2025 camt.104.001.01 CreateMemberV01
Cash Management - Maintenance 2024 - 2025 780 February 2025
```

