---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.2 Structure"]
file_pages: [295]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
---

# 10.2 Structure

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 295 to 295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

```text
10.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BuyInConf> [1..1]  
   TransactionIdentification <TxId> [0..1] Text 299
   ClearingMember <ClrMmb> [1..1] ± 299
   BuyInDetails <BuyInDtls> [1..1]  299
     BuyInNotificationIdentification <BuyInNtfctnId> [0..1] Text 300
     BuyInIdentification <BuyInId> [1..1] Text 300
     Date <Dt> [1..1] Date 300
     Price <Pric> [0..1] ± 300
     SecuritiesBuyIn <SctiesBuyIn> [0..1]  301
       Depository <Dpstry> [1..1] ± 301
       SettlementAmount <SttlmAmt> [1..1] ± 301
       Fees <Fees> [0..1] ± 302
     RequiredCashCompensation <ReqrdCshCompstn> [0..1]  302
       SettlementAmount <SttlmAmt> [1..1] ± 302
       Fees <Fees> [0..1] ± 302
       ValueDate <ValDt> [0..1] Date 303
   OriginalSettlementObligation <OrgnlSttlmOblgtn> [0..1]  303
     CSDTransactionIdentification <CSDTxId> [0..1] Text 305
     CentralCounterpartyTransactionIdentification
<CntrlCtrPtyTxId>
[0..1] Text 305
     PreviousBuyInIdentification <PrvsBuyInId> [0..1] Text 305
     DeliveryAccount <DlvryAcct> [0..1] ± 305
     SafekeepingPlace <SfkpgPlc> [0..1]  305
{Or       Identification <Id> [1..1]  306
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 306
         Identification <Id> [0..1] Text 306
Or       Country <Ctry> [1..1] CodeSet   'C5 307
Or       TypeAndIdentification <TpAndId> [1..1]  307
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 307
         Identification <Id> [1..1] IdentifierSet   'C4 308
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 295
```

