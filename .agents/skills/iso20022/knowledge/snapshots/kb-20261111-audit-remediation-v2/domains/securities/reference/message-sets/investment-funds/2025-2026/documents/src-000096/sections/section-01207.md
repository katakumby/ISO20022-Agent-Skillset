---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.29 SettlementPartiesDetails <SttlmPtiesDtls>", "40.4.15.11.29.1 SafekeepingPlace <SfkpgPlc>"]
file_pages: [1672]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.29.1 SafekeepingPlace <SfkpgPlc>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1672 to 1672.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1672

```text
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters24
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlace <SfkpgPlc> [0..1] ± 1672
   TradeTransactionCondition <TradTxCond> [0..*] ± 1673
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 1673
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 1673
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1674
     Depository <Dpstry> [0..1] ± 1675
     Party1 <Pty1> [0..1] ± 1676
     Party2 <Pty2> [0..1] ± 1676
     Party3 <Pty3> [0..1] ± 1677
     Party4 <Pty4> [0..1] ± 1677
     Party5 <Pty5> [0..1] ± 1678
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C12,
C20,
C38,
C39,
C40,
C41,
C47
1678
     Depository <Dpstry> [0..1] ± 1680
     Party1 <Pty1> [0..1] ± 1681
     Party2 <Pty2> [0..1] ± 1681
     Party3 <Pty3> [0..1] ± 1681
     Party4 <Pty4> [0..1] ± 1682
     Party5 <Pty5> [0..1] ± 1682
40.4.15.11.29.1  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Place where the securities are safe-kept, physically or notionally. This place can be, for
example, a local custodian, a Central Securities Depository or an International Central Securities
Depository.
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1672 May 2026
```

