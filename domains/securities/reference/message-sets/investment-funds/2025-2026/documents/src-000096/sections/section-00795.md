---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.22 PaymentDetails <PmtDtls>", "35.4.14.10.22.2 CreditTransferDetails <CdtTrfDtls>", "35.4.14.10.22.2.7 IntermediaryAgent2 <IntrmyAgt2>", "35.4.14.10.22.2.7.3 NameAndAddress <NmAndAdr>"]
file_pages: [1083]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.22.2.7.3 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1083 to 1083.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1083

```text
ClearingSystemMemberIdentification <ClrSysMmbId> contains one of the following elements (see
"ClearingSystemMemberIdentification4Choice" on page 4454 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CHIPSUniversalIdentification <USCHU> [1..1] IdentifierSet 4454
Or   NewZealandNCCIdentification <NZNCC> [1..1] IdentifierSet 4455
Or   IrishNSCIdentification <IENSC> [1..1] IdentifierSet 4455
Or   UKDomesticSortCode <GBSC> [1..1] IdentifierSet 4455
Or   CHIPSParticipantIdentification <USCH> [1..1] IdentifierSet 4455
Or   SwissBCIdentification <CHBC> [1..1] IdentifierSet 4455
Or   FedwireRoutingNumberIdentification <USFW> [1..1] IdentifierSet 4455
Or   PortugueseNCCIdentification <PTNCC> [1..1] IdentifierSet 4455
Or   RussianCentralBankIdentificationCode <RUCB> [1..1] IdentifierSet 4456
Or   ItalianDomesticIdentificationCode <ITNCC> [1..1] IdentifierSet 4456
Or   AustrianBankleitzahlIdentification <ATBLZ> [1..1] IdentifierSet 4456
Or   CanadianPaymentsAssociationRoutingNumberIdentificati
on <CACPA>
[1..1] IdentifierSet 4456
Or   SwissSICIdentification <CHSIC> [1..1] IdentifierSet 4456
Or   GermanBankleitzahlIdentification <DEBLZ> [1..1] IdentifierSet 4456
Or   SpanishDomesticInterbankingIdentification <ESNCC> [1..1] IdentifierSet 4456
Or   SouthAfricanNCCIdentification <ZANCC> [1..1] IdentifierSet 4457
Or   HongKongBankCode <HKNCC> [1..1] IdentifierSet 4457
Or   AustralianExtensiveBranchNetworkIdentification
<AUBSBx>
[1..1] IdentifierSet 4457
Or}   AustralianSmallNetworkIdentification <AUBSBs> [1..1] IdentifierSet 4457
35.4.14.10.22.2.7.3  NameAndAddress <NmAndAdr>
Presence: [0..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
35.4.14.10.22.2.7.4  LEI <LEI>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1083 May 2026
```

