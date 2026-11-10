---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.13 BulkCashSettlementDetails <BlkCshSttlmDtls>", "49.4.5.13.1 PaymentInstrument <PmtInstrm>", "49.4.5.13.1.5 BankersDraftDetails <BkrsDrftDtls>", "49.4.5.13.1.5.3 DraweeIdentification <DrweeId>", "49.4.5.13.1.5.3.1 Party <Pty>", "49.4.5.13.1.5.3.1.4 ProprietaryIdentification <PrtryId>"]
file_pages: [2997]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.13.1.5.3.1.4 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2997 to 2997.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2997

```text
ClearingSystemMemberIdentification <ClrSysMmbId> contains one of the following elements (see
"ClearingSystemMemberIdentification2Choice" on page 4457 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CHIPSUniversalIdentification <USCHU> [1..1] IdentifierSet 4458
Or   NewZealandNCCIdentification <NZNCC> [1..1] IdentifierSet 4458
Or   IrishNSCIdentification <IENSC> [1..1] IdentifierSet 4459
Or   UKDomesticSortCode <GBSC> [1..1] IdentifierSet 4459
Or   CHIPSParticipantIdentification <USCH> [1..1] IdentifierSet 4459
Or   SwissBCIdentification <CHBC> [1..1] IdentifierSet 4459
Or   FedwireRoutingNumberIdentification <USFW> [1..1] IdentifierSet 4459
Or   PortugueseNCCIdentification <PTNCC> [1..1] IdentifierSet 4459
Or   RussianCentralBankIdentificationCode <RUCB> [1..1] IdentifierSet 4459
Or   ItalianDomesticIdentificationCode <ITNCC> [1..1] IdentifierSet 4460
Or   AustrianBankleitzahlIdentification <ATBLZ> [1..1] IdentifierSet 4460
Or   CanadianPaymentsAssociationRoutingNumberIdentificati
on <CACPA>
[1..1] IdentifierSet 4460
Or   SwissSICIdentification <CHSIC> [1..1] IdentifierSet 4460
Or   GermanBankleitzahlIdentification <DEBLZ> [1..1] IdentifierSet 4460
Or   SpanishDomesticInterbankingIdentification <ESNCC> [1..1] IdentifierSet 4460
Or   SouthAfricanNCCIdentification <ZANCC> [1..1] IdentifierSet 4460
Or   HongKongBankCode <HKNCC> [1..1] IdentifierSet 4461
Or   AustralianExtensiveBranchNetworkIdentification
<AUBSBx>
[1..1] IdentifierSet 4461
Or   AustralianSmallNetworkIdentification <AUBSBs> [1..1] IdentifierSet 4461
Or   IndianFinancialSystemCode <INIFSC> [1..1] IdentifierSet 4461
Or   HellenicBankIdentificationCode <GRHEBIC> [1..1] IdentifierSet 4461
Or   PolishNationalClearingCode <PLKNR> [1..1] IdentifierSet 4461
Or}   OtherClearingCodeIdentification <OthrClrCdId> [1..1] Text 4462
49.4.5.13.1.5.3.1.4  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Datatype: "Max35Text" on page 5403
49.4.5.13.1.5.3.2  LEI <LEI>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2997 May 2026
```

