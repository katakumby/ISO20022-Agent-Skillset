---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.20 Issuance <Issnc>", "27.4.2.3.20.6 IssuerOrganisation <IssrOrg>", "27.4.2.3.20.6.6 RegistrationDate <RegnDt>"]
file_pages: [769]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.20.6.6 RegistrationDate <RegnDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 769 to 769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 769

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
27.4.2.3.20.6.6  RegistrationDate <RegnDt>
Presence: [0..1]
Definition: Date and time at which a given organisation was officially registered.
Datatype: "ISODate" on page 3319
27.4.2.3.20.6.7  TaxIdentificationNumber <TaxIdNb>
Presence: [0..1]
Definition: Number assigned by a tax authority to an entity.
Datatype: "Max35Text" on page 3328
27.4.2.3.20.6.8  NationalRegistrationNumber <NtlRegnNb>
Presence: [0..1]
Definition: Number assigned by a national registration authority to an entity.
Datatype: "Max35Text" on page 3328
27.4.2.3.20.6.9  PostalAddress <PstlAdr>
Presence: [1..5]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Impacted by: C10 "MailingIndicatorRule"
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress3" on page 3099 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [1..1] CodeSet 3099
   MailingIndicator <MlngInd> [1..1] Indicator 3099
   RegistrationAddressIndicator <RegnAdrInd> [1..1] Indicator 3100
   NameAndAddress <NmAndAdr> [1..1] ± 3100
Constraints
• MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
27.4.2.3.20.6.10  PrimaryCommunicationAddress <PmryComAdr>
Presence: [0..1]
Definition: Communication device number or electronic address used for communication.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 769 August 2026
```

