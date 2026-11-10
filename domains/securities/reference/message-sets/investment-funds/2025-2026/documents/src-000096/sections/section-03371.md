---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.7 InvestmentAccountOwnershipInformation16", "66.1.24.7.28 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [4614]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.7.28 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4614 to 4614.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4614

```text
PrimaryCommunicationAddress <PmryComAdr> contains the following elements (see
"CommunicationAddress6" on page 4340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  4341
{Or     Code <Cd> [1..1] CodeSet 4341
Or}     Proprietary <Prtry> [1..1] ± 4341
   Email <Email> [0..1] Text 4342
   Phone <Phne> [0..1] Text 4342
   Mobile <Mob> [0..1] Text 4342
   FaxNumber <FaxNb> [0..1] Text 4342
   TelexAddress <TlxAdr> [0..1] Text 4342
   URLAddress <URLAdr> [0..1] Text 4342
66.1.24.7.28  SecondaryCommunicationAddress <ScndryComAdr>
Presence: [0..*]
Definition: Communication device number or electronic address used for communication.
SecondaryCommunicationAddress <ScndryComAdr> contains the following elements (see
"CommunicationAddress6" on page 4340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  4341
{Or     Code <Cd> [1..1] CodeSet 4341
Or}     Proprietary <Prtry> [1..1] ± 4341
   Email <Email> [0..1] Text 4342
   Phone <Phne> [0..1] Text 4342
   Mobile <Mob> [0..1] Text 4342
   FaxNumber <FaxNb> [0..1] Text 4342
   TelexAddress <TlxAdr> [0..1] Text 4342
   URLAddress <URLAdr> [0..1] Text 4342
66.1.24.7.29  AdditionalRegulatoryInformation <AddtlRgltryInf>
Presence: [0..1]
Definition: Additional regulatory information about the investor or account owner that is required in some
markets to support anti-money laundering laws.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4614 May 2026
```

