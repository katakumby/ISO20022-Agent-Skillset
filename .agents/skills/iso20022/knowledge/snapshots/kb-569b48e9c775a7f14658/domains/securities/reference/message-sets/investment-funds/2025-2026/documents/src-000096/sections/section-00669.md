---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.19 PaymentDetails <PmtDtls>", "34.4.4.19.4 CashSettlementDetails <CshSttlmDtls>", "34.4.4.19.4.1 CreditTransferDetails <CdtTrfDtls>", "34.4.4.19.4.1.5 IntermediaryAgent1 <IntrmyAgt1>", "34.4.4.19.4.1.5.3 NameAndAddress <NmAndAdr>"]
file_pages: [910]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.19.4.1.5.3 NameAndAddress <NmAndAdr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 910 to 910.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 910

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
34.4.4.19.4.1.5.3  NameAndAddress <NmAndAdr>
Presence: [0..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
34.4.4.19.4.1.5.4  LEI <LEI>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 910 May 2026
```

