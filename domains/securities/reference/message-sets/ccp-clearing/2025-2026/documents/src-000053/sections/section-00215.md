---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.4 Message Building Blocks", "9.4.3 OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls>"]
file_pages: [281, 282]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.4.3 OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 281 to 282.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 281

```text
UncoveredQuantity <UcvrdQty> contains one of the following elements (see
FinancialInstrumentQuantity1Choice on page 396 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 396
Or   FaceAmount <FaceAmt> [1..1] Amount 396
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 396
9.4.3 OriginalSettlementObligationDetails
<OrgnlSttlmOblgtnDtls>
Presence: [0..1]
Definition: Provides details about the original settlement obligation that did not settle and for which the
buy in process will be launched.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 281
```

## File page 282

```text
OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls> contains the following
SettlementObligation7 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CSDTransactionIdentification <CSDTxId> [0..1] Text 283
   CentralCounterpartyTransactionIdentification
<CntrlCtrPtyTxId>
[0..1] Text 283
   PreviousBuyInIdentification <PrvsBuyInId> [0..1] Text 283
   DeliveryAccount <DlvryAcct> [0..1] ± 283
   SafekeepingPlace <SfkpgPlc> [0..1]  283
{Or     Identification <Id> [1..1]  284
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 284
       Identification <Id> [0..1] Text 284
Or     Country <Ctry> [1..1] CodeSet   'C5 285
Or     TypeAndIdentification <TpAndId> [1..1]  285
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 285
       Identification <Id> [1..1] IdentifierSet   'C4 286
Or}     Proprietary <Prtry> [1..1]  286
       Identification <Id> [0..1] Text 286
       Type <Tp> [1..1]  287
         Identification <Id> [1..1] Text 287
         Issuer <Issr> [1..1] Text 287
         SchemeName <SchmeNm> [0..1] Text 287
   SafekeepingAccount <SfkpgAcct> [0..1] ± 287
   ClearingSegment <ClrSgmt> [0..1] ± 287
   NonClearingMember <NonClrMmb> [0..1] ± 288
   IntendedSettlementDate <IntnddSttlmDt> [0..1] Date 288
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C8,
C9, C10,
  'C11,
  'C12
288
   TradeDate <TradDt> [0..1] Date 290
   DealPrice <DealPric> [0..1] ± 290
   Quantity <Qty> [1..1] ± 290
   Depository <Dpstry> [0..1] ± 291
   RemainingQuantityToBeSettled <RmngQtyToBeSttld> [0..1] ± 291
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 282
```

