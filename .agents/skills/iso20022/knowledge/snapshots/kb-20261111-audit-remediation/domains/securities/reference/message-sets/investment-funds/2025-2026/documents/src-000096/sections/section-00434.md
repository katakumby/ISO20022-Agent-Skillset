---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.4 Message Building Blocks", "26.4.6 TransferDetails <TrfDtls>", "26.4.8.17 SettlementPartiesDetails <SttlmPtiesDtls>"]
file_pages: [593]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.4.8.17 SettlementPartiesDetails <SttlmPtiesDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 593 to 593.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 593

```text
QuotedCurrency EUR
ExchangeRate 0.769.
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms37"
on page 4532 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ToAmount <ToAmt> [0..1] Amount C1, C13 4532
   FromAmount <FrAmt> [0..1] Amount C1, C13 4532
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 4533
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 4533
   ExchangeRate <XchgRate> [1..1] Rate 4534
   QuotationDate <QtnDt> [0..1] DateTime 4534
   QuotingInstitution <QtgInstn> [0..1] ± 4534
26.4.8.17  SettlementPartiesDetails <SttlmPtiesDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of the transaction.
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters25
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeTransactionCondition <TradTxCond> [0..*] ± 594
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 594
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 594
   ReceivingSideDetails <RcvgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
594
     Depository <Dpstry> [0..1] ± 596
     Party1 <Pty1> [0..1] ± 597
     Party2 <Pty2> [0..1] ± 597
     Party3 <Pty3> [0..1] ± 597
     Party4 <Pty4> [0..1] ± 598
     Party5 <Pty5> [0..1] ± 598
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 593 May 2026
```

