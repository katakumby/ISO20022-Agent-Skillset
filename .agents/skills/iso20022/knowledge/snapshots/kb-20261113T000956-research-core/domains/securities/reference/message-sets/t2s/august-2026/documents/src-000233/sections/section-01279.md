---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.1 Equity <Eqty>"]
file_pages: [1864]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.1 Equity <Eqty>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1864 to 1864.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1864

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 1943
         CashAmount <CshAmt> [0..1] Amount C1, C5 1943
         CashType <CshTp> [0..1] Text 1944
         Price <Pric> [0..1]  1944
           ValueType <ValTp> [0..1] CodeSet 1944
           Value <Val> [1..1] ± 1945
           PriceType <PricTp> [0..1] CodeSet 1945
         DirtyPrice <DrtyPric> [0..1]  1946
           ValueType <ValTp> [0..1] CodeSet 1946
           Value <Val> [1..1] ± 1947
           PriceType <PricTp> [0..1] CodeSet 1947
         EndPrice <EndPric> [0..1]  1948
           ValueType <ValTp> [0..1] CodeSet 1948
           Value <Val> [1..1] ± 1949
           PriceType <PricTp> [0..1] CodeSet 1949
         StartValue <StartVal> [0..1] Amount C1, C5 1950
         CurrentValue <CurVal> [0..1] Amount C1, C5 1950
         EndValue <EndVal> [0..1] Amount C1, C5 1951
         AdjustedQuantity <AdjstdQty> [0..1]  1951
{Or           Unit <Unit> [1..1] Quantity 1951
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 1952
         ExchangeRate <XchgRate> [0..1] Rate 1952
         CapValue <CapVal> [0..1] Amount C1, C5 1952
32.4.3.1.1.2.1  Equity <Eqty>
Presence: [0..1]
Definition: Financial instrument which represents a title of ownership in a company, ie, the shareholder
is entitled to a part of the company's profit - usually by payment of a dividend - and to voting rights, if
any. Each company issues generally different classes of shares, eg, ordinary or common shares, which
have no guaranteed amount of dividend but carry voting rights, or preferred shares, which receive
dividends before ordinary shares but have no voting right.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1864 August 2026
```

