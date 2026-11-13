---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.4 Message Building Blocks", "46.4.5 MultipleExecutionDetails <MltplExctnDtls>", "46.4.5.12 BulkCashSettlementDetails <BlkCshSttlmDtls>", "46.4.5.12.1 PaymentInstrument <PmtInstrm>", "46.4.5.12.1.1 CreditTransferDetails <CdtTrfDtls>", "46.4.5.12.1.1.6 IntermediaryAgent1 <IntrmyAgt1>", "46.4.5.12.1.1.6.1 Party <Pty>", "46.4.5.12.1.1.6.1.4 ProprietaryIdentification <PrtryId>"]
file_pages: [2497]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.4.5.12.1.1.6.1.4 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2497 to 2497.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2497

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
46.4.5.12.1.1.6.1.4  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Datatype: "Max35Text" on page 5403
46.4.5.12.1.1.6.2  LEI <LEI>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2497 May 2026
```

