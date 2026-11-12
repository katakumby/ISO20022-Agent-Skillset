---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.4 Message Building Blocks", "43.4.4 RelatedReference <RltdRef>", "43.4.5.9 IndividualExecutionDetails <IndvExctnDtls>", "43.4.5.9.43 CustomerConductClassification <CstmrCndctClssfctn>"]
file_pages: [2046]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.4.5.9.43 CustomerConductClassification <CstmrCndctClssfctn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2046 to 2046.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2046

```text
Definition: Part of an investor's subscription amount that was held by the fund in order to pay incentive/
performance fees at the end of the fiscal year, and is returned due to the redemption.
Equalisation <Equlstn> contains the following elements (see "Equalisation1" on page 4775 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C2, C10 4775
   Rate <Rate> [0..1] Rate 4776
43.4.5.9.43  CustomerConductClassification <CstmrCndctClssfctn>
Presence: [0..1]
Definition: Assessment of the customer's behaviour at the time of the account opening application.
CustomerConductClassification <CstmrCndctClssfctn> contains one of the following elements (see
"CustomerConductClassification1Choice" on page 4663 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4663
Or}   Proprietary <Prtry> [1..1] ± 4664
43.4.5.9.44  TransactionChannelType <TxChanlTp>
Presence: [0..1]
Definition: Means by which the investor or account owner submits the open account form.
TransactionChannelType <TxChanlTp> contains one of the following elements (see
"TransactionChannelType1Choice" on page 4824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4824
Or}   Proprietary <Prtry> [1..1] ± 4824
43.4.5.9.45  SignatureType <SgntrTp>
Presence: [0..1]
Definition: Type of signature.
SignatureType <SgntrTp> contains one of the following elements (see "SignatureType1Choice" on
page 4845 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4845
Or}   Proprietary <Prtry> [1..1] ± 4846
43.4.5.9.46  OrderWaiverDetails <OrdrWvrDtls>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2046 May 2026
```

