---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "36.4 Message Building Blocks", "36.4.12 TransferorAccount <TrfrAcct>", "36.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "36.4.15.11.29 SettlementPartiesDetails <SttlmPtiesDtls>", "36.4.15.11.29.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [1289]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.013.001.12"]
---

# 36.4.15.11.29.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1289 to 1289.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1289

```text
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [0..1] ± 1289
   TradeTransactionCondition <TradTxCond> [0..*] ± 1290
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1290
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1290
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1291
     Depository <Dpstry> [0..1] ± 1292
     Party1 <Pty1> [0..1] ± 1293
     Party2 <Pty2> [0..1] ± 1293
     Party3 <Pty3> [0..1] ± 1294
     Party4 <Pty4> [0..1] ± 1294
     Party5 <Pty5> [0..1] ± 1295
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1295
     Depository <Dpstry> [0..1] ± 1297
     Party1 <Pty1> [0..1] ± 1298
     Party2 <Pty2> [0..1] ± 1298
     Party3 <Pty3> [0..1] ± 1298
     Party4 <Pty4> [0..1] ± 1299
     Party5 <Pty5> [0..1] ± 1299
36.4.15.11.29.1  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository or an International Central Securities
Depository.
Approved by the Securities SEG on 27 January 2026 sese.013.001.12 PortfolioTransferConfirmationV12
Investment Funds - Maintenance 2025 - 2026 1289 May 2026
```

