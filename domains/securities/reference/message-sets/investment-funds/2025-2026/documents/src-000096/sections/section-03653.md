---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.6 PartyIdentification220", "66.1.29.6.1 Identification <Id>", "66.1.29.6.1.4 TaxIdentificationNumber <TaxIdNb>"]
file_pages: [4903]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.6.1.4 TaxIdentificationNumber <TaxIdNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4903 to 4903.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4903

```text
PostalAddress <PstlAdr> contains the following elements (see "PostalAddress21" on page 5101 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  5102
{Or     Code <Cd> [1..1] CodeSet 5103
Or}     Proprietary <Prtry> [1..1] ± 5103
   MailingIndicator <MlngInd> [0..1] Indicator 5103
   RegistrationAddressIndicator <RegnAdrInd> [0..1] Indicator 5103
   CareOf <CareOf> [0..1] Text 5104
   AddressLine <AdrLine> [0..5] Text 5104
   StreetName <StrtNm> [0..1] Text 5104
   BuildingNumber <BldgNb> [0..1] Text 5104
   BuildingName <BldgNm> [0..1] Text 5104
   PostBox <PstBx> [0..1] Text 5104
   SideInBuilding <SdInBldg> [0..1] Text 5104
   Floor <Flr> [0..1] Text 5104
   SuiteIdentification <SuiteId> [0..1] Text 5105
   PostCode <PstCd> [0..1] Text 5105
   DistrictName <DstrctNm> [0..1] Text 5105
   Village <Vllg> [0..1] Text 5105
   TownName <TwnNm> [0..1] Text 5105
   State <Stat> [0..1] Text 5105
   Country <Ctry> [1..1] CodeSet C12 5105
Constraints
• MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
66.1.29.6.1.4  TaxIdentificationNumber <TaxIdNb>
Presence: [1..1]
Definition: Number assigned by a tax authority to an entity.
Datatype: "Max35Text" on page 5403
66.1.29.6.1.5  NationalRegistrationNumber <NtlRegnNb>
Presence: [1..1]
Definition: Number assigned by a national registration authority to an entity.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4903 May 2026
```

