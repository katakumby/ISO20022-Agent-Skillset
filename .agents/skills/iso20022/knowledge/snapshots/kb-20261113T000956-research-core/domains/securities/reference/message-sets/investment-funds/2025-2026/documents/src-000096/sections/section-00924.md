---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.26 PaymentDetails <PmtDtls>", "36.4.15.11.26.2 CreditTransferDetails <CdtTrfDtls>", "36.4.15.11.26.2.3 DebtorAgent <DbtrAgt>", "36.4.15.11.26.2.3.3 NameAndAddress <NmAndAdr>"]
file_pages: [1271]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.26.2.3.3 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1271 to 1271.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1271

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
36.4.15.11.26.2.3.3  NameAndAddress <NmAndAdr>
Presence: [0..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
36.4.15.11.26.2.3.4  LEI <LEI>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1271 May 2026
```

