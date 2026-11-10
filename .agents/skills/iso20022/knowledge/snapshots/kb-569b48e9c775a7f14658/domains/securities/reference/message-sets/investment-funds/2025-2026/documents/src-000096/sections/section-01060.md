---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>", "39.4.15.3 Portfolio <Prtfl>", "39.4.15.3.3 Pension <Pnsn>", "39.4.15.3.3.7 AdditionalInformation <AddtlInf>"]
file_pages: [1465, 1466, 1467]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.15.3.3.7 AdditionalInformation <AddtlInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1465 to 1467.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1465

```text
Definition: Indicates that the transfer is only in relation to underlying assets, and that the wrapper
transfer will occur separately.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
39.4.15.3.3.7  AdditionalInformation <AddtlInf>
Presence: [0..*]
Definition: Additional information about the pension policy, plan or scheme.
AdditionalInformation <AddtlInf> contains the following elements (see "AdditionalInformation15" on
page 4508 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InformationType <InfTp> [1..1] ± 4508
   InformationValue <InfVal> [1..1] Text 4508
39.4.15.4  FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>
Presence: [0..*]
Definition: Asset to be transferred.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1465 May 2026
```

## File page 1466

```text
FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf> contains the following
FinancialInstrument111 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LineIdentification <LineId> [0..1] Text 1468
   Instrument <Instrm> [1..1]  1468
{Or     Security <Scty> [1..1]  C13 1469
       Identification <Id> [1..1]  1470
{Or         ISIN <ISIN> [1..1] IdentifierSet 1471
Or         SEDOL <SEDOL> [1..1] IdentifierSet 1471
Or         CUSIP <CUSIP> [1..1] IdentifierSet 1472
Or         RIC <RIC> [1..1] IdentifierSet 1472
Or         TickerSymbol <TckrSymb> [1..1] IdentifierSet 1472
Or         Bloomberg <Blmbrg> [1..1] IdentifierSet 1472
Or         CTA <CTA> [1..1] IdentifierSet 1472
Or         QUICK <QUICK> [1..1] IdentifierSet 1472
Or         Wertpapier <Wrtppr> [1..1] IdentifierSet 1472
Or         Dutch <Dtch> [1..1] IdentifierSet 1473
Or         Valoren <Vlrn> [1..1] IdentifierSet 1473
Or         Sicovam <SCVM> [1..1] IdentifierSet 1473
Or         Belgian <Belgn> [1..1] IdentifierSet 1473
Or         Common <Cmon> [1..1] IdentifierSet 1473
Or         DTI <DTI> [1..1] IdentifierSet 1473
Or}         OtherProprietaryIdentification <OthrPrtryId> [1..1]  1473
           Identification <Id> [1..1] Text 1474
           IdentificationSource <IdSrc> [1..1] ± 1474
       Name <Nm> [0..1] Text 1474
       ShortName <ShrtNm> [0..1] Text 1474
       ClassificationType <ClssfctnTp> [0..1] ± 1474
Or     CashAsset <CshAsst> [1..1] ± 1474
Or}     OtherAsset <OthrAsst> [1..1] ± 1475
   ClientReference <ClntRef> [0..1] ± 1475
   CounterpartyReference <CtrPtyRef> [0..1] ± 1475
   TransfereeAccount <TrfeeAcct> [0..1]  1476
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1466 May 2026
```

## File page 1467

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     OwnerIdentification <OwnrId> [0..1] ± 1476
     AccountIdentification <AcctId> [0..1] Text 1477
     Designation <Dsgnt> [0..1] Text 1477
     AccountName <AcctNm> [0..1] Text 1477
     Servicer <Svcr> [0..1] ± 1477
     SubAccountDetails <SubAcctDtls> [0..1] ± 1477
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1478
   Transferor <Trfr> [0..1]  1478
     OwnerIdentification <OwnrId> [0..1] ± 1478
     AccountIdentification <AcctId> [0..1] Text 1479
     Designation <Dsgnt> [0..1] Text 1479
     AccountName <AcctNm> [0..1] Text 1479
     Servicer <Svcr> [0..1] ± 1479
     SubAccountDetails <SubAcctDtls> [0..1] ± 1480
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1480
   SettlementPartiesDetails <SttlmPtiesDtls> [0..1]  1480
     SafekeepingPlace <SfkpgPlc> [0..1] ± 1481
     TradeTransactionCondition <TradTxCond> [0..*] ± 1482
     SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1482
     SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1482
     ReceivingSideDetails <RcvgSdDtls> [0..1]  C6, C11,
C17,
C18,
C19,
C20,
C21
1482
       Depository <Dpstry> [0..1] ± 1484
       Party1 <Pty1> [0..1] ± 1485
       Party2 <Pty2> [0..1] ± 1485
       Party3 <Pty3> [0..1] ± 1485
       Party4 <Pty4> [0..1] ± 1486
       Party5 <Pty5> [0..1] ± 1486
   AssetsHeldInOwnName <AsstsHeldInOwnNm> [0..1] Indicator 1487
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1467 May 2026
```

