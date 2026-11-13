---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.8 AccountDetails <AcctDtls>", "30.4.9.17 SettlementPartiesDetails <SttlmPtiesDtls>"]
file_pages: [769]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.9.17 SettlementPartiesDetails <SttlmPtiesDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 769 to 769.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 769

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
30.4.9.17  SettlementPartiesDetails <SttlmPtiesDtls>
Presence: [0..1]
Definition: Chain of parties involved in the settlement of the transaction.
SettlementPartiesDetails <SttlmPtiesDtls> contains the following FundSettlementParameters26
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TradeTransactionCondition <TradTxCond> [0..*] ± 770
   SettlementTransactionCondition <SttlmTxCond> [0..*] ± 770
   SecuritiesSettlementSystemIdentification
<SctiesSttlmSysId>
[0..1] Text 770
   DeliveringSideDetails <DlvrgSdDtls> [0..1]  C7, C11,
C26,
C27,
C28,
C29,
C33
770
     Depository <Dpstry> [0..1] ± 772
     Party1 <Pty1> [0..1] ± 773
     Party2 <Pty2> [0..1] ± 773
     Party3 <Pty3> [0..1] ± 773
     Party4 <Pty4> [0..1] ± 774
     Party5 <Pty5> [0..1] ± 774
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 769 May 2026
```

