---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks", "10.4.3 BuyInDetails <BuyInDtls>", "10.4.3.6 RequiredCashCompensation <ReqrdCshCompstn>", "10.4.3.6.3 ValueDate <ValDt>"]
file_pages: [303, 304]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.4.3.6.3 ValueDate <ValDt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 303 to 304.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 303

```text
Fees <Fees> contains the following elements (see AmountAndDirection20 on page 378 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
378
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 379
10.4.3.6.3  ValueDate <ValDt>
Presence: [0..1]
Definition: Indicates the value date of the cash compensation.
Datatype: ISODate on page 487
10.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>
Presence: [0..1]
Definition: Provides details about the original settlement obligation that did not settle and for which the
buy in process will be launched.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 303
```

## File page 304

```text
OriginalSettlementObligation <OrgnlSttlmOblgtn> contains the following SettlementObligation7
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CSDTransactionIdentification <CSDTxId> [0..1] Text 305
   CentralCounterpartyTransactionIdentification
<CntrlCtrPtyTxId>
[0..1] Text 305
   PreviousBuyInIdentification <PrvsBuyInId> [0..1] Text 305
   DeliveryAccount <DlvryAcct> [0..1] ± 305
   SafekeepingPlace <SfkpgPlc> [0..1]  305
{Or     Identification <Id> [1..1]  306
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 306
       Identification <Id> [0..1] Text 306
Or     Country <Ctry> [1..1] CodeSet   'C5 307
Or     TypeAndIdentification <TpAndId> [1..1]  307
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 307
       Identification <Id> [1..1] IdentifierSet   'C4 308
Or}     Proprietary <Prtry> [1..1]  308
       Identification <Id> [0..1] Text 308
       Type <Tp> [1..1]  309
         Identification <Id> [1..1] Text 309
         Issuer <Issr> [1..1] Text 309
         SchemeName <SchmeNm> [0..1] Text 309
   SafekeepingAccount <SfkpgAcct> [0..1] ± 309
   ClearingSegment <ClrSgmt> [0..1] ± 309
   NonClearingMember <NonClrMmb> [0..1] ± 310
   IntendedSettlementDate <IntnddSttlmDt> [0..1] Date 310
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C8,
C9, C10,
  'C11,
  'C12
310
   TradeDate <TradDt> [0..1] Date 312
   DealPrice <DealPric> [0..1] ± 312
   Quantity <Qty> [1..1] ± 312
   Depository <Dpstry> [0..1] ± 313
   RemainingQuantityToBeSettled <RmngQtyToBeSttld> [0..1] ± 313
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 304
```

