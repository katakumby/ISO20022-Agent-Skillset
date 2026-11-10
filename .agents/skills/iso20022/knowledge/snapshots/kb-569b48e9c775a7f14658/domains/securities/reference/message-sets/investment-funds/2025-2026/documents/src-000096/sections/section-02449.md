---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.4 Message Building Blocks", "52.4.2 PoolReference <PoolRef>", "52.4.5.10 IndividualExecutionDetails <IndvExctnDtls>", "52.4.5.10.47 CustomerConductClassification <CstmrCndctClssfctn>"]
file_pages: [3426]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.4.5.10.47 CustomerConductClassification <CstmrCndctClssfctn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3426 to 3426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3426

```text
SourceOfCash <SrcOfCsh> contains one of the following elements (see "SourceOfCash1Choice" on
page 5045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5045
Or}   Proprietary <Prtry> [1..1] ± 5046
52.4.5.10.47  CustomerConductClassification <CstmrCndctClssfctn>
Presence: [0..1]
Definition: Assessment of the customer's behaviour at the time of the account opening application.
CustomerConductClassification <CstmrCndctClssfctn> contains one of the following elements (see
"CustomerConductClassification1Choice" on page 4663 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4663
Or}   Proprietary <Prtry> [1..1] ± 4664
52.4.5.10.48  TransactionChannelType <TxChanlTp>
Presence: [0..1]
Definition: Means by which the investor or account owner submits the open account form.
TransactionChannelType <TxChanlTp> contains one of the following elements (see
"TransactionChannelType1Choice" on page 4824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4824
Or}   Proprietary <Prtry> [1..1] ± 4824
52.4.5.10.49  SignatureType <SgntrTp>
Presence: [0..1]
Definition: Type of signature.
SignatureType <SgntrTp> contains one of the following elements (see "SignatureType1Choice" on
page 4845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4845
Or}   Proprietary <Prtry> [1..1] ± 4846
52.4.5.10.50  OrderWaiverDetails <OrdrWvrDtls>
Presence: [0..1]
Definition: Information about a non-standard order.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3426 May 2026
```

