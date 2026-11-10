---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.1 Equity <Eqty>"]
file_pages: [1210]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.1 Equity <Eqty>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1210 to 1210.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1210

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1289
         CashAmount <CshAmt> [0..1] Amount C1, C5 1289
         CashType <CshTp> [0..1] Text 1290
         Price <Pric> [0..1]  1290
           ValueType <ValTp> [0..1] CodeSet 1290
           Value <Val> [1..1] ± 1291
           PriceType <PricTp> [0..1] CodeSet 1291
         DirtyPrice <DrtyPric> [0..1]  1292
           ValueType <ValTp> [0..1] CodeSet 1292
           Value <Val> [1..1] ± 1293
           PriceType <PricTp> [0..1] CodeSet 1293
         EndPrice <EndPric> [0..1]  1294
           ValueType <ValTp> [0..1] CodeSet 1294
           Value <Val> [1..1] ± 1295
           PriceType <PricTp> [0..1] CodeSet 1295
         StartValue <StartVal> [0..1] Amount C1, C5 1296
         CurrentValue <CurVal> [0..1] Amount C1, C5 1296
         EndValue <EndVal> [0..1] Amount C1, C5 1297
         AdjustedQuantity <AdjstdQty> [0..1]  1297
{Or           Unit <Unit> [1..1] Quantity 1297
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1298
         ExchangeRate <XchgRate> [0..1] Rate 1298
         CapValue <CapVal> [0..1] Amount C1, C5 1298
28.4.2.1.2.1.1  Equity <Eqty>
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
Target2-Securities 1210 August 2026
```

