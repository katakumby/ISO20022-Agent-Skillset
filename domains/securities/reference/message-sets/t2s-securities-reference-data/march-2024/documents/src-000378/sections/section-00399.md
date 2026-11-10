---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.12 Postal Address", "13.1.12.1 CommunicationAddress3", "13.1.12.1.3 Mobile <Mob>"]
file_pages: [492]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.12.1.3 Mobile <Mob>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 492 to 492.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 492

```text
13.1.12.1.3  Mobile <Mob>
Presence: [0..1]
Definition: Collection of information that identifies a mobile phone number, as defined by telecom
services.
Datatype: "PhoneNumber" on page 535
13.1.12.1.4  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 535
13.1.12.1.5  TelexAddress <TlxAdr>
Presence: [0..1]
Definition: Address for a telex machine.
Datatype: "Max35Text" on page 534
13.1.12.1.6  URLAddress <URLAdr>
Presence: [0..1]
Definition: Address for the Universal Resource Locator (URL), for example an address used over the
www (HTTP) service.
Datatype: "Max256Text" on page 534
13.1.12.2  PostalAddress3
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [1..1] CodeSet 492
   MailingIndicator <MlngInd> [1..1] Indicator 493
   RegistrationAddressIndicator <RegnAdrInd> [1..1] Indicator 493
   NameAndAddress <NmAndAdr> [1..1] ± 493
Constraints
• MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
13.1.12.2.1  AddressType <AdrTp>
Presence: [1..1]
Definition: Type of address.
Datatype: "AddressType1Code" on page 508
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 492 March 2024
```

