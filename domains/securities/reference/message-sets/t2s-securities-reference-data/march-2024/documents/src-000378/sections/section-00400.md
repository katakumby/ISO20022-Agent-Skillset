---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.12 Postal Address", "13.1.12.2 PostalAddress3", "13.1.12.2.2 MailingIndicator <MlngInd>"]
file_pages: [493]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.12.2.2 MailingIndicator <MlngInd>

Source: [src-000378](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 493 to 493.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 493

```text
CodeName Name Definition
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
13.1.12.2.2  MailingIndicator <MlngInd>
Presence: [1..1]
Definition: Indicates whether mail should be sent to an address.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.12.2.3  RegistrationAddressIndicator <RegnAdrInd>
Presence: [1..1]
Definition: Indicates whether the address is the official address of the party.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.12.2.4  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress4" on
page 496 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 496
   Address <Adr> [1..1] ± 496
13.1.12.3  PostalAddress1
Definition: Information that locates and identifies a specific address, as defined by postal services.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 493 March 2024
```

