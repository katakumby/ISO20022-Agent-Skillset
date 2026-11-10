---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.49 SecuritiesFinancing12", "7.1.19.49.4 LegalFramework <LglFrmwk>"]
file_pages: [361]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.49.4 LegalFramework <LglFrmwk>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 361 to 361.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 361

```text
7.1.19.49.4  LegalFramework <LglFrmwk>
Presence: [0..1]
Definition: Legal framework of the transaction.
Datatype: "LegalFramework1Code" on page 634
CodeName Name Definition
FRAN PensionLivree Relates to the French legal framework
for repos, that is, relates to a "Pension
Livrée".
7.1.19.49.5  InterestComputationMethod <IntrstCmptnMtd>
Presence: [0..1]
Definition: Identifies the computation method of accrued interest of the related financial instrument.
InterestComputationMethod <IntrstCmptnMtd> contains one of the following elements (see
"InterestComputationMethod3Choice" on page 291 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 291
Or}   Proprietary <Prtry> [1..1] ± 294
7.1.19.49.6  VariableRateSupport <VarblRateSpprt>
Presence: [0..1]
Definition: Index or support rate used together with the spread to calculate the repurchase rate.
VariableRateSupport <VarblRateSpprt> contains the following elements (see "RateName1" on
page 515 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 516
   RateName <RateNm> [1..1] Text 516
7.1.19.49.7  RepurchaseRate <RpRate>
Presence: [0..1]
Definition: Repurchase rate used to calculate the repurchase amount.
Impacted by: C48 "SignRule"
RepurchaseRate <RpRate> contains the following elements (see "Rate2" on page 517 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 517
   Rate <Rate> [1..1] Rate 517
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 361 February 2025
```

