---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.32 CashSettlementDetails <CshSttlmDtls>", "43.4.5.9.32.1 PaymentInstrument <PmtInstrm>", "43.4.5.9.32.1.1 CreditTransferDetails <CdtTrfDtls>", "43.4.5.9.32.1.1.10 CreditorAgent <CdtrAgt>", "43.4.5.9.32.1.1.10.1 Party <Pty>", "43.4.5.9.32.1.1.10.1.4 ProprietaryIdentification <PrtryId>"]
file_pages: [2022]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.32.1.1.10.1.4 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2022 to 2022.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2022

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
43.4.5.9.32.1.1.10.1.4  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
Datatype: "Max35Text" on page 5403
43.4.5.9.32.1.1.10.2  LEI <LEI>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2022 May 2026
```

