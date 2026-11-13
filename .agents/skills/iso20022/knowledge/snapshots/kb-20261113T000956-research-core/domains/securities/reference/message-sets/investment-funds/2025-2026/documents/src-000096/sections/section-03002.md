---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "56.4 Message Building Blocks", "56.4.3.3 SwitchOrderDetailsReport <SwtchOrdrDtlsRpt>", "56.4.3.3.11 NewDetails <NewDtls>"]
file_pages: [4203]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.016.001.05"]
---

# 56.4.3.3.11 NewDetails <NewDtls>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4203 to 4203.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4203

```text
OrderData <OrdrData> contains the following elements (see "FundOrderData6" on page 4763 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementAmount <SttlmAmt> [0..1] Amount C1, C13 4764
   SettlementMethod <SttlmMtd> [0..1] CodeSet 4764
   AdditionalAmount <AddtlAmt> [0..1] ± 4765
   UnitCurrency <UnitCcy> [0..1] CodeSet C1 4765
   QuotedCurrency <QtdCcy> [0..1] CodeSet C1 4765
Constraints
• SwitchOrderDataElementRule
One of the elements (SettlementAmount, SettlementMethod, AdditionalAmount, UnitCurrency,
QuotedCurrency) must be present.
56.4.3.3.11  NewDetails <NewDtls>
Presence: [0..1]
Definition: Expected execution information.
NewDetails <NewDtls> contains the following ExpectedExecution6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExpectedTradeDateTime <XpctdTradDtTm> [0..1] ± 4203
   ExpectedCashSettlementDate <XpctdCshSttlmDt> [0..1] Date 4203
56.4.3.3.11.1  ExpectedTradeDateTime <XpctdTradDtTm>
Presence: [0..1]
Definition: Expected date or expected date and time at which a price will be applied according to the
terms of the prospectus.
ExpectedTradeDateTime <XpctdTradDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
56.4.3.3.11.2  ExpectedCashSettlementDate <XpctdCshSttlmDt>
Presence: [0..1]
Definition: Expected date at which the financial instruments will be exchanged against cash.
Datatype: "ISODate" on page 5388
Approved by the Securities SEG on 27 January 2026 setr.016.001.05 OrderInstructionStatusReportV05
Investment Funds - Maintenance 2025 - 2026 4203 May 2026
```

