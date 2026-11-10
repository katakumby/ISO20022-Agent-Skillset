---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.30 SourceOfCash <SrcOfCsh>"]
file_pages: [3181]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.30 SourceOfCash <SrcOfCsh>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3181 to 3181.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3181

```text
Equalisation <Equlstn> contains the following elements (see "Equalisation1" on page 4775 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4775
   Rate <Rate> [0..1] Rate 4776
50.4.4.9.30  SourceOfCash <SrcOfCsh>
Presence: [0..*]
Definition: Source of cash used for the settlement of the subscription.
SourceOfCash <SrcOfCsh> contains one of the following elements (see "SourceOfCash1Choice" on
page 5045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5045
Or}   Proprietary <Prtry> [1..1] ± 5046
50.4.4.9.31  CustomerConductClassification <CstmrCndctClssfctn>
Presence: [0..1]
Definition: Assessment of the customer's behaviour at the time of the account opening application.
CustomerConductClassification <CstmrCndctClssfctn> contains one of the following elements (see
"CustomerConductClassification1Choice" on page 4663 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4663
Or}   Proprietary <Prtry> [1..1] ± 4664
50.4.4.9.32  TransactionChannelType <TxChanlTp>
Presence: [0..1]
Definition: Means by which the investor or account owner submits the open account form.
TransactionChannelType <TxChanlTp> contains one of the following elements (see
"TransactionChannelType1Choice" on page 4824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4824
Or}   Proprietary <Prtry> [1..1] ± 4824
50.4.4.9.33  SignatureType <SgntrTp>
Presence: [0..1]
Definition: Type of signature.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3181 May 2026
```

