---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.3 Debt <Debt>", "27.4.2.2.3.22 PreFundedIndicator <PreFnddInd>"]
file_pages: [681]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.3.22 PreFundedIndicator <PreFnddInd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 681 to 681.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 681

```text
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.22  PreFundedIndicator <PreFnddInd>
Presence: [0..1]
Definition: Indicates whether an interest bearing instrument is being escrowed or collateralized either by
direct obligations guaranteed by the US government, or by other types of securities. The maturity
schedules of the securities in the escrow fund are determined in such a way to pay the maturity value,
coupon, and premium payments (if any) of the refunded bonds.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.23  EscrowedIndicator <EscrwdInd>
Presence: [0..1]
Definition: Indicates whether an interest bearing instrument is deposited in a fund that will be used to
pay debt service on refunded securities.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.24  PerpetualIndicator <PerptlInd>
Presence: [0..1]
Definition: Indicates whether the security has no maturity date.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.25  SubordinatedIndicator <SubrdntdInd>
Presence: [0..1]
Definition: Indicates whether the security is a subordinated security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
27.4.2.2.3.26  ExtendibleIndicator <XtndblInd>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 681 August 2026
```

