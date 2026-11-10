---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.1 Equity <Eqty>"]
file_pages: [1398]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.1 Equity <Eqty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1398 to 1398.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1398

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1477
         CashAmount <CshAmt> [0..1] Amount C1, C5 1477
         CashType <CshTp> [0..1] Text 1478
         Price <Pric> [0..1]  1478
           ValueType <ValTp> [0..1] CodeSet 1478
           Value <Val> [1..1] ± 1479
           PriceType <PricTp> [0..1] CodeSet 1479
         DirtyPrice <DrtyPric> [0..1]  1480
           ValueType <ValTp> [0..1] CodeSet 1480
           Value <Val> [1..1] ± 1481
           PriceType <PricTp> [0..1] CodeSet 1481
         EndPrice <EndPric> [0..1]  1482
           ValueType <ValTp> [0..1] CodeSet 1482
           Value <Val> [1..1] ± 1483
           PriceType <PricTp> [0..1] CodeSet 1483
         StartValue <StartVal> [0..1] Amount C1, C5 1484
         CurrentValue <CurVal> [0..1] Amount C1, C5 1484
         EndValue <EndVal> [0..1] Amount C1, C5 1485
         AdjustedQuantity <AdjstdQty> [0..1]  1485
{Or           Unit <Unit> [1..1] Quantity 1485
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1486
         ExchangeRate <XchgRate> [0..1] Rate 1486
         CapValue <CapVal> [0..1] Amount C1, C5 1486
28.4.2.1.3.1.1  Equity <Eqty>
Presence: [0..1]
Definition: Financial instrument which represents a title of ownership in a company, ie, the shareholder
is entitled to a part of the company's profit - usually by payment of a dividend - and to voting rights, if
any. Each company issues generally different classes of shares, eg, ordinary or common shares, which
have no guaranteed amount of dividend but carry voting rights, or preferred shares, which receive
dividends before ordinary shares but have no voting right.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1398 August 2026
```

