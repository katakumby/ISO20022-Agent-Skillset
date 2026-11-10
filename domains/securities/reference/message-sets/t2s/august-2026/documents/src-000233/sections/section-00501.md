---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.1 Equity <Eqty>"]
file_pages: [662]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.1 Equity <Eqty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 662 to 662.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 662

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 741
         CashAmount <CshAmt> [0..1] Amount C1, C5 741
         CashType <CshTp> [0..1] Text 742
         Price <Pric> [0..1]  742
           ValueType <ValTp> [0..1] CodeSet 742
           Value <Val> [1..1] ± 743
           PriceType <PricTp> [0..1] CodeSet 743
         DirtyPrice <DrtyPric> [0..1]  744
           ValueType <ValTp> [0..1] CodeSet 744
           Value <Val> [1..1] ± 745
           PriceType <PricTp> [0..1] CodeSet 745
         EndPrice <EndPric> [0..1]  746
           ValueType <ValTp> [0..1] CodeSet 746
           Value <Val> [1..1] ± 747
           PriceType <PricTp> [0..1] CodeSet 747
         StartValue <StartVal> [0..1] Amount C1, C5 748
         CurrentValue <CurVal> [0..1] Amount C1, C5 748
         EndValue <EndVal> [0..1] Amount C1, C5 749
         AdjustedQuantity <AdjstdQty> [0..1]  749
{Or           Unit <Unit> [1..1] Quantity 749
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 750
         ExchangeRate <XchgRate> [0..1] Rate 750
         CapValue <CapVal> [0..1] Amount C1, C5 750
27.4.2.2.1  Equity <Eqty>
Presence: [0..1]
Definition: Financial instrument which represents a title of ownership in a company, ie, the shareholder
is entitled to a part of the company's profit - usually by payment of a dividend - and to voting rights, if
any. Each company issues generally different classes of shares, eg, ordinary or common shares, which
have no guaranteed amount of dividend but carry voting rights, or preferred shares, which receive
dividends before ordinary shares but have no voting right.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 662 August 2026
```

