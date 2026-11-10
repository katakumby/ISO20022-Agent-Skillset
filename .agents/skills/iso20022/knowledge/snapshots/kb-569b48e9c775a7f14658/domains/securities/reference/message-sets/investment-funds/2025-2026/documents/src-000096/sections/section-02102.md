---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.4 Message Building Blocks", "49.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "49.4.5.9.45 CustomerConductClassification <CstmrCndctClssfctn>"]
file_pages: [2939]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.4.5.9.45 CustomerConductClassification <CstmrCndctClssfctn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2939 to 2939.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2939

```text
49.4.5.9.45  CustomerConductClassification <CstmrCndctClssfctn>
Presence: [0..1]
Definition: Assessment of the customer's behaviour at the time of the account opening application.
CustomerConductClassification <CstmrCndctClssfctn> contains one of the following elements (see
"CustomerConductClassification1Choice" on page 4663 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4663
Or}   Proprietary <Prtry> [1..1] ± 4664
49.4.5.9.46  TransactionChannelType <TxChanlTp>
Presence: [0..1]
Definition: Means by which the investor or account owner submits the open account form.
TransactionChannelType <TxChanlTp> contains one of the following elements (see
"TransactionChannelType1Choice" on page 4824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4824
Or}   Proprietary <Prtry> [1..1] ± 4824
49.4.5.9.47  SignatureType <SgntrTp>
Presence: [0..1]
Definition: Type of signature.
SignatureType <SgntrTp> contains one of the following elements (see "SignatureType1Choice" on
page 4845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4845
Or}   Proprietary <Prtry> [1..1] ± 4846
49.4.5.9.48  OrderWaiverDetails <OrdrWvrDtls>
Presence: [0..1]
Definition: Information about a non-standard order.
Impacted by: C40 "WaiverElementRule"
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2939 May 2026
```

