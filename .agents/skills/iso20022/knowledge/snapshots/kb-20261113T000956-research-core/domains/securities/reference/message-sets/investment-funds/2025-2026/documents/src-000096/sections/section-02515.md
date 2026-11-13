---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.12 SettlementMethod <SttlmMtd>"]
file_pages: [3543]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.12 SettlementMethod <SttlmMtd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3543 to 3543.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3543

```text
53.4.5.12  SettlementMethod <SttlmMtd>
Presence: [0..1]
Definition: Method by which the transaction is settled.
Datatype: "DeliveryReceiptType2Code" on page 5294
CodeName Name Definition
FREE SeparateSettlement Settlement of the financial instrument
and cash is separate.
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
53.4.5.13  AdditionalAmount <AddtlAmt>
Presence: [0..1]
Definition: Choice between additional cash in or resulting cash out.
AdditionalAmount <AddtlAmt> contains one of the following elements (see
"AdditionalAmount1Choice" on page 4774 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AdditionalCashIn <AddtlCshIn> [1..1] Amount C2, C10 4774
Or}   ResultingCashOut <RsltgCshOut> [1..1] Amount C2, C10 4775
53.4.5.14  ExpiryDateTime <XpryDtTm>
Presence: [0..1]
Definition: Date on which the order expires.
ExpiryDateTime <XpryDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4468
Or}   DateTime <DtTm> [1..1] DateTime 4468
53.4.5.15  CancellationRight <CxlRght>
Presence: [0..1]
Definition: Cancellation right of the investor with respect to the investment fund order.
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3543 May 2026
```

