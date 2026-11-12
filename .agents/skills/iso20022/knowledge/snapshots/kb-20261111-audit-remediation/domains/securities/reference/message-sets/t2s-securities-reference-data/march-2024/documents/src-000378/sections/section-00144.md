---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.2 Asset", "13.1.2.3 Debt5", "13.1.2.3.21 PutableIndicator <PutblInd>"]
file_pages: [206]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.2.3.21 PutableIndicator <PutblInd>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 206 to 206.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 206

```text
13.1.2.3.21  PutableIndicator <PutblInd>
Presence: [0..1]
Definition: Indicates whether the holder has the right to ask for redemption of the security prior to final
maturity. Also called RedeemableIndicator.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.22  PreFundedIndicator <PreFnddInd>
Presence: [0..1]
Definition: Indicates whether an interest bearing instrument is being escrowed or collateralized either by
direct obligations guaranteed by the US government, or by other types of securities. The maturity
schedules of the securities in the escrow fund are determined in such a way to pay the maturity value,
coupon, and premium payments (if any) of the refunded bonds.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.23  EscrowedIndicator <EscrwdInd>
Presence: [0..1]
Definition: Indicates whether an interest bearing instrument is deposited in a fund that will be used to
pay debt service on refunded securities.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.24  PerpetualIndicator <PerptlInd>
Presence: [0..1]
Definition: Indicates whether the security has no maturity date.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
13.1.2.3.25  SubordinatedIndicator <SubrdntdInd>
Presence: [0..1]
Definition: Indicates whether the security is a subordinated security.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 531):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 206 March 2024
```

