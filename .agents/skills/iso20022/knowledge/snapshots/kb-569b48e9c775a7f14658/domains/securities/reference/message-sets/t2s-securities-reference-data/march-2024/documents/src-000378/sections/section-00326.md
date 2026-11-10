---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.20 Issuance <Issnc>", "13.1.6.4.20.6 IssuerOrganisation <IssrOrg>", "13.1.6.4.20.6.6 RegistrationDate <RegnDt>"]
file_pages: [419]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.20.6.6 RegistrationDate <RegnDt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 419 to 419.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 419

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.1.6.4.20.6.6  RegistrationDate <RegnDt>
Presence: [0..1]
Definition: Date and time at which a given organisation was officially registered.
Datatype: "ISODate" on page 529
13.1.6.4.20.6.7  TaxIdentificationNumber <TaxIdNb>
Presence: [0..1]
Definition: Number assigned by a tax authority to an entity.
Datatype: "Max35Text" on page 534
13.1.6.4.20.6.8  NationalRegistrationNumber <NtlRegnNb>
Presence: [0..1]
Definition: Number assigned by a national registration authority to an entity.
Datatype: "Max35Text" on page 534
13.1.6.4.20.6.9  PostalAddress <PstlAdr>
Presence: [1..5]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Impacted by: C10 "MailingIndicatorRule"
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress3" on page 492 for
details)
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
13.1.6.4.20.6.10  PrimaryCommunicationAddress <PmryComAdr>
Presence: [0..1]
Definition: Communication device number or electronic address used for communication.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 419 March 2024
```

