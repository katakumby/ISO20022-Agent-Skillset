---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["9 MX secl.008.001.03 BuyInResponseV03", "9.2 Structure"]
file_pages: [275]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.008.001.03"]
---

# 9.2 Structure

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 275 to 275.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 275

```text
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BuyInRspn> [1..1]  
   TransactionIdentification <TxId> [0..1] Text 279
   BuyInResponseDetails <BuyInRspnDtls> [1..1]  279
     BuyInNotificationIdentification <BuyInNtfctnId> [1..1] Text 279
     RequestForDelayIndicator <ReqForDelyInd> [1..1] Indicator 279
     NumberOfDays <NbOfDays> [1..1] Quantity 280
     InitialQuantity <InitlQty> [1..1] ± 280
     CoveredQuantity <CvrdQty> [1..1] ± 280
     UncoveredQuantity <UcvrdQty> [1..1] ± 280
   OriginalSettlementObligationDetails <OrgnlSttlmOblgtnDtls> [0..1]  281
     CSDTransactionIdentification <CSDTxId> [0..1] Text 283
     CentralCounterpartyTransactionIdentification
<CntrlCtrPtyTxId>
[0..1] Text 283
     PreviousBuyInIdentification <PrvsBuyInId> [0..1] Text 283
     DeliveryAccount <DlvryAcct> [0..1] ± 283
     SafekeepingPlace <SfkpgPlc> [0..1]  283
{Or       Identification <Id> [1..1]  284
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 284
         Identification <Id> [0..1] Text 284
Or       Country <Ctry> [1..1] CodeSet   'C5 285
Or       TypeAndIdentification <TpAndId> [1..1]  285
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 285
         Identification <Id> [1..1] IdentifierSet   'C4 286
Or}       Proprietary <Prtry> [1..1]  286
         Identification <Id> [0..1] Text 286
         Type <Tp> [1..1]  287
           Identification <Id> [1..1] Text 287
           Issuer <Issr> [1..1] Text 287
           SchemeName <SchmeNm> [0..1] Text 287
     SafekeepingAccount <SfkpgAcct> [0..1] ± 287
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.008.001.03 BuyInResponseV03
March 2026 275
```

