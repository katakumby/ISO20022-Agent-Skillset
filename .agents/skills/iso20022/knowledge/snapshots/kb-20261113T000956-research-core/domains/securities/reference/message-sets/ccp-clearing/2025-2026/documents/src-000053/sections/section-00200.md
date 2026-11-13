---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.4 Message Building Blocks", "8.4.3 NotificationDetails <NtfctnDtls>", "8.4.3.2 ExpectedBuyInDate <XpctdBuyInDt>", "8.4.3.2.1 Date <Dt>"]
file_pages: [261, 262]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.4.3.2.1 Date <Dt>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 261 to 262.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 261

```text
8.4.3.2.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as a calendar date.
Datatype: ISODate on page 487
8.4.3.2.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date is expressed using a code.
DateCode <DtCd> contains one of the following elements (see DateCode3Choice on page 389 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 389
Or}   Proprietary <Prtry> [1..1] ± C5 389
8.4.3.3  CancellationLimitDate <CxlLmtDt>
Presence: [0..1]
Definition: Identifies the latest date by which the buy-in operation can be cancelled.
Datatype: ISODate on page 487
8.4.3.4  BuyInReversionDate <BuyInRvrsnDt>
Presence: [0..1]
Definition: Identifies the date by which the buy-in operation is reversed by the CCP.
Datatype: ISODate on page 487
8.4.4 OriginalSettlementObligation <OrgnlSttlmOblgtn>
Presence: [1..1]
Definition: Provides details about the original settlement obligation that did not settle and for which the
buy in process will be launched.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 261
```

## File page 262

```text
OriginalSettlementObligation <OrgnlSttlmOblgtn> contains the following SettlementObligation7
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CSDTransactionIdentification <CSDTxId> [0..1] Text 263
   CentralCounterpartyTransactionIdentification
<CntrlCtrPtyTxId>
[0..1] Text 263
   PreviousBuyInIdentification <PrvsBuyInId> [0..1] Text 263
   DeliveryAccount <DlvryAcct> [0..1] ± 263
   SafekeepingPlace <SfkpgPlc> [0..1]  263
{Or     Identification <Id> [1..1]  264
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 264
       Identification <Id> [0..1] Text 264
Or     Country <Ctry> [1..1] CodeSet   'C6 265
Or     TypeAndIdentification <TpAndId> [1..1]  265
       SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 265
       Identification <Id> [1..1] IdentifierSet   'C4 266
Or}     Proprietary <Prtry> [1..1]  266
       Identification <Id> [0..1] Text 266
       Type <Tp> [1..1]  267
         Identification <Id> [1..1] Text 267
         Issuer <Issr> [1..1] Text 267
         SchemeName <SchmeNm> [0..1] Text 267
   SafekeepingAccount <SfkpgAcct> [0..1] ± 267
   ClearingSegment <ClrSgmt> [0..1] ± 267
   NonClearingMember <NonClrMmb> [0..1] ± 268
   IntendedSettlementDate <IntnddSttlmDt> [0..1] Date 268
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ±   'C9,
C10,
C11,
  'C12,
  'C13
268
   TradeDate <TradDt> [0..1] Date 270
   DealPrice <DealPric> [0..1] ± 270
   Quantity <Qty> [1..1] ± 270
   Depository <Dpstry> [0..1] ± 271
   RemainingQuantityToBeSettled <RmngQtyToBeSttld> [0..1] ± 271
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 262
```

