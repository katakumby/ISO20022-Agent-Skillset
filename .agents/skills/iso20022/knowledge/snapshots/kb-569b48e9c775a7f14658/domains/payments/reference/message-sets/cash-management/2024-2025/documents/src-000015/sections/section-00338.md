---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["13 camt.014.001.05 ReturnMemberV05", "13.3 Constraints"]
file_pages: [479]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.014.001.05"]
---

# 13.3 Constraints

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 479 to 479.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 479

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
               FaxNumber <FaxNb> [0..1] Text 492
               EmailAddress <EmailAdr> [0..1] Text 492
           CommunicationAddress <ComAdr> [0..1]  492
             PostalAddress <PstlAdr> [1..1] ± 493
             PhoneNumber <PhneNb> [1..1] Text 493
             FaxNumber <FaxNb> [0..1] Text 493
             EmailAddress <EmailAdr> [0..1] Text 493
Or}         BusinessError <BizErr> [1..1] ± 493
Or}     OperationalError <OprlErr> [1..*] ± 494
   SupplementaryData <SplmtryData> [0..*] ± C8 494
13.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C2 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C5 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C6 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C7 StreetNameAndOrPostOfficeBoxRule
If StreetName is not present, then PostOfficeBox is mandatory. If StreetName is present, then
PostOfficeBox is optional.
Approved by the Payments SEG on 04 February 2025 camt.014.001.05 ReturnMemberV05
Cash Management - Maintenance 2024 - 2025 479 February 2025
```

