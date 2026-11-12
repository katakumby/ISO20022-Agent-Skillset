---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.18 SettlementPartiesDetails <SttlmPtiesDtls>", "38.4.15.8.18.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [1429]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.18.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1429 to 1429.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1429

```text
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [0..1] ± 1429
   TradeTransactionCondition <TradTxCond> [0..*] ± 1430
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1430
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1430
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C11,
C17,
C32,
C33,
C34,
C35,
C40
1431
     Depository <Dpstry> [0..1] ± 1432
     Party1 <Pty1> [0..1] ± 1433
     Party2 <Pty2> [0..1] ± 1433
     Party3 <Pty3> [0..1] ± 1434
     Party4 <Pty4> [0..1] ± 1434
     Party5 <Pty5> [0..1] ± 1435
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C11,
C17,
C32,
C33,
C34,
C35,
C40
1435
     Depository <Dpstry> [0..1] ± 1437
     Party1 <Pty1> [0..1] ± 1438
     Party2 <Pty2> [0..1] ± 1438
     Party3 <Pty3> [0..1] ± 1438
     Party4 <Pty4> [0..1] ± 1439
     Party5 <Pty5> [0..1] ± 1439
38.4.15.8.18.1  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository or an International Central Securities
Depository.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1429 May 2026
```

