---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.2 Structure"]
file_pages: [255]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.2 Structure

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 255 to 255.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 255

```text
8.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <BuyInNtfctn> [1..1]    'C15
   TransactionIdentification <TxId> [0..1] Text 259
   ClearingMember <ClrMmb> [1..1] ± 259
   NotificationDetails <NtfctnDtls> [0..1]  260
     WarningIndicator <WrngInd> [0..1] Indicator 260
     ExpectedBuyInDate <XpctdBuyInDt> [1..1]  260
{Or       Date <Dt> [1..1] Date 261
Or}       DateCode <DtCd> [1..1] ± 261
     CancellationLimitDate <CxlLmtDt> [0..1] Date 261
     BuyInReversionDate <BuyInRvrsnDt> [0..1] Date 261
   OriginalSettlementObligation <OrgnlSttlmOblgtn> [1..1]  261
     CSDTransactionIdentification <CSDTxId> [0..1] Text 263
     CentralCounterpartyTransactionIdentification
<CntrlCtrPtyTxId>
[0..1] Text 263
     PreviousBuyInIdentification <PrvsBuyInId> [0..1] Text 263
     DeliveryAccount <DlvryAcct> [0..1] ± 263
     SafekeepingPlace <SfkpgPlc> [0..1]  263
{Or       Identification <Id> [1..1]  264
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 264
         Identification <Id> [0..1] Text 264
Or       Country <Ctry> [1..1] CodeSet   'C6 265
Or       TypeAndIdentification <TpAndId> [1..1]  265
         SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 265
         Identification <Id> [1..1] IdentifierSet   'C4 266
Or}       Proprietary <Prtry> [1..1]  266
         Identification <Id> [0..1] Text 266
         Type <Tp> [1..1]  267
           Identification <Id> [1..1] Text 267
           Issuer <Issr> [1..1] Text 267
           SchemeName <SchmeNm> [0..1] Text 267
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 255
```

